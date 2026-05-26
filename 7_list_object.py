import boto3
s3 = boto3.client('s3')        # low-level
s3_res = boto3.resource('s3')  # object-oriented


objects = s3.list_objects_v2(Bucket='my-test-bucket-uniquename')
for obj in objects.get('Contents', []):
    print(obj['Key'])
