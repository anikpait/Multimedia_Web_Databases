#Task 5:  To find k similar locations based on location ID and return the contributions from each of the 10 models
import json
import numpy as np
import pymongo
import sys
from array import array
from scipy import spatial
from pymongo import MongoClient
client=MongoClient()
db=client.MWDB_P1
vd=db.visual_descriptors																			#connection with the visual descriptor collection in the database
locationid=db.location_info
final_location=[]
sim={}
sum_len=0
cos_av=0
n=[]
locate={}
cos_location=[]
print ("Hi! Please enter the following:\n")
id=int(input("Enter Location ID "))
k=int(input("Enter k value: "))
model=['CM','CN','CM3x3','CN3x3','CSD','GLRLM','GLRLM3x3','HOG','LBP','LBP3x3']					#Initializing the 10 visual models to pass through 
location_name=locationid.distinct("title",{"number":id})
location_name=location_name[0]
query_location_images=vd.find_one({"location":location_name})
query_location=dict()
for i in model:
	query_location[location_name]=query_location_images[i]											#Creating a dictionary for query location mapping location to scores
other_location_images=vd.find()
other_location=dict()
for i in other_location_images:
	for j in model:
		other_location[i['location']]=i[j]															#Creating a dictionary for every location including visual models 
other_location.pop(location_name)
for i in other_location:
	for m in model:
		for j in other_location[i]:
			for loc in query_location[location_name]:
				cos=np.sqrt(np.sum(np.square(np.subtract(loc["scores"],j["scores"]))))				#Calculating the Euclidean distance beteween the image pairs and taking the mean
		cos_location.append(np.mean(cos))															# Storing the mean values for models
	locate[i]=np.mean(cos)
	sim[i]=(np.sum(cos_location)/3)
top=sorted(sim.items(),key=lambda x:-x[1],reverse=True)[:k]									# Top k locations based on similarity, sorted the array and took out lambda as key
print("The given location is similar to",top)
for r in top:																				#Storing the keys of the top k terms as need to retrieve the 10 Visual model contribution
	n.append(r[0])

for p in n:
	cos_location=[]																					#To store the mean values of each model 
	for m in model:
		for j in other_location[p]:
			for loc in query_location[location_name]:
				cos=np.sqrt(np.sum(np.square(np.subtract(loc["scores"],j["scores"]))))				#Calculating the Euclidean distance beteween the image pairs and taking the mean
		cos_location.append(np.mean(cos))	
																									# Storing the mean values for models
		print("Similar Location",p,"has model",m,"=",cos_location[0])								#Printing the Contribution from each of the model towards similarity


