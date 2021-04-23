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
    temp = collections.OrderedDict(sorted(temp.items()))      
    return temp

def two_dimention_figure_bytes_per_sec(a,b):
    # MatplotLib
    plt.scatter(a, b,s=10)  # Matplotlib
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

for k in range(368,369):
    name = 'in_coming_pkt_numbers_355to364'

    ip_address,pt_num = open_csv_file('./data/' + name + '.csv')
    temp = dict_from_2_list_and_cal_total_in_value(ip_address,pt_num)
    ip_address = list(temp.keys())
    pt_num = list(temp.values())

    pps = []
    for i in range(len(temp)):
        pps.append(sum(pt_num[i])/2400)
    # print(max(pps))
    nlarget = heapq.nlargest(5, pps)
    m = []
    for j in range(len(nlarget)):
        for k in range(len(temp)):
            if(pps[k] == nlarget[j]):
                m.append(j)
    print()
    print("5 IP largest: ")
    for j in m:
        print(ip_address[j])

    ip_address.sort()
    print("from " + str(ip_address[0]))
    print("to " + str(ip_address[-1]))
    plt.subplots()
    # two_dimention_figure_bytes_per_sec(ip_address,bps)
    # plt.show()
    two_dimention_figure_packet_per_sec(ip_address,pps)
    plt.savefig("./figure/" + name + ".png")
    plt.show()
