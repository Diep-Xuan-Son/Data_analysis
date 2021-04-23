import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import ipaddress
import heapq

# name='OutGoing367_Pktlen.csv'
name="/content/drive/My Drive/Out_going_Duong/CsvData/inCom368_00001_20200925122310.csv"
dataset = pd.read_csv(name,header=None,delim_whitespace=False)

# dataset.head(1000)


dataset=dataset.rename(columns = {1:'dst'})
dataset=dataset.rename(columns = {6:'len'})				#vị trí số 6 trong file csv


# dataset.head(40)


ip_times=dataset.pivot_table(index=['dst'],aggfunc='size')
dataset['dst'].unique().tolist()
pkt_times=dataset.pivot_table(index=['dst','len',],aggfunc='size')
df = pkt_times.to_frame().reset_index()
df=df.rename(columns = {0:'count'})		
# print(df['dst'][0:-2])

x=0
for i in df['dst'][0:-1]:
     df['dst'][x]=int(ipaddress.IPv4Address(i))		#convert sang decimal
     x=x+1
print(df)

#=======================
df = pd.DataFrame(df, columns=['dst','len','count','bps'])
src=df['dst'][0:-1]
pktlen=df['len'][0:-1]
count=df['count'][0:-1]
sport_slot=[]
print(df.dst)
for i in range(len(dst)):
    sport_slot.append(float(count[i])*float(pktlen[i])/600)
df['bps'][0:-1] = sport_slot									# thêm 1 cột bps
df = df.drop(df[df.dst == df['dst'][len(dst)]].index)
print(df)
df = df.drop(df[((df.dst < 3232301055) & (df.dst > 3232235520)) | ((df.dst < 2886795263) & (df.dst > 2886729728)) | ((df.dst < 184549375) & (df.dst > 167772160))].index)	# | for or, & for and, và ~ cho not
df = df.reset_index()
df = df.drop('index', 1)						# 1 la xoa cot, 0 la xoa hang	
# print(df)
# plt.scatter(dst, pktlen)
# plt.xlabel('dst')
# plt.ylabel('len')
# plt.show()

#======================
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
print(df)

# plt.scatter(df['ip'][0:-1],df['bps'][0:-1], c=df['cluster name'][0:-1])
plt.scatter(df['dst'],df['bps'])
# plt.show()
# plt.scatter(dataset_scaled['ip'], dataset_scaled['count'], c=dataset_scaled['cluster name'])
plt.xlabel("IP")
plt.ylabel("Bytes/s")
plt.title(name + " " + str(len(ip_times)) + " IP")
# print(df[df['cluster name']==1])
nlarget = heapq.nlargest(5, df['bps'])
print("5 IP larget:")
for i in range(len(nlarget)):
    print(df[df['bps'] == nlarget[i]])
plt.show()

# mal_ip=[]
# mal_ip[:]=str(df[df['cluster name']==1].iloc[:]['ip'])
# with open("D:/data_analyzis/malicious_ip.txt","w") as f:
#     for i in mal_ip:
# 	    # L=i+"\n"
# 	    f.writelines(i)
# print('completed!!')