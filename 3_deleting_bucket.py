# import boto3

# s3 = boto3.client('s3')
# s3_res = boto3.resource('s3')


# s3.delete_bucket(Bucket='my-test-bucket-uniquename-754')


import boto3

s3 = boto3.client('s3')
bucket_name = 'my-test-bucket-uniquename-754'

# Delete bucket
s3.delete_bucket(Bucket=bucket_name)

# Print only bucket name
print(f"Deleted bucket: {bucket_name}")
