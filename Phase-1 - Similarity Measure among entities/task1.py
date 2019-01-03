#Task 1 : Finding Similar k users based on User ID and getting top 3 terms with Similarity Scores between the users

#Importing the necessary libraries:
import json
import numpy as np                     
import pymongo
import sys
import sklearn.decomposition as PCA
from array import array
from pymongo import MongoClient

#Establishing the NoSQL Database Connection:
client=MongoClient()
db=client.MWDB_P1    																	#Connection with Database MWDB_P1
user=db.peruser_data																	#Collection peruser_data in the NoSQL Database
similarity_distance=[]
common_users=[]
query_user_f_vector=[]

#Function for calculating the Similarity distance (Euclidean distance between the terms used by the query user and the other users)
def term_calculation(model):
	final_users={}     																	#Storing ALL the common users as 'key' and the term distance between the terms in form of a list as 'value'
	final_users_1={}   																	#Storing the K common users out of ALL the users as 'key' and the term distance between the terms with different users in form of a list as 'value'
	for i in common_users:
		other_user_f_vector=[]
		diff=[]
		other_user=[]
		for j in query_user_terms:		
			other_user=user.find_one({"USER_ID":i},{"TEXT_DESC":{"$elemMatch":{"TERM":j}}}) #Extracting the users whose terms which they use match the terms used by the Query user
			if "TEXT_DESC" in other_user: 
				other_user_f_vector.append(other_user["TEXT_DESC"][0][model]) 			 #other_user_f_vector Captures TF/DF/TF_IDF for OTHER users who share the common term with Query user
			else:
				other_user_f_vector.append(0) 		                                     #If the users dont use the term used by query users, its replaced by 0
		diff=np.absolute(np.subtract(query_user_f_vector,other_user_f_vector))           #Difference between Query TF/DF/TF_IDF vector and the other user TF/DF/TF_IDF vector
		final_users[i]=list(diff)														 #Storing the User ID's and their differences between the terms for further computation
		similarity_distance.append(np.sqrt(np.sum(np.square(diff))))					 #Calculating the Euclidean Distance measure
	#Fetching out Top K Similar Users:
	for i in range(0,k):
		for j in similarity_distance:
			minimum=min(similarity_distance)	 										  #Taking out the minimum of the similarity_distance and popping it out of the list to calculate next two minimum distances
#Storing final_users to final_users_1 to fetch out the top 3 terms in each measure
		final_users_1[common_users[similarity_distance.index(minimum)]]=final_users[common_users[similarity_distance.index(minimum)]]
		print(common_users[similarity_distance.index(minimum)],"has similarity distance based on the",model,"model: ",similarity_distance.pop(similarity_distance.index(minimum)))
#Fetching out the Top 3 terms for each match of users along with their similarity contribution
	for r in final_users_1:
		for i in range(0,3):
			mini=min(final_users_1[r])
			print("Terms",i,"for user",r,":","'",query_user_terms[final_users_1[r].index(mini)],"'",":",mini)
			final_users_1[r].pop(final_users_1[r].index(mini))
if __name__ == '__main__':
#Inputs from the end user
	print ("Hi! Please enter the following:\n")                                                                     
	id=input("Enter the corresponding ID: ")
'''	model=input("Enter the Model(TF/DF/TF_IDF)\n(Please enter from the three options only): ")
	k=int(input("Enter k value: "))
	query_user_terms=user.distinct("TEXT_DESC.TERM",{"USER_ID":id})	
	g=[]
for v in query_user_terms:
	cu=user.distinct("USER_ID",{"TEXT_DESC.TERM":v})
	for uid in cu:																		#Parsing through the Common users id and mapping them with the common terms used by the Query users and Other users
		g.append(uid)
common_users=set(g)
common_users=list(common_users)     													#Presenting the list of Common users(based on the fact that they used the terms common with the Query user evn if it is at least one term
common_users.remove(id)       
'''       													#Removing the Query user data to avoid duplicate user
for j in query_user_terms:			
	query_user=user.find_one({"USER_ID":id},{"TEXT_DESC":{"$elemMatch":{"TERM":j}}}) 
#Fetching out the TF/DF/TF_IDF details of the user from NoSQL database and the input given
	for tf in query_user["TEXT_DESC"]:
		query_user_f_vector.append(tf[model])											#query_user_f_vector captures the TF/DF/TF_IDF ONLY for the Query User (based on the input model)
if model=="TF" or model=="DF" or model=="TF_IDF":
	term_calculation(model)																#Calling the Calculation function
sys.exit()


	
