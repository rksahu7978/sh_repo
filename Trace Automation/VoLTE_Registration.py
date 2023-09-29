import Assets.Custom_Modules.Important_Methods as im
import Assets.Custom_Modules.Filter_Builder as fb
import pyshark

config = im.parser()
static_filter = fb.final_filter

# Adding UE IP Filter (Start)
capture0 = pyshark.FileCapture(config.get("VoLTE_Trace","input"),display_filter=static_filter)

ue_ip = ""
for packet in capture0:
    if "SIP" in str(packet.layers):
        if packet.sip.get("Max-Forwards") == "70":
            ue_ip = packet.sip.get("contact.host") + ue_ip
            break

ue_ip = ue_ip[1:-1]
if ue_ip == "":
    pass
else:
    static_filter = f'{static_filter} or diameter.framed_ipv6_prefix_ipv6 == {ue_ip}'
# Adding UE IP Filter (End)

# Adding GSM_MAP Filter (Start)
capture1 = pyshark.FileCapture(config.get("VoLTE_Trace","input"),display_filter=static_filter)

temp_transaction_id_list = []
for packet in capture1:
    if "GSM_MAP" in str(packet.layers) and "TCAP" in str(packet.layers):
        temp_transaction_id_list.append(packet.tcap.get("tcap.tid"))
    else:
        continue

if temp_transaction_id_list == []:
    pass
else:
    non_duplicate_transaction_id_list = im.duplicate_removal(temp_transaction_id_list)
    for transaction_id in non_duplicate_transaction_id_list:
        static_filter = static_filter + f' or tcap.tid == {transaction_id}'
# Adding GSM_MAP Filter (End)

# Adding Diameter Filter (Start)
capture2 = pyshark.FileCapture(config.get("VoLTE_Trace","input"),display_filter=static_filter)

temp_session_id_list = []
for packet in capture2:
    if "DIAMETER" in str(packet.layers):
        temp_session_id_list.append(packet.diameter.get("Session-Id"))
    else:
        continue

if temp_session_id_list == []:
    pass
else:
    non_duplicate_session_id_list = im.duplicate_removal(temp_session_id_list)
    for session_id in non_duplicate_session_id_list:
        static_filter = static_filter + f' or diameter.Session-Id == "{session_id}"'
# Adding Diameter Filter (End)

print(f'{static_filter}\n')

# Saving the Trace
capture3 = pyshark.FileCapture(config.get("VoLTE_Trace","input"),display_filter=static_filter,output_file=config.get("VoLTE_Trace","output"))
capture3.load_packets()
