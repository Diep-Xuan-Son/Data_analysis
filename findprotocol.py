import pandas as pd
import matplotlib.pyplot as plt
# from sklearn.preprocessing import StandardScaler
# from sklearn.cluster import KMeans
import ipaddress
import heapq
import os, sys
path = "D:/data_analyzis/bps,pps/data/test2/"
lists = os.listdir(path)

for name in lists:
    # name = j
    dataset = pd.read_csv(path + name , header=None, delim_whitespace=False)  #+ ".csv": neu co duoi .csv
    dataset = dataset.rename(columns={7: 'proto'})  # vị trí số 6 trong file csv

    ip_times = dataset.pivot_table(index=['proto'], aggfunc='size')
    dataset['proto'].unique().tolist()
    pkt_times = dataset.pivot_table(index=['proto', ], aggfunc='size')
    df = pkt_times.to_frame().reset_index()
    df = df.rename(columns={0: 'count'})
    print(len(ip_times))
    for i in range(len(ip_times)):
        print(df['proto'][i])
    print(df)
    # # for i in range(len(df['src'][0:-1])):
    # #     df['src'][i] = int(ipaddress.ip_address(df['src'][i]))  # convert sang decimal
    # src = df['src'][0:-1]
    # src = src.to_numpy()
    # # src.sort()
    # # print(src)
    # x = 0
    # for i in src:
    #     src[x] = int(ipaddress.ip_address(i)) # convert sang decimal
    #     x = x+1
    # df['src'][0:-1] = src
    # # ====================================================
    # df = pd.DataFrame(df, columns=['src', 'len', 'count', 'bps'])
    # pktlen = df['len'][0:-1]
    # count = df['count'][0:-1]
    # sport_slot = []
    # for i in range(len(src)):
    #     sport_slot.append(float(count[i])*float(pktlen[i])/600)
    # df['bps'][0:-1] = sport_slot                                    # thêm 1 cột bps
    # df = df.drop(df[df.src == df['src'][len(src)]].index)
    # df = df.drop(df[((df.src < 3232301055) & (df.src > 3232235520)) | ((df.src < 2886795263) & (df.src > 2886729728)) | (
    #     (df.src < 184549375) & (df.src > 167772160))].index)  # | for or, & for and, và ~ cho not
    # df = df.reset_index()
    # df = df.drop('index', 1)                        # 1 la xoa cot, 0 la xoa hang

    # plt.subplots()
    # plt.scatter(df['src'], df['bps'])
    # # plt.show()
    # # plt.scatter(dataset_scaled['ip'], dataset_scaled['count'], c=dataset_scaled['cluster name'])
    # plt.xlabel("IP")
    # plt.ylabel("Bytes/s")
    # plt.title(name + " " + str(len(ip_times)) + " IP")
    # # print(df[df['cluster name']==1])
    # nlarget = heapq.nlargest(5, df['bps'])
    # print("("+name+")"+"5 IP larget:")
    # for i in range(len(nlarget)):
    #     print(df[df['bps'] == nlarget[i]])
    # # plt.savefig("./figure/" + name + ".png")
    # plt.show()


    # # mal_ip=[]
    # # mal_ip[:]=str(df[df['cluster name']==1].iloc[:]['ip'])
    # # with open("D:/data_analyzis/malicious_ip.txt","w") as f:
    # #     for i in mal_ip:
    # #       # L=i+"\n"
    # #       f.writelines(i)
    # # print('completed!!')
