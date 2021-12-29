class ch:
	def __init__(self):
		self.path=str
		self.string=str

import pandas as pd

def openfile(path):
	f = open(path,"r",encoding="utf8")
	for lines in f:
    		files = f.read().splitlines()
	icd9s=[]
	for elm in files:
   	 	icd9s.append(elm.split("\t"))
	df = pd.DataFrame(icd9s, columns=["icd9","chinese"]) 
	return df
	
def search_ch(string):
	result = openfile("./data/icd9.txt")
	return print("{}:{}".format(string,result[result["icd9"]==string]["chinese"].iloc[0]))

#if __name__ == "__main__":
#	print("{}:{}".format(string, search_ch(string)))