def int_ip2str(int_ip):
    a0 = str(int_ip & 0xff)
    a1 = str((int_ip & 0xff00) >> 8) 
    a2 = str((int_ip & 0xff0000) >> 16)
    a3 = str((int_ip & 0xff000000) >> 24)

    return ".".join([a3, a2, a1, a0])

a = int_ip2str(4294967295)
print(a)

def str_ip2_int(s_ip):
    lst = [int(item) for item in s_ip.split('.')]  
    # [192, 168, 1, 100]

    int_ip = lst[3] | lst[2] << 8 | lst[1] << 16 | lst[0] << 24
    return int_ip   # 3232235876
b = str_ip2_int('192.168.1.100')
print(b)