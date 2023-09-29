import Assets.Custom_Modules.Important_Methods as im
import Assets.Custom_Modules.Filter_Builder as fb
import pyshark

config = im.parser()
static_filter = fb.final_filter

# Adding GSM_MAP Filter (Start)
capture1 = pyshark.FileCapture(config.get("LTE_Trace","input"),display_filter=static_filter)

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

# Adding S1ap Filter (Start)
capture2 = pyshark.FileCapture(config.get("LTE_Trace","input"),display_filter=static_filter)

temp_mme_ue_s1ap_list = []
temp_enb_ue_s1ap_list = []
for packet in capture2:
    if "S1AP" in str(packet.layers):
        temp_enb_ue_s1ap_list.append(packet.s1ap.get("ENB_UE_S1AP_ID"))
        temp_mme_ue_s1ap_list.append(packet.s1ap.get("MME_UE_S1AP_ID"))
    else:
        continue

if temp_enb_ue_s1ap_list == []:
    pass
else:
    non_duplicate_end_ue_s1ap_id = im.duplicate_removal(temp_enb_ue_s1ap_list)
    for enb_ue_s1ap_id in non_duplicate_end_ue_s1ap_id:
        static_filter = static_filter + f' or s1ap.ENB_UE_S1AP_ID == {enb_ue_s1ap_id}'

if temp_mme_ue_s1ap_list == []:
    pass
else:
    non_duplicate_mme_ue_s1ap_id = im.duplicate_removal(temp_mme_ue_s1ap_list)
    for mme_ue_s1ap_id in non_duplicate_mme_ue_s1ap_id:
        static_filter = static_filter + f' or s1ap.MME_UE_S1AP_ID == {mme_ue_s1ap_id}'
# Adding S1ap Filter (End)

# Modify Bearer Request/Response
# Adding GTPv2 Filter (Start)
capture3 = pyshark.FileCapture(config.get("LTE_Trace","input"),display_filter=static_filter)

temp_gtpv2_f_teid_list = []
for packet in capture3:
    if "S1AP" in str(packet.layers):
        if packet.s1ap.get("procedureCode") == "9" or packet.s1ap.get("procedureCode") == "5":
            temp_gtpv2_f_teid_list.append(packet.s1ap.get("transportLayerAddressIPv4"))
        else:
            continue
    else:
        continue

if temp_gtpv2_f_teid_list == []:
    pass
else:
    non_duplicate_gtpv2_f_teid_list = im.duplicate_removal(temp_gtpv2_f_teid_list)
    for f_teid in non_duplicate_gtpv2_f_teid_list:
        static_filter = static_filter + f' or gtpv2.f_teid_ipv4 == {f_teid}'
# Adding GTPv2 Filter (End)

# Create Session Request/Response
# Adding GTPv2 Filter (Start)
capture4 = pyshark.FileCapture(config.get("LTE_Trace","input"),display_filter=static_filter)

temp_gtpv2_seq_list = []
for packet in capture4:
    if "GTPV2" in str(packet.layers):
        temp_gtpv2_seq_list.append(packet.gtpv2.get("seq"))
    else:
        continue

if temp_gtpv2_seq_list == []:
    pass
else:
    non_duplicate_gtpv2_seq_list = im.duplicate_removal(temp_gtpv2_seq_list)
    for seq in non_duplicate_gtpv2_seq_list:
        static_filter = static_filter + f' or gtpv2.seq == {seq}'
# Adding GTPv2 Filter (End)

# Adding Diameter Filter (Start)
capture5 = pyshark.FileCapture(config.get("LTE_Trace","input"),display_filter=static_filter)

temp_session_id_list = []
for packet in capture5:
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
capture6 = pyshark.FileCapture(config.get("LTE_Trace","input"),display_filter=static_filter,output_file=config.get("LTE_Trace","output"))
capture6.load_packets()
