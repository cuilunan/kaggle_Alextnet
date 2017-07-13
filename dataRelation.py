import numpy as np
import os
import random
import re 
def generTrainData(filename,pictureDir):
	di={}
	with open("label.txt","r") as f:
		for line in f:
			content=line.strip().split()
			key=content[0]
			val=str(content[1])
			di[key]=int(val)
	w2=open("poolTrain.txt","a+")
	data=[]
	with open(filename,"r") as f:
		f.readline()
		for line in f:
			content=line.strip().split(",")
			picName=str(content[0])
			labels=content[1].strip().split()
			w2.write(pictureDir+"/"+picName+".jpg")
			for l in labels:
				# w2.write(pictureDir+"/"+picName+".jpg"+"\t"+str(di.get(l))+"\n")
				w2.write("\t"+str(di.get(l)))
			w2.write("\n")

	w2.close()
def shuffle(filename):
	w=open("transform/train.txt","a+")
	train=[]
	with open(filename,"r") as f:
		for line in f:
			train.append(line)
	random.shuffle(train)
	for line in train:
		w.write(line)
	w.close()

def generLabelsOfVal(valName):
	di1={}
	with open("label.txt","r") as f:
		for line in f:
			content=line.strip().split()
			key=content[0]
			val=str(content[1])
			di1[key]=int(val)
	di2={}
	with open("train_v2.csv","r") as f:
		for line in f:
			content=line.strip().split(",")
			key=content[0]
			val=content[1].strip().split()
			di2[key]=val
	w=open("valLabels.txt","a+")
	with open(valName,"r") as f:
		for line in f:
			content=line.strip().split()
			picName=content[0]
			name=re.findall("train-jpg/(.*).jpg", picName)[0]
			labels=di2[name]
			for label in labels:
				w.write(str(di1[label])+"\t")
			w.write("\n")
	w.close()

def generTestData(pictureDir):
	w=open("test.txt","a+")
	for picName in os.listdir(pictureDir):
		path=os.path.join(pictureDir,picName)
		w.write(str(path)+"\n")
	w.close()

def generResult(filename1,filename2):
	w=open("temp.csv","a+")
	r1=open(filename1,"r")
	r2=open(filename2,"r")
	for line in r1:
		content1=line.strip()
		content2=r2.readline().strip().split()
		name=re.findall("test-jpg/(.*).jpg", content1)[0]
		w.write(name+",")
		for word in content2:
			w.write(word+" ")
		w.write("\n")
	w.close()
def generTestOfTrainData(filename,pictureDir):
	w=open("testOfTrain.txt","a+")
	with open(filename,"r") as f:
		f.readline()
		for line in f:
			content=line.strip().split(",")
			name=content[0]
			picName=os.path.join(pictureDir,name+".jpg")
			w.write(picName+"\n")
	w.close()
def ridOfClass1and3(filename):
	w=open("train2.txt","a+")
	with open(filename,"r") as f:
		for line in f:
			content=line.strip().split()
			label=int(content[1])
			if label==1 or label==3:
				pass
			else:
				w.write(line)
	w.close()






if __name__=="__main__":
	generTrainData("train_v2.csv", "/home/ices/Documents/kaggle/Planet/input/train-jpg")
	# shuffle("/home/cln/hitsz/kaggle/Planet/transform/trainAll.txt")
	# generLabelsOfVal("validation.txt")
	# generTestData("/home/ices/Documents/kaggle/Planet/input/test-jpg")
	# generResult("test.txt", "result.txt")
	# generTestOfTrainData("train_v2.csv","/home/cln/hitsz/kaggle/Planet/train-jpg")
	# ridOfClass1and3("train.txt")