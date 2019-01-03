-----------------------
Similarity Measure Tasks: Readme File
-----------------------

----------
*Author: 
Anik Pait

Open the task1.py,task2.py,task3.py,task4.py,task5.py files with "Notepad++", The exe files are in Code folder from which the notepad++ files can be opened using (Edit with notepad++)

Operating System Requirements: Windows 10, Mac,Ubuntu,Linux

Pre-requisite knowledge on the following would be helpful:
-MongoDB
-Python 
-Similarity Distance measures
-Vectors

Installations Required:

MongoDB: 

version: 4.0.1
The steps for installation are:https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/
Link for download: https://www.mongodb.com/download-center?jmp=nav#compass

Python:

version: 3.7.0
The steps for installation are:https://realpython.com/installing-python/
Link for download: https://www.python.org/downloads/release/python-370/
Install the packages Scipy and Numpy using pip

Notepad++
version:7.5.8
The steps for installation and download :https://notepad-plus-plus.org/download/v7.5.8.html

----------
**Description:

There are 5 tasks which you need to run. To run those tasks, the installations as mentioned is required.
After the completion of MongoDB installation, the localhost(27017) is connected and the GUI to the database can be seen in MOngoDB Compass.The data files were converted into JSON and BSON 
for database compatibility and were retrieved. The text files were converted into JSON and BSON file schema by Mongolb dump. The JSON files contains the metadata for the collection 
whereas BSON file contains the data to be used or retrieved.

To store bson file in mongodb via cmd : >mongorestore -d database_name -c collection_name Path
To store Json file in mongodb via cmd: >mongoimport -d database_name -c collection_name Path

To install the packages:
pip install scipy
pip install numpy

How to convert the files:

Convert the txt file containing user text descriptors data to json format:
    $ bash scripts/parseUserText.sh <path-to-text-descriptor>
    Load text descriptor data for users in the MongoDB:
    $ bash scripts/loadData.sh <file-generated-by-previous-command> <db> <collection>

    Convert the txt file containing images text descriptors data to json format:
    $ bash scripts/parseImageText.sh <path-to-text-descriptor>
    Load text descriptor data for images in the MongoDB:
    $ bash scripts/loadData.sh <file-generated-by-previous-command> <db> <collection>

    Convert the txt file containing location text descriptors data to json format:
    $ bash scripts/parseLocationText.sh <path-to-text-descriptor>
    Load text descriptor data for locations in the MongoDB:
    $ bash scripts/loadData.sh <file-generated-by-previous-command> <db> <collection>

    Load location info to MongoDB
    $ python scripts/mongoInsertLocationInfo.py --xml-file <path-to-topics-xml> \
    --database <db> --collection <collection>

    Load visual descriptor data into MongoDB:
    $ bash scripts/load_VD.sh <path-to-visual-descriptor-data-directory> <db> <collection>


There are 5 tasks suppsoed to be accomplished.
----------

To run the tasks,steps are as follows:

Task 1:

1.Open the command line.
2. Run the python file task1.py 
3. The database should be locally set up.
 Enter the inputs
				User ID: 39052554@N00 
				Enter the model(TF/DF/IDF): DF
				Enter k: 5

4.Sample outputs:
9067738157@N00 has similarity distance based on the DF model:  27.22
929292920@N08 has similarity distance based on the DF model:  30.0
9028829238157@N00 has similarity distance based on the DF model:  33.0
3897478187@N00 has similarity distance based on the DF model:  141.42
Terms 0 for image 9067738157@N00 : ' orlando ' : 0.0
Terms 1 for image 929292920@N08 : ' 2011 ' : 0.0
Terms 2 for image 3897478187@N00 : ' nol ' : 0.0
Terms 0 for image 9067738157@N00 : ' bok ' : 1.0
Terms 1 for image 929292920@N08 : ' garden' : 1.0
Terms 2 for image 3897478187@N00: ' entrance ' : 1.0



Task 2:

1. Open the command lin interface
2. Type python task2.py
3.Enter the inputs

				Image ID:9069963392
				Enter the model(TF/DF/IDF):DF
				Enter k: 4 

4.Sample Output:
9067738157 has similarity distance based on the DF model:  0.0
416345714 has similarity distance based on the DF model:  0.0
4847508172 has similarity distance based on the DF model:  0.0
3897478187 has similarity distance based on the DF model:  1.4142135623730951
Terms 0 for image 9067738157 : ' acropoli ' : 0.0
Terms 1 for image 9067738157 : ' acropoli ' : 0.0
Terms 2 for image 9067738157 : ' acropoli ' : 0.0
Terms 0 for image 416345714 : ' entrance ' : 1.0
Terms 1 for image 416345714 : ' entrance ' : 1.0
Terms 2 for image 416345714 : ' entrance ' : 1.0

Task 3:
-

1. Open the command lin interface
2. Type python task4.py
3.Enter the inputs

				Location ID: 6
				Enter the model(TF/DF/IDF):TF-IDF
				Enter k: 4 

Sample Output:
albert memorial has similarity distance based on the TF-IDF model:  113.24
agra fort has similarity distance based on the TF-IDF model:  112.22
angel of the north has similarity distance based on the TF-IDF model: 100.56
le medelene has similarity distance based on the TF-IDF model:  98.50
Terms 0 for albert memorial : ' 02 ' : 0.0
Terms 1 for agra fort : ' 1450 ' : 0.0
Terms 2 for angel of the north : ' 2006 ' : 0.0
Terms 0 for image 416345714 : ' 02 ' : 1.0
Terms 1 for agra fort : ' ee ' : 1.0
Terms 2 for le medelene: ' 18 ' : 1.0


Task 4:
-

1. Open the command lin interface
2. Type python task5.py
3.Enter the inputs

				Location ID: 4
				Enter the model:CM
				Enter k: 4 

Sample Output:
Enter Location ID 4
Enter the Model (in caps): CM
Enter k value: 2
The given location is similar to [('cabrillo', -0.4470621773557375), ('castillo_de_san_marcos', -0.34177037193694493)]
Image-Image pair for location cabrillo is: 872988816   9847103976 with score -1318.8733718578828
Image-Image pair for location cabrillo is: 872988816   9847103976 with score -1128.529298513303
Image-Image pair for location cabrillo is: 872988816   9847103976 with score -1057.3358498532507
Image-Image pair for location castillo_de_san_marcos is: 9838973373   9847103976 with score -7640.5865213434445
Image-Image pair for location castillo_de_san_marcos is: 9838973373   9847103976 with score -6640.12232940948
Image-Image pair for location castillo_de_san_marcos is: 9838973373   9847103976 with score -1083.1170508123196



Task 5:
-

1. Open the command lin interface
2. Type python task2.py
Enter the inputs

				User ID:9069963392
				Enter the model(TF/DF/IDF):DF
				Enter k: 4 

---------
**References:
I would like to thank Professor K. Candon from Arizona State University for providing me the opportunity to be a part of it.
I would also like to acknowledge my group members for the same.

