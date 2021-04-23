import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D 
# from sklearn.preprocessing import StandardScaler
# from sklearn.cluster import KMeans
import ipaddress
import heapq
import os, sys
path = "D:/data_analyzis/bps,pps/data/test/"
lists = os.listdir(path)

def three_dimention_plot(a,b,c,ip_number):
    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')
    ax1.scatter(a, b, c, s=10, c=None, depthshade=True)
    ax1.plot3D(a, b, c, c=None)
    ax1.set_xlabel('IP')
    ax1.set_ylabel('Times')
    ax1.set_zlabel('Bytes/s')
    ax1.set_title(name + " " + str(len(ip_number)) + " IP")

def three_dimention_surface(a,b,c,axes2,ip_number):
    # axes1.scatter(a, b,s=10)  # Matplotlib
    # # axes1.plot(a, b)
    # axes1.set_xlabel("IP")
    # axes1.set_ylabel("Times")
    # axes1.set_title(name + " " + str(len(ip_number)) + " IP")

    # axes2.scatter(b, c,s=10)  # Matplotlib
    axes2.plot(b, c, scaley = True, scalex = True)
    axes2.set_xlabel("Times")
    axes2.set_ylabel("Bytes/s")
    axes2.set_title(name + " " + str(len(ip_number)) + " IP")

    # axes3.scatter(a, c,s=10)  # Matplotlib
    # # axes3.plot(a, c)
    # axes3.set_xlabel("IP")
    # axes3.set_ylabel("Bytes/s")
    # axes3.set_title(name + " " + str(len(ip_number)) + " IP")

for name in lists:
    dataset = pd.read_csv(path + name , header=None, delim_whitespace=False)  #+ ".csv": neu co duoi .csv
    dataset = dataset.rename(columns={1: 'src'})
    dataset = dataset.rename(columns={6: 'timestamp'})
    dataset = dataset.rename(columns={20: 'bps'})
    # dataset = dataset.rename(columns={21: 'Flow Pkts/s'})  # vị trí số 6 trong file csv

    ip_times = dataset.pivot_table(index=['src'], aggfunc='size')
    dataset['src'].unique().tolist()
    df = dataset.pivot_table(index=['src', 'timestamp', 'bps'], aggfunc='size')
    df = df.to_frame().reset_index().rename(columns={0: 'count'})
    
    src = df['src'][0:-1].to_numpy()
    x = 0
    for i in src:
        src[x] = int(ipaddress.ip_address(i)) # convert sang decimal
        x = x+1
    df['src'][0:-1] = src
    # print(list(src))
    # for i in df['src'][0:-1]:
    #     df['src'][x] = int(ipaddress.IPv4Address(i)) # convert sang decimal
    #     x = x+1
    # ====================================================
    
    count = df['count'][0:-1]
    bps = []
    for i in range(len(src)):
        bps.append(float(df['bps'][i]))
    df['bps'][0:-1] = bps

    timestamp = df['timestamp'][0:-1].to_numpy()
    print(timestamp)
    x = 0
    for i in range(len(src)):
        timestamp[x] = int(timestamp[i][11:13])*3600 + int(timestamp[i][14:16])*60 + int(timestamp[i][17:19])
        x = x + 1
    df['timestamp'][0:-1] = timestamp                             
    
    df = df.drop(df[df.src == df['src'][len(src)]].index)
    df = df.drop(df[((df.src < 3232301055) & (df.src > 3232235520)) | ((df.src < 2886795263) & (df.src > 2886729728)) | (
        (df.src < 184549375) & (df.src > 167772160))].index)  # | for or, & for and, và ~ cho not
    df = df.reset_index()
    df = df.drop('index', 1)                        # 1 la xoa cot, 0 la xoa hang

    ip_number = df['src'].unique().tolist()
    src = df['src'].to_numpy()
    bps = df['bps'].to_numpy()
    timestamp = df['timestamp'].to_numpy()

    three_dimention_plot(src,timestamp,bps,ip_number)
    # plt.savefig("./figure/" + name + ".png")

    fig, axes = plt.subplots(1,1,figsize=(15, 4))
    three_dimention_surface(src,timestamp,bps,axes,ip_number)
    # plt.savefig("./figure/" + name + "(surface)" + ".png")

    bps.sort()
    a = -1
    nlarget = []
    for i in range(5):
        nlarget.append(bps[a])
        a = a-1
    print("("+name+")"+"5 IP larget:")
    for i in nlarget:
        print(df[df['bps'] == i])
    plt.show()