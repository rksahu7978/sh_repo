import Assets.Custom_Modules.BT_custom_module as cms
import pyshark
import time

# Start time recorder
start = time.time()

# Designated trace path (Editable) 
trace_path = ".\\Assets\\Traces\\Trace1.pcapng"

options_dict = {
    1:"diameter",
    2:"sip",
    3:"http",
    4:"http2",
    5:"tcp",
    6:"sctp"
}

opt = '''
1 = DIAMETER Protocol
2 = SIP Protocol
3 = HTTP Protocol
4 = HTTP2 Protocol
5 = TCP Protocol
6 = SCTP Protocol
'''
print(opt)

user_option = int(input("Please choose a protocol : "))
print("\n")

# Existing DIAMETER ports lists (Editable)
diameter_sctp_port_list = cms.diameter_sctp_port_extractor()
diameter_tcp_port_list = cms.diameter_tcp_port_extractor()
diameter_udp_port_list = cms.diameter_udp_port_extractor()

# Existing SIP ports lists (Editable)
sip_tcp_port_list = cms.sip_tcp_port_extractor()
sip_udp_port_list = cms.sip_udp_port_extractor()

# Existing HTTP ports lists (Editable)
http_tcp_port_list = cms.http_tcp_port_extractor()
http_sctp_port_list = cms.http_sctp_port_extractor()

# Existing HTTP2 ports lists (Editable)
http2_tcp_port_list = cms.http2_tcp_port_extractor()

# Existing TCP/UDP ports lists (Editable)
tcp_udp_port_list = cms.tcp_udp_port_extractor()

# Existing SCTP/UDP ports lists (Editable)
sctp_udp_port_list = cms.sctp_udp_port_extractor()

if "diameter" == options_dict.get(user_option):
    diameter_sctp_list = []
    diameter_tcp_list = []
    diameter_udp_list = []
    capture = pyshark.FileCapture(trace_path)
    for packet in capture:
        if "DIAMETER" in str(packet.layers):
            if "SCTP" in str(packet.layers):
                diameter_sctp_list.append(int(packet.sctp.get("sctp.srcport")))
                diameter_sctp_list.append(int(packet.sctp.get("sctp.dstport")))
            if "TCP" in str(packet.layers):
                diameter_tcp_list.append(int(packet.tcp.get("tcp.srcport")))
                diameter_tcp_list.append(int(packet.tcp.get("tcp.dstport")))
            if "UDP" in str(packet.layers):
                diameter_udp_list.append(int(packet.udp.get("udp.srcport")))
                diameter_udp_list.append(int(packet.udp.get("udp.dstport")))
    
    temp_diameter_sctp_list = diameter_sctp_list + diameter_sctp_port_list
    temp_diameter_tcp_list = diameter_tcp_list + diameter_tcp_port_list
    temp_diameter_udp_list = diameter_udp_list + diameter_udp_port_list
    print(f'Diameter SCTP = {cms.duplicate_removal(temp_diameter_sctp_list)}\n')
    print(f'Diameter TCP = {cms.duplicate_removal(temp_diameter_tcp_list)}\n')
    print(f'Diameter UDP = {cms.duplicate_removal(temp_diameter_udp_list)}\n')

    print(cms.diameter_sctp_port_writer(temp_diameter_sctp_list))
    print(cms.diameter_tcp_port_writer(temp_diameter_tcp_list))
    print(cms.diameter_udp_port_writer(temp_diameter_udp_list))

    print("Please close all wireshark instances and reopen.\n")
elif "sip" == options_dict.get(user_option):
    sip_tcp_list = []
    sip_udp_list = []
    capture = pyshark.FileCapture(trace_path)
    for packet in capture:
        if "SIP" in str(packet.layers):
            if "TCP" in str(packet.layers):
                sip_tcp_list.append(int(packet.tcp.get("tcp.srcport")))
                sip_tcp_list.append(int(packet.tcp.get("tcp.dstport")))
            if "UDP" in str(packet.layers):
                sip_udp_list.append(int(packet.udp.get("udp.srcport")))
                sip_udp_list.append(int(packet.udp.get("udp.dstport")))
    
    temp_sip_tcp_list = sip_tcp_list + sip_tcp_port_list
    temp_sip_udp_list = sip_udp_list + sip_udp_port_list

    print(f'SIP TCP = {cms.duplicate_removal(temp_sip_tcp_list)}\n')
    print(f'SIP UDP = {cms.duplicate_removal(temp_sip_udp_list)}\n')

    print(cms.sip_tcp_port_writer(temp_sip_tcp_list))
    print(cms.sip_udp_port_writer(temp_sip_udp_list))

    print("Please close all wireshark instances and reopen.\n")
elif "http" == options_dict.get(user_option):
    http_tcp_list = []
    http_sctp_list = []
    capture = pyshark.FileCapture(trace_path)
    for packet in capture:
        if "HTTP" in str(packet.layers):
            if "TCP" in str(packet.layers):
                http_tcp_list.append(int(packet.tcp.get("tcp.srcport")))
                http_tcp_list.append(int(packet.tcp.get("tcp.dstport")))
            if "SCTP" in str(packet.layers):
                http_sctp_list.append(int(packet.sctp.get("sctp.srcport")))
                http_sctp_list.append(int(packet.sctp.get("sctp.dstport")))
    
    temp_http_tcp_list = http_tcp_list + http_tcp_port_list
    temp_http_sctp_list = http_sctp_list + http_sctp_port_list

    print(f'HTTP TCP = {cms.duplicate_removal(temp_http_tcp_list)}\n')
    print(f'HTTP SCTP = {cms.duplicate_removal(temp_http_sctp_list)}\n')

    print(cms.http_tcp_port_writer(temp_http_tcp_list))
    print(cms.http_sctp_port_writer(temp_http_sctp_list))

    print("Please close all wireshark instances and reopen.\n")
elif "http2" == options_dict.get(user_option):
    http2_tcp_list = []
    capture = pyshark.FileCapture(trace_path)
    for packet in capture:
        if "HTTP2" in str(packet.layers):
            if "EXPORTED_PDU" in str(packet.layers):
                http2_tcp_list.append(int(packet.exported_pdu.get("exported_pdu.src_port")))
                http2_tcp_list.append(int(packet.exported_pdu.get("exported_pdu.dst_port")))
            if "TCP" in packet:
                http2_tcp_list.append(int(packet.tcp.get("tcp.srcport")))
                http2_tcp_list.append(int(packet.tcp.get("tcp.dstport")))
    
    temp_http2_tcp_list = http2_tcp_list + http2_tcp_port_list

    print(f'HTTP2 TCP = {cms.duplicate_removal(temp_http2_tcp_list)}\n')

    print(cms.http2_tcp_port_writer(temp_http2_tcp_list))

    print("Please close all wireshark instances and reopen.\n")
elif "tcp" == options_dict.get(user_option):
    tcp_udp_list = []
    capture = pyshark.FileCapture(trace_path)
    for packet in capture:
        if "TCP" in str(packet.layers) and ("DIAMETER" and "SIP" not in str(packet.layers)) and ("HTTP" and "HTTP2" not in str(packet.layers)):
            tcp_udp_list.append(int(packet.tcp.get("tcp.srcport")))
            tcp_udp_list.append(int(packet.tcp.get("tcp.dstport")))
    
    temp_tcp_udp_list = tcp_udp_list + tcp_udp_port_list

    print(f'TCP/UDP = {cms.duplicate_removal(temp_tcp_udp_list)}\n')

    print(cms.tcp_udp_port_writer(temp_tcp_udp_list))

    print("Please close all wireshark instances and reopen.\n")
elif "sctp" == options_dict.get(user_option):
    sctp_udp_list = []
    capture = pyshark.FileCapture(trace_path)
    for packet in capture:
        if "SCTP" in str(packet.layers) and ("DIAMETER" and "SIP" not in str(packet.layers)) and ("HTTP" and "HTTP2" not in str(packet.layers)):
            sctp_udp_list.append(int(packet.sctp.get("sctp.srcport")))
            sctp_udp_list.append(int(packet.sctp.get("sctp.dstport")))
    
    temp_sctp_udp_list = sctp_udp_list + sctp_udp_port_list

    print(f'SCTP/UDP = {cms.duplicate_removal(temp_sctp_udp_list)}\n')

    print(cms.sctp_udp_port_writer(temp_sctp_udp_list))

    print("Please close all wireshark instances and reopen.\n")
else:
    print("Please choose a correct option\n")

# End time recorder
end = time.time()

# Time calculator
print(f'Total time taken = {end - start} Seconds\n')
