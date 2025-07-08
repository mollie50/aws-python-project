import boto3

# Create S3 client
s3 = boto3.client('s3')

# call the deletion method 
s3.delete_object(
    Bucket='mollie-learning-bucket',
    Key='hello.py'
)

print("Deleted file from bucket.")