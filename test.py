import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import ipaddress

name='out368_total.csv'
# name='/content/drive/Shared drives/Dataset_trash_storage/Hust Data/file_368/outGoinginCom368_00004_20200925122940.csv'
dataset = pd.read_csv('./data/' + name,header=None,delim_whitespace=False)

# dataset.head(1000)


dataset=dataset.rename(columns = {0:'ip'})
dataset=dataset.rename(columns = {1:'len'})


# dataset.head(40)


ip_times=dataset.pivot_table(index=['ip'],aggfunc='size')
dataset['ip'].unique().tolist()
pkt_times=dataset.pivot_table(index=['ip','len',],aggfunc='size')
df = pkt_times.to_frame().reset_index()
df=df.rename(columns = {0:'count'})		
# print(df)

#=======================
ip=df['ip']
pktlen=df['len']
count=df['count']
sport_slot=[]
for i in range(len(ip)):
    sport_slot.append(count[i]*pktlen[i]/300)
df['bps'] = sport_slot									# thêm 1 cột bps
# print(df)
# plt.scatter(ip, pktlen)
# plt.xlabel('ip')
# plt.ylabel('len')
# plt.show()

#======================
sc = StandardScaler()
data_scaled = sc.fit_transform(df)				#chuẩn hóa dữ liệu
# print(data_scaled)

#=====================
model = KMeans(n_clusters=2)
model.fit(data_scaled)
pred  = model.fit_predict(data_scaled)	
# print(pred)
# dataset_scaled = pd.DataFrame(data_scaled, columns=['ip', 'len','count','bps'])
# # print(data_scaled)
# dataset_scaled['cluster name'] = pred
# print(dataset_scaled['cluster name'])
df['cluster name'] = pred
# print(df)

# x=0
# for i in df['ip']:
#   df['ip'][x]=str(ipaddress.IPv4Address(i))
#   x=x+1
# print(df)

plt.scatter(df['ip'],df['bps'], c=df['cluster name'])
# plt.show()
# plt.scatter(dataset_scaled['ip'], dataset_scaled['count'], c=dataset_scaled['cluster name'])
plt.xlabel("IP")
plt.ylabel("Bytes/s")
plt.title(name + " " + str(len(df['ip'])) + " IP")
print(df[df['cluster name']==1])
print(df[df['bps'] == df['bps'].max()])
# print(df['bps'].max())
plt.show()

# mal_ip=[]
# mal_ip[:]=str(df[df['cluster name']==1].iloc[:]['ip'])
# with open("D:/data_analyzis/malicious_ip.txt","w") as f:
#     for i in mal_ip:
# 	    # L=i+"\n"
# 	    f.writelines(i)
# print('completed!!')