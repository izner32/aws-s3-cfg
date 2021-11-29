# Import necessary libraries
import boto3 # access aws services
import pandas as pd # creating dataframes
import configparser # grabbing values of parameters for aws

# for env 
import os 
from dotenv import load_dotenv 
load_dotenv() 

# Grab values inside the config file 
config = configparser.ConfigParser() 
config.read_file(open('aws-s3.cfg')) 

KEY = os.getenv('AWS_KEY')
SECRET = os.getenv('AWS_SECRET')

# Create a dataframe out of it for visualization purposes
pd.DataFrame({
    "Parameter": ["KEY", "SECRET"],
    "Value": [KEY,SECRET]
    }
)

# Connect to S3
s3 = boto3.resource(
   's3',
   region_name="us-west-2",
   aws_access_key_id=KEY,
   aws_secret_access_key=SECRET
)

# Extract from source 
data = ["this","is","a","sample","data"]

# Create S3 Bucket (folder)
sample_bucket = s3.create_bucket(
    Bucket = 'bucket_name' 
)

# Upload extracted data(objects/file) to S3
s3.upload_file(
    'sample-path/data-is-here', # path of the file you wanted to upload 
    'bucket_name', # name of the bucket 
    'newfilename.csv' # file-name of the file you're uploading as they arrive into s3
)

# List Buckets(folder) 
bucket_list = s3.list_buckets()["Buckets"]
print(bucket_list)

# List Objects(file)
object_list = s3.list_objects(  
    Bucket='sample_bucket', # from what bucket 
    MaxKeys=2, # show only two objects 
    Prefix='f') # passing it will limit the response to objects that start with the string we provided 
print(object_list)

# Delete Objects
s3.delete_object(  
    Bucket='sample_bucket', # from what bucket  
    Key='sample_data.csv' # what key of the object we wanted to delete 
)
# check object list again
object_list = s3.list_objects(  
    Bucket='sample_bucket', # from what bucket 
)
print(object_list)

# Delete Buckets
s3.delete_bucket('sample_bucket')

# check bucket list again 
bucket_list = s3.list_buckets()["Buckets"]
print(bucket_list)

