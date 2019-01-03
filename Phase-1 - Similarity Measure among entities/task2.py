#Task 2 : Finding Similar k images based on image ID and getting top 3 terms with Similarity Scores between the images
import json
import numpy as np
import pymongo
import sys
from array import array
from pymongo import MongoClient
#Establishing the NoSQL Database Connection:
client=MongoClient()
db=client.MWDB_P1
image=db.perimage_data																								#Collection to the database (image collection)
similarity_distance=[]
common_image=[]
query_image_f_vector=[]
def term_calculation(model):
	final_image={}
	final_image_1={}
	for i in common_image:
		other_image_f_vector=[]
		diff=[]
		other_image=[]
		for j in query_image_terms:		
			other_image=image.find_one({"IMAGE_ID":i},{"TEXT_DESC":{"$elemMatch":{"TERM":j}}})						#Fetching out the images with the same term from NoSQL DB
			if "TEXT_DESC" in other_image: 
				other_image_f_vector.append(other_image["TEXT_DESC"][0][model]) 
			else:
				other_image_f_vector.append(0) 		
		diff=np.absolute(np.subtract(query_image_f_vector,other_image_f_vector))								   # Calculating the Euclidean distance
		final_image[i]=list(diff)																					# Storing the final list of ALL images
		similarity_distance.append(np.sqrt(np.sum(np.square(diff))))	
	for i in range(0,k):
		for j in similarity_distance:
			minimum=min(similarity_distance)
		final_image_1[common_image[similarity_distance.index(minimum)]]=final_image[common_image[similarity_distance.index(minimum)]]			#Filtering the ALL images into final ones with common image terms
		print(common_image[similarity_distance.index(minimum)],"has similarity distance based on the",model,"model: ",similarity_distance.pop(similarity_distance.index(minimum)))
	for r in final_image_1:
		for i in range(0,3):
			mini=min(final_image_1[r])																					#Top 3 terms contributing to the image terms
			print("Terms",i,"for image",r,":","'",query_image_terms[final_image_1[r].index(mini)],"'",":",mini)
			final_image_1[r].pop(final_image_1[r].index(mini))
if __name__ == '__main__':
#Inputs from the end user
	print ("Hi! Please enter the following:\n")
	id=input("Enter Image ID: ")
	model=input("Enter the Model(TF/DF/TF_IDF): ")
	k=int(input("Enter k value: "))
	query_image_terms=image.distinct("TEXT_DESC.TERM",{"IMAGE_ID":id})
	g=[]
for v in query_image_terms:
	cu=image.distinct("IMAGE_ID",{"TEXT_DESC.TERM":v})														  #Fetching out the image terms based on the image ID given
	for uid in cu:
		g.append(uid)															
common_image=set(g)
common_image=list(common_image)
common_image.remove(id)
for j in query_image_terms:			
	query_image=image.find_one({"IMAGE_ID":id},{"TEXT_DESC":{"$elemMatch":{"TERM":j}}})							#Fetching out query image terms from the database based on match
	for tf in query_image["TEXT_DESC"]:
		query_image_f_vector.append(tf[model])
if model=="TF" or model=="DF" or model=="TF_IDF":
	term_calculation(model)																						#Calling the calculation function
sys.exit()
