import boto3 

# create S3 client
s3 = boto3.client('s3')

# Bucket and file details
bucket_name = 'mollie-learning-bucket'
file_name_in_s3 = 'hello.py'
local_file_name = 'downloaded_hello.py'

# Download file from S3 to local
s3.download_file(bucket_name, file_name_in_s3, local_file_name)

print(f"Downloaded '{file_name_in_s3}' from bucket '{bucket_name}' and saved as '{local_file_name}'. ")
