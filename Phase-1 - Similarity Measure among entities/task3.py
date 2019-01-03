#Task 3 : Finding Similar k users based on Location and getting top 3 terms with Similarity Scores between the locations
import json
import numpy as np
import pymongo
import sys
from array import array
from pymongo import MongoClient
#Establishing the NoSQL Database Connection:
client=MongoClient()
db=client.MWDB_P1
locationid=db.location_info																							#Collection of location in the database
location=db.TD_locations																							#location name is mapped to TD_locations collection
similarity_distance=[]
common_location=[]
query_location_f_vector=[]
#Function for calculating the Similarity distance (Euclidean distance between the terms used by the query user and the other location)
def term_calculation(model):
	final_location={}																								#Storing ALL the common location as 'key' and the term distance between the terms in form of a list as 'value'
	final_location_1={}   																	#Storing the K common location out of ALL the location as 'key' and the term distance between the terms with different location in form of a list as 'value'
	for i in common_location:
		other_location_f_vector=[]
		diff=[]
		other_location=[]
		for j in query_location_terms:																			     #Parsing through the location terms used
			other_location=location.find_one({"LOCATION_ID":i},{"TEXT_DESC":{"$elemMatch":{"TERM":j}}})
			if "TEXT_DESC" in other_location: 
				other_location_f_vector.append(other_location["TEXT_DESC"][0][model]) 								 #Fetching out the other user TF/DF/IDF as required			
			else:
				other_location_f_vector.append(0) 		
		diff=np.absolute(np.subtract(query_location_f_vector,other_location_f_vector))								#Calculating the Euclidean measure
		final_location[i]=list(diff)
		similarity_distance.append(np.sqrt(np.sum(np.square(diff))))	
	for i in range(0,k):
		for j in similarity_distance:
			minimum=min(similarity_distance)
		final_location_1[common_location[similarity_distance.index(minimum)]]=final_location[common_location[similarity_distance.index(minimum)]]
		print(common_location[similarity_distance.index(minimum)],"has similarity distance based on the",model,"model: ",similarity_distance.pop(similarity_distance.index(minimum)))
	for r in final_location_1:	
		for i in range(0,3):
			mini=min(final_location_1[r])
			print("Terms",i,"for user",r,":","'",query_location_terms[final_location_1[r].index(mini)],"'",":",mini)
			final_location_1[r].pop(final_location_1[r].index(mini))
if __name__ == '__main__':
#inputs from the end user
	print ("Hi! Please enter the following:\n")
	id=int(input("Enter location ID: "))
	model=input("Enter the Model(TF/DF/TF_IDF): ")
	k=int(input("Enter k value: "))
	location_name=locationid.distinct("title",{"number":id})
	location_name=location_name[0]
	location_name=location_name.replace('_'," ")
	query_location_terms=location.distinct("TEXT_DESC.TERM",{"LOCATION_ID":location_name})					#Fetching out the location name from the database
	g=[]
for v in query_location_terms:
	cu=location.distinct("LOCATION_ID",{"TEXT_DESC.TERM":v})												#Common location terms used by different locations
	for uid in cu:
		g.append(uid)
common_location=set(g)
common_location=list(common_location)
common_location.pop(common_location.index(location_name))
for j in query_location_terms:			
	query_location=location.find_one({"LOCATION_ID":location_name},{"TEXT_DESC":{"$elemMatch":{"TERM":j}}})		#Fetching out query details based on TF/IDF/DF
	for tf in query_location["TEXT_DESC"]:
		query_location_f_vector.append(tf[model])
if model=="TF" or model=="DF" or model=="TF_IDF":
	term_calculation(model)
sys.exit()


	
