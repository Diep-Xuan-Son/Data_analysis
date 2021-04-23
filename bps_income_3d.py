import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md
import numpy as np
from mpl_toolkits.mplot3d import Axes3D 
# from sklearn.preprocessing import StandardScaler
# from sklearn.cluster import KMeans
import ipaddress
import heapq
import os, sys
from datetime import datetime
path = "/home/son/bps,pps/data/test/"
lists = os.listdir(path)

def three_dimention_plot(a,b,c,ip_number):
    # fig = plt.figure()
    # ax1 = fig.add_subplot(111, projection='3d')
    ax1.scatter(a, b, c, s=10, c=None, depthshade=True)
    # ax1.plot3D(a, b, c, c=None)
    ax1.set_xlabel('IP')
    ax1.set_ylabel('Times')
    ax1.set_zlabel('Bytes/s')
    ax1.set_title(name + " " + str(len(ip_number)) + " IP")

def three_dimention_surface(a,b,c,axes1,axes2,axes3,ip_number):
    axes1.scatter(a, b, s = 10)  # Matplotlib
    # axes1.plot(a, b)
    axes1.set_xlabel("IP")
    axes1.set_ylabel("Times")
    axes1.set_title(name + " " + str(len(ip_number)) + " IP")

    axes2.scatter(a, c, s = 10)  # Matplotlib
    # axes2.plot(a, c)
    axes2.set_xlabel("IP")
    axes2.set_ylabel("Bytes/s")
    axes2.set_title(name + " " + str(len(ip_number)) + " IP")

    axes3.xaxis.set_major_formatter(md.DateFormatter('%d/%m/%Y \n %H:%M:%S'))
    axes3.scatter(b, c, s = 10)  # Matplotlib
    # axes3.plot(b, c, scaley = True, scalex = True)
    axes3.set_xlabel("Times")
    axes3.set_ylabel("Bytes/s")
    axes3.set_title(name + " " + str(len(ip_number)) + " IP")


j = 0
for name in lists:
    # def BI_inCome_3d(name, j):
    # data = pd.read_csv(path + name , header=None, delim_whitespace=False)
    # numpy_data = data.to_numpy()
    # transpose_data = numpy_data.T
    # src = list(transpose_data[1][1:len(transpose_data[1])])
    # timestamp = list(transpose_data[6][1:len(transpose_data[6])])
    # bps = list(transpose_data[20][1:len(transpose_data[20])])

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
    # ====================================================
    
    count = df['count'][0:-1]
    bps = []
    for i in range(len(src)):
        bps.append(float(df['bps'][i]))
    df['bps'][0:-1] = bps

    timestamp = df['timestamp'][0:-1].to_numpy()
    x = 0
    for i in range(len(src)):
        # timestamp[x] = time.mktime(dt.datetime.strptime(timestamp[i][0:10], "%d/%m/%Y").timetuple()) + int(timestamp[i][11:13])*3600 + int(timestamp[i][14:16])*60 + int(timestamp[i][17:19])
        timestamp[x] = md.date2num(datetime.strptime(timestamp[i][0:19], '%d/%m/%Y %H:%M:%S'))
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

    # if(j == 0):
    #     fig = plt.figure()
    #     ax1 = fig.add_subplot(111, projection='3d')
    # three_dimention_plot(src,timestamp,bps,ip_number)
    # plt.savefig("./figure/" + name + ".png")

    if(j == 0):
        fig, axes = plt.subplots(1,3,figsize=(15, 4))
        plt.subplots_adjust(bottom=0.2)
        plt.xticks( rotation=30 )
    three_dimention_surface(src,timestamp,bps,axes[0],axes[1],axes[2],ip_number)
    # plt.savefig("./figure/" + name + "(surface)" + ".png")

    if(j > 4):              #ve 6 hinh lien tiep
        bps.sort()
        a = -1
        nlarget = []
        if not bps:
            print("không có dest ip")
        if not bps.any():
            for i in range(5):
                nlarget.append(bps[a])
                a = a-1
            print("("+name+")"+"5 IP larget:")
            for i in nlarget:
                print(df[df['bps'] == i])
        # plt.show()
        plt.savefig("./figure/" + name + "(surface)" + ".png")
        j = 0 
    else:
        j = j + 1 