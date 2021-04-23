import matplotlib.pyplot as plt
import csv
import numpy as np
import collections
import matplotlib.pyplot as plt
import heapq

def dict_from_2_list_and_cal_total_in_value(a,b):
    temp= collections.defaultdict(set)
    for delvt, pin in zip(a, b):
        temp[delvt].add(pin)
    temp = collections.OrderedDict(sorted(temp.items()))        # SORT kEY FROM LOW TO HIGH
    return temp

def two_dimention_figure_bytes_per_sec(a,b):
    # MatplotLib
    plt.scatter(a, b, s=10)  # Matplotlib
    # plt.plot(a, b,'r^')  # Matplotlib
    plt.xlabel("IP")
    plt.ylabel("Bytes/s")
    plt.title(name + " " + str(len(a)) + " IP")
    # plt.show()

def two_dimention_figure_packet_per_sec(a,b):
    # MatplotLib
    plt.scatter(a, b,s=10)  # Matplotlib
    plt.xlabel("IP")
    plt.ylabel("Packet/s")
    plt.title(name + " " + str(len(a)) + " IP")
    # plt.show()

def open_csv_file(file_name):
    with open(file_name, mode='r') as f:
        loaded_file = np.loadtxt(f, delimiter=',', unpack=True)
    return loaded_file
# def dict_from_2_list(a,b):
#     temp= collections.defaultdict(set)
#     for delvt, pin in zip(a, b):
#         temp[delvt].add(pin)
#     temp = collections.OrderedDict(sorted(temp.items()))        
#     return temp

# with open('D:/data_analyzis/test1-10-ver2.csv','rt')as f:
#   ip_address,pkt_len,s_port= np.loadtxt(f, delimiter=',', unpack=True)


# temp= dict_from_2_list(ip_address,s_port)

# ip_address= list(temp.keys())
# s_port= list(temp.values())
# FPS=list()
# for i in range(len(temp)):
# 	counter= collections.Counter(s_port[i])
# 	FPS.append(len(counter.keys())/300)
   
# plt.axis([-1*1e9, 5*1e9, -1, 6])
# plt.plot(ip_address, FPS, 'go')
# plt.xlabel('IP')
# plt.ylabel('flows/s')
# plt.show()

import os, sys
path = "D:/data_analyzis/bps,pps/data1/"
lists = os.listdir(path)

for k in lists:
    name = k

    ip_address,pkt_len = open_csv_file(path + name )
    temp = dict_from_2_list_and_cal_total_in_value(ip_address,pkt_len)
    ip_address = list(temp.keys())
    pkt_len = list(temp.values())

    bps = []
    for i in range(len(temp)):
        bps.append(sum(pkt_len[i])/2400)

    # pps = []
    # # print(len(collections.Counter(pkt_len[0])))
    # for i in range(len(temp)):
    #     counter = collections.Counter(pkt_len[i])
    #     pps.append(len(counter)/300)					# len(couter) để lấy số lượng values trong từng key, nếu ko có len thì chỉ lấy đc số lượng từng value trong 1 key
    nlarget = heapq.nlargest(5, bps)
    m = []
    for j in range(len(nlarget)):
        for k in range(len(temp)):
            if(bps[k] == nlarget[j]):
                m.append(j)
    # print(m)
    print(nlarget)
    print("5 IP largest: ")
    for j in m:
        print(ip_address[j])

    ip_address.sort()
    print("from " + str(ip_address[0]))
    print("to " + str(ip_address[-1]))
    # for j in range(len(temp)):
    #     if(ip_address[j] == min(ip_address)):
    #         print("from IP: " + str(ip_address[j]))
    #         break
    #     # if(ip_address[j] == max(ip_address)):
    #     #     print("to IP: " + str(ip_address[j]))

    plt.subplots()
    two_dimention_figure_bytes_per_sec(ip_address,bps)
    plt.savefig("./figure/" + name + ".png")
    plt.show()
    # two_dimention_figure_packet_per_sec(ip_address,pps)
    # plt.show()
