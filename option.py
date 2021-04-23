from bps_advanced2_inCome import BI_inCome
from bps_advanced2_outGo import BI_outGo
from bps_income_3d import BI_inCome_3d
from bps_outgo_3d import BI_outGo_3d
import os, sys
path = "/home/son/bps,pps/data/test/"
lists = os.listdir(path)
def option(s, name, j):
	if(s == 1):
		BI_inCome()
	elif (s == 2):
		BI_outGo()
	elif (s == 3):
		BI_inCome_3d(name,j)
	elif (s == 4):
		BI_outGo_3d()

for name in lists:
	option(3, name, j = 0)
"""
s = 1: bps,ip,income
s = 2: bps,ip,outgo
s = 3: bps,ip,income,3d
s = 4: bps,ip,outgo,3d
s = 5: bps,time,income
s = 6: bps,time,outgo
"""
