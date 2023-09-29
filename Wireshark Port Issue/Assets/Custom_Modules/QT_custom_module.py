def duplicate_removal(arg1):
    no_dup_list = []
    dict1 = {}
    for i in arg1:
        if dict1.get(i):
            continue
        else:
            no_dup_list.append(i)
            dict1[i] = True
    return no_dup_list

# Wireshark config file path
file_path = "C:\\Users\\Rajeeb Kumar Sahu\\AppData\\Roaming\\Wireshark\\decode_as_entries"

def diameter_sctp_port_extractor():
    import re
    my_file = open(file_path)
    re_2_comp = re.compile(r',[0-9][0-9],')
    re_3_comp = re.compile(r',[0-9][0-9][0-9],')
    re_4_comp = re.compile(r',[0-9][0-9][0-9][0-9],')
    re_5_comp = re.compile(r',[0-9][0-9][0-9][0-9][0-9],')
    re_6_comp = re.compile(r',[0-9][0-9][0-9][0-9][0-9][0-9],')
    sctp_ports = []
    for line in my_file:
        if "Diameter" in line and "sctp" in line:
            if re.search(re_2_comp,line):
                temp = re.search(re_2_comp,line)
                port = re.search(r'[0-9][0-9]',temp.group())
                port = int(port.group())
                sctp_ports.append(port)
            elif re.search(re_3_comp,line):
                temp = re.search(re_3_comp,line)
                port = re.search(r'[0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                sctp_ports.append(port)
            elif re.search(re_4_comp,line):
                temp = re.search(re_4_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                sctp_ports.append(port)
            elif re.search(re_5_comp,line):
                temp = re.search(re_5_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                sctp_ports.append(port)
            elif re.search(re_6_comp,line):
                temp = re.search(re_6_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                sctp_ports.append(port)
            else:
                continue
        else:
            continue
    my_file.close()
    return sctp_ports

def diameter_tcp_port_extractor():
    import re
    my_file = open(file_path)
    re_2_comp = re.compile(r',[0-9][0-9],')
    re_3_comp = re.compile(r',[0-9][0-9][0-9],')
    re_4_comp = re.compile(r',[0-9][0-9][0-9][0-9],')
    re_5_comp = re.compile(r',[0-9][0-9][0-9][0-9][0-9],')
    re_6_comp = re.compile(r',[0-9][0-9][0-9][0-9][0-9][0-9],')
    tcp_ports = []
    for line in my_file:
        if "Diameter" in line and "tcp" in line:
            if re.search(re_2_comp,line):
                temp = re.search(re_2_comp,line)
                port = re.search(r'[0-9][0-9]',temp.group())
                port = int(port.group())
                tcp_ports.append(port)
            elif re.search(re_3_comp,line):
                temp = re.search(re_3_comp,line)
                port = re.search(r'[0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                tcp_ports.append(port)
            elif re.search(re_4_comp,line):
                temp = re.search(re_4_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                tcp_ports.append(port)
            elif re.search(re_5_comp,line):
                temp = re.search(re_5_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                tcp_ports.append(port)
            elif re.search(re_6_comp,line):
                temp = re.search(re_6_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                tcp_ports.append(port)
            else:
                continue
        else:
            continue
    my_file.close()
    return tcp_ports

def diameter_udp_port_extractor():
    import re
    my_file = open(file_path)
    re_2_comp = re.compile(r',[0-9][0-9],')
    re_3_comp = re.compile(r',[0-9][0-9][0-9],')
    re_4_comp = re.compile(r',[0-9][0-9][0-9][0-9],')
    re_5_comp = re.compile(r',[0-9][0-9][0-9][0-9][0-9],')
    re_6_comp = re.compile(r',[0-9][0-9][0-9][0-9][0-9][0-9],')
    udp_ports = []
    for line in my_file:
        if "Diameter" in line and "udp" in line:
            if re.search(re_2_comp,line):
                temp = re.search(re_2_comp,line)
                port = re.search(r'[0-9][0-9]',temp.group())
                port = int(port.group())
                udp_ports.append(port)
            elif re.search(re_3_comp,line):
                temp = re.search(re_3_comp,line)
                port = re.search(r'[0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                udp_ports.append(port)
            elif re.search(re_4_comp,line):
                temp = re.search(re_4_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                udp_ports.append(port)
            elif re.search(re_5_comp,line):
                temp = re.search(re_5_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                udp_ports.append(port)
            elif re.search(re_6_comp,line):
                temp = re.search(re_6_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                udp_ports.append(port)
            else:
                continue
        else:
            continue
    my_file.close()
    return udp_ports

def sip_udp_port_extractor():
    import re
    my_file = open(file_path)
    re_2_comp = re.compile(r',[0-9][0-9],')
    re_3_comp = re.compile(r',[0-9][0-9][0-9],')
    re_4_comp = re.compile(r',[0-9][0-9][0-9][0-9],')
    re_5_comp = re.compile(r',[0-9][0-9][0-9][0-9][0-9],')
    re_6_comp = re.compile(r',[0-9][0-9][0-9][0-9][0-9][0-9],')
    udp_ports = []
    for line in my_file:
        if "SIP" in line and "udp" in line:
            if re.search(re_2_comp,line):
                temp = re.search(re_2_comp,line)
                port = re.search(r'[0-9][0-9]',temp.group())
                port = int(port.group())
                udp_ports.append(port)
            elif re.search(re_3_comp,line):
                temp = re.search(re_3_comp,line)
                port = re.search(r'[0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                udp_ports.append(port)
            elif re.search(re_4_comp,line):
                temp = re.search(re_4_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                udp_ports.append(port)
            elif re.search(re_5_comp,line):
                temp = re.search(re_5_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                udp_ports.append(port)
            elif re.search(re_6_comp,line):
                temp = re.search(re_6_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                udp_ports.append(port)
            else:
                continue
        else:
            continue
    my_file.close()
    return udp_ports

def sip_tcp_port_extractor():
    import re
    my_file = open(file_path)
    re_2_comp = re.compile(r',[0-9][0-9],')
    re_3_comp = re.compile(r',[0-9][0-9][0-9],')
    re_4_comp = re.compile(r',[0-9][0-9][0-9][0-9],')
    re_5_comp = re.compile(r',[0-9][0-9][0-9][0-9][0-9],')
    re_6_comp = re.compile(r',[0-9][0-9][0-9][0-9][0-9][0-9],')
    tcp_ports = []
    for line in my_file:
        if "SIP" in line and "tcp" in line:
            if re.search(re_2_comp,line):
                temp = re.search(re_2_comp,line)
                port = re.search(r'[0-9][0-9]',temp.group())
                port = int(port.group())
                tcp_ports.append(port)
            elif re.search(re_3_comp,line):
                temp = re.search(re_3_comp,line)
                port = re.search(r'[0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                tcp_ports.append(port)
            elif re.search(re_4_comp,line):
                temp = re.search(re_4_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                tcp_ports.append(port)
            elif re.search(re_5_comp,line):
                temp = re.search(re_5_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                tcp_ports.append(port)
            elif re.search(re_6_comp,line):
                temp = re.search(re_6_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                tcp_ports.append(port)
            else:
                continue
        else:
            continue
    my_file.close()
    return tcp_ports

def http_tcp_port_extractor():
    import re
    my_file = open(file_path)
    re_2_comp = re.compile(r',[0-9][0-9],')
    re_3_comp = re.compile(r',[0-9][0-9][0-9],')
    re_4_comp = re.compile(r',[0-9][0-9][0-9][0-9],')
    re_5_comp = re.compile(r',[0-9][0-9][0-9][0-9][0-9],')
    re_6_comp = re.compile(r',[0-9][0-9][0-9][0-9][0-9][0-9],')
    tcp_ports = []
    for line in my_file:
        if "HTTP" in line and "tcp" in line:
            if re.search(re_2_comp,line):
                temp = re.search(re_2_comp,line)
                port = re.search(r'[0-9][0-9]',temp.group())
                port = int(port.group())
                tcp_ports.append(port)
            elif re.search(re_3_comp,line):
                temp = re.search(re_3_comp,line)
                port = re.search(r'[0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                tcp_ports.append(port)
            elif re.search(re_4_comp,line):
                temp = re.search(re_4_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                tcp_ports.append(port)
            elif re.search(re_5_comp,line):
                temp = re.search(re_5_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                tcp_ports.append(port)
            elif re.search(re_6_comp,line):
                temp = re.search(re_6_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                tcp_ports.append(port)
            else:
                continue
        else:
            continue
    my_file.close()
    return tcp_ports

def http_sctp_port_extractor():
    import re
    my_file = open(file_path)
    re_2_comp = re.compile(r',[0-9][0-9],')
    re_3_comp = re.compile(r',[0-9][0-9][0-9],')
    re_4_comp = re.compile(r',[0-9][0-9][0-9][0-9],')
    re_5_comp = re.compile(r',[0-9][0-9][0-9][0-9][0-9],')
    re_6_comp = re.compile(r',[0-9][0-9][0-9][0-9][0-9][0-9],')
    sctp_ports = []
    for line in my_file:
        if "HTTP" in line and "sctp" in line:
            if re.search(re_2_comp,line):
                temp = re.search(re_2_comp,line)
                port = re.search(r'[0-9][0-9]',temp.group())
                port = int(port.group())
                sctp_ports.append(port)
            elif re.search(re_3_comp,line):
                temp = re.search(re_3_comp,line)
                port = re.search(r'[0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                sctp_ports.append(port)
            elif re.search(re_4_comp,line):
                temp = re.search(re_4_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                sctp_ports.append(port)
            elif re.search(re_5_comp,line):
                temp = re.search(re_5_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                sctp_ports.append(port)
            elif re.search(re_6_comp,line):
                temp = re.search(re_6_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                sctp_ports.append(port)
            else:
                continue
        else:
            continue
    my_file.close()
    return sctp_ports

def http2_tcp_port_extractor():
    import re
    my_file = open(file_path)
    re_2_comp = re.compile(r',[0-9][0-9],')
    re_3_comp = re.compile(r',[0-9][0-9][0-9],')
    re_4_comp = re.compile(r',[0-9][0-9][0-9][0-9],')
    re_5_comp = re.compile(r',[0-9][0-9][0-9][0-9][0-9],')
    re_6_comp = re.compile(r',[0-9][0-9][0-9][0-9][0-9][0-9],')
    tcp_ports = []
    for line in my_file:
        if "HTTP2" in line and "tcp" in line:
            if re.search(re_2_comp,line):
                temp = re.search(re_2_comp,line)
                port = re.search(r'[0-9][0-9]',temp.group())
                port = int(port.group())
                tcp_ports.append(port)
            elif re.search(re_3_comp,line):
                temp = re.search(re_3_comp,line)
                port = re.search(r'[0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                tcp_ports.append(port)
            elif re.search(re_4_comp,line):
                temp = re.search(re_4_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                tcp_ports.append(port)
            elif re.search(re_5_comp,line):
                temp = re.search(re_5_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                tcp_ports.append(port)
            elif re.search(re_6_comp,line):
                temp = re.search(re_6_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                tcp_ports.append(port)
            else:
                continue
        else:
            continue
    my_file.close()
    return tcp_ports

def tcp_udp_port_extractor():
    import re
    my_file = open(file_path)
    re_2_comp = re.compile(r',[0-9][0-9],')
    re_3_comp = re.compile(r',[0-9][0-9][0-9],')
    re_4_comp = re.compile(r',[0-9][0-9][0-9][0-9],')
    re_5_comp = re.compile(r',[0-9][0-9][0-9][0-9][0-9],')
    re_6_comp = re.compile(r',[0-9][0-9][0-9][0-9][0-9][0-9],')
    udp_ports = []
    for line in my_file:
        if "TCP" in line and "udp" in line:
            if re.search(re_2_comp,line):
                temp = re.search(re_2_comp,line)
                port = re.search(r'[0-9][0-9]',temp.group())
                port = int(port.group())
                udp_ports.append(port)
            elif re.search(re_3_comp,line):
                temp = re.search(re_3_comp,line)
                port = re.search(r'[0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                udp_ports.append(port)
            elif re.search(re_4_comp,line):
                temp = re.search(re_4_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                udp_ports.append(port)
            elif re.search(re_5_comp,line):
                temp = re.search(re_5_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                udp_ports.append(port)
            elif re.search(re_6_comp,line):
                temp = re.search(re_6_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                udp_ports.append(port)
            else:
                continue
        else:
            continue
    my_file.close()
    return udp_ports

def sctp_udp_port_extractor():
    import re
    my_file = open(file_path)
    re_2_comp = re.compile(r',[0-9][0-9],')
    re_3_comp = re.compile(r',[0-9][0-9][0-9],')
    re_4_comp = re.compile(r',[0-9][0-9][0-9][0-9],')
    re_5_comp = re.compile(r',[0-9][0-9][0-9][0-9][0-9],')
    re_6_comp = re.compile(r',[0-9][0-9][0-9][0-9][0-9][0-9],')
    udp_ports = []
    for line in my_file:
        if "SCTP" in line and "udp" in line:
            if re.search(re_2_comp,line):
                temp = re.search(re_2_comp,line)
                port = re.search(r'[0-9][0-9]',temp.group())
                port = int(port.group())
                udp_ports.append(port)
            elif re.search(re_3_comp,line):
                temp = re.search(re_3_comp,line)
                port = re.search(r'[0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                udp_ports.append(port)
            elif re.search(re_4_comp,line):
                temp = re.search(re_4_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                udp_ports.append(port)
            elif re.search(re_5_comp,line):
                temp = re.search(re_5_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                udp_ports.append(port)
            elif re.search(re_6_comp,line):
                temp = re.search(re_6_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                udp_ports.append(port)
            else:
                continue
        else:
            continue
    my_file.close()
    return udp_ports

def dns_udp_port_extractor():
    import re
    my_file = open(file_path)
    re_2_comp = re.compile(r',[0-9][0-9],')
    re_3_comp = re.compile(r',[0-9][0-9][0-9],')
    re_4_comp = re.compile(r',[0-9][0-9][0-9][0-9],')
    re_5_comp = re.compile(r',[0-9][0-9][0-9][0-9][0-9],')
    re_6_comp = re.compile(r',[0-9][0-9][0-9][0-9][0-9][0-9],')
    udp_ports = []
    for line in my_file:
        if "DNS" in line and "udp" in line:
            if re.search(re_2_comp,line):
                temp = re.search(re_2_comp,line)
                port = re.search(r'[0-9][0-9]',temp.group())
                port = int(port.group())
                udp_ports.append(port)
            elif re.search(re_3_comp,line):
                temp = re.search(re_3_comp,line)
                port = re.search(r'[0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                udp_ports.append(port)
            elif re.search(re_4_comp,line):
                temp = re.search(re_4_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                udp_ports.append(port)
            elif re.search(re_5_comp,line):
                temp = re.search(re_5_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                udp_ports.append(port)
            elif re.search(re_6_comp,line):
                temp = re.search(re_6_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                udp_ports.append(port)
            else:
                continue
        else:
            continue
    my_file.close()
    return udp_ports

def dns_tcp_port_extractor():
    import re
    my_file = open(file_path)
    re_2_comp = re.compile(r',[0-9][0-9],')
    re_3_comp = re.compile(r',[0-9][0-9][0-9],')
    re_4_comp = re.compile(r',[0-9][0-9][0-9][0-9],')
    re_5_comp = re.compile(r',[0-9][0-9][0-9][0-9][0-9],')
    re_6_comp = re.compile(r',[0-9][0-9][0-9][0-9][0-9][0-9],')
    tcp_ports = []
    for line in my_file:
        if "DNS" in line and "tcp" in line:
            if re.search(re_2_comp,line):
                temp = re.search(re_2_comp,line)
                port = re.search(r'[0-9][0-9]',temp.group())
                port = int(port.group())
                tcp_ports.append(port)
            elif re.search(re_3_comp,line):
                temp = re.search(re_3_comp,line)
                port = re.search(r'[0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                tcp_ports.append(port)
            elif re.search(re_4_comp,line):
                temp = re.search(re_4_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                tcp_ports.append(port)
            elif re.search(re_5_comp,line):
                temp = re.search(re_5_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                tcp_ports.append(port)
            elif re.search(re_6_comp,line):
                temp = re.search(re_6_comp,line)
                port = re.search(r'[0-9][0-9][0-9][0-9][0-9][0-9]',temp.group())
                port = int(port.group())
                tcp_ports.append(port)
            else:
                continue
        else:
            continue
    my_file.close()
    return tcp_ports

def diameter_sctp_port_writer(diameter_sctp_port_list):
    for port in diameter_sctp_port_list:
        count = 0
        with open(file_path, mode="r") as read_file:
            if f'sctp.port,{port},(none),Diameter' in read_file.read():
                count = 1
        write_file = open(file_path, mode="a")
        if count == 0:
            write_file.write(f'\ndecode_as_entry: sctp.port,{port},(none),Diameter')
        else:
            continue
        write_file.close()
    return f'All Diameter/SCTP ports have been added successfully.\n'

def diameter_tcp_port_writer(diameter_tcp_port_list):
    for port in diameter_tcp_port_list:
        count = 0
        with open(file_path, mode="r") as read_file:
            if f'tcp.port,{port},(none),Diameter' in read_file.read():
                count = 1
        write_file = open(file_path, mode="a")
        if count == 0:
            write_file.write(f'\ndecode_as_entry: tcp.port,{port},(none),Diameter')
        else:
            continue
        write_file.close()
    return f'All Diameter/TCP ports have been added successfully.\n'

def diameter_udp_port_writer(diameter_udp_port_list):
    for port in diameter_udp_port_list:
        count = 0
        with open(file_path, mode="r") as read_file:
            if f'udp.port,{port},(none),Diameter' in read_file.read():
                count = 1
        write_file = open(file_path, mode="a")
        if count == 0:
            write_file.write(f'\ndecode_as_entry: udp.port,{port},(none),Diameter')
        else:
            continue
        write_file.close()
    return f'All Diameter/UDP ports have been added successfully.\n'

def sip_udp_port_writer(sip_udp_port_list):
    for port in sip_udp_port_list:
        count = 0
        with open(file_path, mode="r") as read_file:
            if f'udp.port,{port},(none),SIP' in read_file.read():
                count = 1
        write_file = open(file_path, mode="a")
        if count == 0:
            write_file.write(f'\ndecode_as_entry: udp.port,{port},(none),SIP')
        else:
            continue
        write_file.close()
    return f'All SIP/UDP ports have been added successfully.\n'

def sip_tcp_port_writer(sip_tcp_port_list):
    for port in sip_tcp_port_list:
        count = 0
        with open(file_path, mode="r") as read_file:
            if f'tcp.port,{port},(none),SIP' in read_file.read():
                count = 1
        write_file = open(file_path, mode="a")
        if count == 0:
            write_file.write(f'\ndecode_as_entry: tcp.port,{port},(none),SIP')
        else:
            continue
        write_file.close()
    return f'All SIP/TCP ports have been added successfully.\n'

def http_tcp_port_writer(http_tcp_port_list):
    for port in http_tcp_port_list:
        count = 0
        with open(file_path, mode="r") as read_file:
            if f'tcp.port,{port},(none),HTTP' in read_file.read():
                count = 1
        write_file = open(file_path, mode="a")
        if count == 0:
            write_file.write(f'\ndecode_as_entry: tcp.port,{port},(none),HTTP')
        else:
            continue
        write_file.close()
    return f'All HTTP/TCP ports have been added successfully.\n'

def http_sctp_port_writer(http_sctp_port_list):
    for port in http_sctp_port_list:
        count = 0
        with open(file_path, mode="r") as read_file:
            if f'sctp.port,{port},(none),HTTP' in read_file.read():
                count = 1
        write_file = open(file_path, mode="a")
        if count == 0:
            write_file.write(f'\ndecode_as_entry: sctp.port,{port},(none),HTTP')
        else:
            continue
        write_file.close()
    return f'All HTTP/sctp ports have been added successfully.\n'

def http2_tcp_port_writer(http2_tcp_port_list):
    for port in http2_tcp_port_list:
        count = 0
        with open(file_path, mode="r") as read_file:
            if f'tcp.port,{port},(none),HTTP2' in read_file.read():
                count = 1
        write_file = open(file_path, mode="a")
        if count == 0:
            write_file.write(f'\ndecode_as_entry: tcp.port,{port},(none),HTTP2')
        else:
            continue
        write_file.close()
    return f'All HTTP2/tcp ports have been added successfully.\n'

def tcp_udp_port_writer(tcp_udp_port_list):
    for port in tcp_udp_port_list:
        count = 0
        with open(file_path, mode="r") as read_file:
            if f'udp.port,{port},(none),TCP' in read_file.read():
                count = 1
        write_file = open(file_path, mode="a")
        if count == 0:
            write_file.write(f'\ndecode_as_entry: udp.port,{port},(none),TCP')
        else:
            continue
        write_file.close()
    return f'All TCP/udp ports have been added successfully.\n'

def sctp_udp_port_writer(sctp_udp_port_list):
    for port in sctp_udp_port_list:
        count = 0
        with open(file_path, mode="r") as read_file:
            if f'udp.port,{port},(none),SCTP' in read_file.read():
                count = 1
        write_file = open(file_path, mode="a")
        if count == 0:
            write_file.write(f'\ndecode_as_entry: udp.port,{port},(none),SCTP')
        else:
            continue
        write_file.close()
    return f'All SCTP/udp ports have been added successfully.\n'

def dns_udp_port_writer(dns_udp_port_list):
    for port in dns_udp_port_list:
        count = 0
        with open(file_path, mode="r") as read_file:
            if f'udp.port,{port},(none),DNS' in read_file.read():
                count = 1
        write_file = open(file_path, mode="a")
        if count == 0:
            write_file.write(f'\ndecode_as_entry: udp.port,{port},(none),DNS')
        else:
            continue
        write_file.close()
    return f'All DNS/UDP ports have been added successfully.\n'

def dns_tcp_port_writer(dns_tcp_port_list):
    for port in dns_tcp_port_list:
        count = 0
        with open(file_path, mode="r") as read_file:
            if f'tcp.port,{port},(none),DNS' in read_file.read():
                count = 1
        write_file = open(file_path, mode="a")
        if count == 0:
            write_file.write(f'\ndecode_as_entry: tcp.port,{port},(none),DNS')
        else:
            continue
        write_file.close()
    return f'All DNS/TCP ports have been added successfully.\n'
