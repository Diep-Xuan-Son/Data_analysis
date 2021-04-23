import pandas as pd
import matplotlib.pyplot as plt
# from sklearn.preprocessing import StandardScaler
# from sklearn.cluster import KMeans
import ipaddress
import heapq
import os, sys
path = "/home/son/bps,pps/data/test2/"
lists = os.listdir(path)

for name in lists:
    def BI_outGo():
        # name = "inCom" + str(j) + "_0000" + str(k)
        dataset = pd.read_csv(path + name , header=None, delim_whitespace=False)  #+ ".csv": neu co duoi .csv
        dataset = dataset.rename(columns={1: 'dst'})
        dataset = dataset.rename(columns={6: 'len'})  # vị trí số 6 trong file csv

        # ip_times = dataset.pivot_table(index=['dst'], aggfunc='size')
        dataset['dst'].unique().tolist()
        pkt_times = dataset.pivot_table(index=['dst', 'len', ], aggfunc='size')
        df = pkt_times.to_frame().reset_index()
        df = df.rename(columns={0: 'count'})
        
        dst = df['dst'][0:-1]
        dst = dst.to_numpy()
        x = 0
        for i in dst:
            dst[x] = int(ipaddress.ip_address(i)) # convert sang decimal
            x = x+1
        df['dst'][0:-1] = dst

        # =======================
        df = pd.DataFrame(df, columns=['dst', 'len', 'count', 'bps'])
        dst = df['dst'][0:-1]
        pktlen = df['len'][0:-1]
        count = df['count'][0:-1]
        sport_slot = []
        for i in range(len(dst)):
            sport_slot.append(float(count[i])*float(pktlen[i])/600)
        df['bps'][0:-1] = sport_slot									# thêm 1 cột bps
        
        df = df.drop(df[df.dst == df['dst'][len(dst)]].index)
        df = df.drop(df[((df.dst < 3232301055) & (df.dst > 3232235520)) | ((df.dst < 2886795263) & (df.dst > 2886729728)) | (
            (df.dst < 184549375) & (df.dst > 167772160))].index)  # | for or, & for and, và ~ cho not
        df = df.reset_index()
        df = df.drop('index', 1)						# 1 la xoa cot, 0 la xoa hang

        # print(df)
        # plt.scatter(dst, pktlen)
        # plt.xlabel('dst')
        # plt.ylabel('len')
        # plt.show()

        # ======================
        # print(df[0:-1])
        # sc = StandardScaler()
        # data_scaled = sc.fit_transform(df[0:-1])				#chuẩn hóa dữ liệu
        # # print(data_scaled)

        # #=====================
        # model = KMeans(n_clusters=2)
        # model.fit(data_scaled)
        # pred  = model.fit_predict(data_scaled)
        # # print(pred)
        # # dataset_scaled = pd.DataFrame(data_scaled, columns=['ip', 'len','count','bps'])
        # # # print(data_scaled)
        # # dataset_scaled['cluster name'] = pred
        # # print(dataset_scaled['cluster name'])
        # print(pred)
        # df = pd.DataFrame(df, columns=['ip','len','count','bps','cluster name'])
        # # df.insert(4,'cluster name'[0:-1], pred)
        # df['cluster name'][0:-1] = pred
        # # print(df)

        # x=0
        # for i in df['ip']:
        #   df['ip'][x]=str(ipaddress.IPv4Address(i))
        #   x=x+1

        ip_numbers = df['dst'].unique().tolist()
        dst = df['dst'].to_numpy()
        bps = df['bps'].to_numpy()

        # plt.scatter(df['ip'][0:-1],df['bps'][0:-1], c=df['cluster name'][0:-1])
        plt.scatter(dst, bps)
        # plt.show()
        # plt.scatter(dataset_scaled['ip'], dataset_scaled['count'], c=dataset_scaled['cluster name'])
        plt.xlabel("IP")
        plt.ylabel("Bytes/s")
        plt.title(name + " " + str(len(ip_numbers)) + " IP")
        # print(df[df['cluster name']==1])
        nlarget = heapq.nlargest(5, bps)
        print("5 IP larget:")
        for i in range(len(nlarget)):
            print(df[df['bps'] == nlarget[i]])
        # plt.savefig("./figure/" + name + ".png")
        plt.show()


        # mal_ip=[]
        # mal_ip[:]=str(df[df['cluster name']==1].iloc[:]['ip'])
        # with open("D:/data_analyzis/malicious_ip.txt","w") as f:
        #     for i in mal_ip:
        # 	    # L=i+"\n"
        # 	    f.writelines(i)
        # print('completed!!')
