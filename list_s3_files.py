import boto3

# Create S3 client
s3 = boto3.client('s3')

# bucket name
bucket_name = 'mollie-learning-bucket'

# list objects
response = s3.list_objects_v2(Bucket=bucket_name)

# check and print
if 'Contents' in response:
    print(f"Files in bucket '{bucket_name}':")
    for obj in response['Contents']:
        print(f" - {obj['Key']}")

else:
    print(f"No files found in bucket '{bucket_name}'.")
