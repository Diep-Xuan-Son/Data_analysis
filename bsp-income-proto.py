import pandas as pd
import matplotlib.pyplot as plt
# from sklearn.preprocessing import StandardScaler
# from sklearn.cluster import KMeans
import ipaddress
import heapq
import os, sys
path = "D:/data_analyzis/bps,pps/data/test2/"
lists = os.listdir(path)

print("Running.......")
for name in lists:
    # name = j
    dataset = pd.read_csv(path + name , header=None, delim_whitespace=False)  #+ ".csv": neu co duoi .csv
    dataset = dataset.rename(columns={0: 'src'})
    dataset = dataset.rename(columns={6: 'len'})  # vị trí số 6 trong file csv
    dataset = dataset.rename(columns={7: 'proto'})

    dataset['src'].unique().tolist()
    df = dataset.pivot_table(index=['src', 'len', 'proto'], aggfunc='size')
    df = df.to_frame().reset_index().rename(columns={0: 'count'})

    src = df['src'][0:-1].to_numpy()
    x = 0
    for i in src:
        src[x] = int(ipaddress.ip_address(i)) # convert sang decimal
        x = x+1
    df['src'][0:-1] = src
    # ====================================================
    df = pd.DataFrame(df, columns=['src', 'len', 'proto', 'count', 'bps'])
    pktlen = df['len'][0:-1]
    count = df['count'][0:-1]
    proto = df['proto'][0:-1]
    sport_slot = []
    for i in range(len(src)):
        sport_slot.append(float(count[i])*float(pktlen[i])/600)
    df['bps'][0:-1] = sport_slot                                    # thêm 1 cột bps
    df = df.drop(df[df.src == df['src'][len(src)]].index)
    df = df.drop(df[((df.src < 3232301055) & (df.src > 3232235520)) | ((df.src < 2886795263) & (df.src > 2886729728)) | (
        (df.src < 184549375) & (df.src > 167772160))].index)  # | for or, & for and, và ~ cho not
    df = df.reset_index()
    df = df.drop('index', 1)                        # 1 la xoa cot, 0 la xoa hang

    ip_numbers = df['src'].unique().tolist()
    src = df['src'].to_numpy()
    bps = df['bps'].to_numpy()
    proto = df['proto'].to_numpy()

    df1 = df[df['proto'] == "1"]
    src1 = df1['src'].to_numpy()
    bps1 = df1['bps'].to_numpy()
    proto1 = df1['proto'].to_numpy()
    ip_numbers1 = df1['src'].unique().tolist()

    df6 = df[df['proto'] == "6"]
    src6 = df6['src'].to_numpy()
    bps6 = df6['bps'].to_numpy()
    proto6 = df6['proto'].to_numpy()
    ip_numbers6 = df6['src'].unique().tolist()

    df17 = df[df['proto'] == "17"]
    src17 = df17['src'].to_numpy()
    bps17 = df17['bps'].to_numpy()
    proto17 = df17['proto'].to_numpy()
    ip_numbers17 = df17['src'].unique().tolist()

    print("******")
    print(df1)
    print(df6)
    print(df17)

    fig,axes = plt.subplots(1,3,figsize=(12, 6))
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.3, hspace=None)

    axes[0].scatter(src1, bps1)
    axes[0].set_xlabel("IP")
    axes[0].set_ylabel("Bytes/s")
    axes[0].set_title(name + " " + str(len(ip_numbers1)) + " IP-ICMP")

    axes[1].scatter(src6, bps6)
    axes[1].set_xlabel("IP")
    axes[1].set_ylabel("Bytes/s")
    axes[1].set_title(name + " " + str(len(ip_numbers6)) + " IP-TCP")

    axes[2].scatter(src17, bps17)
    axes[2].set_xlabel("IP")
    axes[2].set_ylabel("Bytes/s")
    axes[2].set_title(name + " " + str(len(ip_numbers17)) + " IP-UDP")

    nlarget = heapq.nlargest(5, bps)
    print("("+name+")"+"5 IP larget:")
    for i in range(len(nlarget)):
        print(df[df['bps'] == nlarget[i]])
    # plt.savefig("./figure/" + name + ".png")
    plt.show()


    # mal_ip=[]
    # mal_ip[:]=str(df[df['cluster name']==1].iloc[:]['ip'])
    # with open("D:/data_analyzis/malicious_ip.txt","w") as f:
    #     for i in mal_ip:
    #       # L=i+"\n"
    #       f.writelines(i)
    # print('completed!!')

print("End")