import boto3

s3 = boto3.client('s3')
s3.upload_file('hello.py', 'mollie-learning-bucket', 'hello.py')

print("Upload successful!")

