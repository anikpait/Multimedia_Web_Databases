#Task 4:  To find k similar locations based on location ID and return the image image pairs on each match

import json
import numpy as np
import pymongo
import sys
from array import array
from scipy import spatial
from pymongo import MongoClient
client=MongoClient()
db=client.MWDB_P1
vd=db.visual_descriptors  																						# Database connection established
locationid=db.location_info
final_location=[]
sum_len=0
mul=[]
cos_av=0
cos_location={}
#input from the end user
print ("Hi! Please enter the following:\n")
id=int(input("Enter Location ID "))
model=input("Enter the Model (in caps): ")
k=int(input("Enter k value: "))
location_name=locationid.distinct("title",{"number":id})
location_name=location_name[0]
query_location_images=vd.find_one({"location":location_name})											#query_location_images stores the details of the location (fetching from database)
query_location=dict()			
query_location[location_name]=query_location_images[model]
other_location_images=vd.find()																			#Two Dictionaries: query user (location to score mapping) and other user with the same mapping
other_location=dict()
for i in other_location_images:
	other_location[i['location']]=i[model]																#Extracting location details according to the visual model
other_location.pop(location_name)
for i in other_location:
	for j in other_location[i]:
		for loc in query_location[location_name]:
			cos=1-spatial.distance.cosine(loc["scores"],j["scores"])								    #Calculating the Cosine similarity distance between image and image pairs
	cos_location[i]=np.mean(cos)																		# Taking the mean and storing it to Cos_location to create a location and mean image pair for the given model
top=sorted(cos_location.items(),key=lambda x:-x[1],reverse=True)[:k]									# Top k locations based on similarity, sorted the array and took out lambda as key
print("The given location is similar to",top)
for i in top:
	for j in other_location[i[0]]:
		for loc in query_location[location_name]:
			mul.append(np.dot(j["scores"],loc["scores"]))												# to get the image image pair calculations of scores,storing it in mul list
	for a in range(0,3):
		m=min(mul)
		print("Image-Image pair for location",i[0],"is:",j["image"]," ",loc["image"],"with score",m)	#Displaying the image image pairs
		mul.pop(mul.index(m))
			
