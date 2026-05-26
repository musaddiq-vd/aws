import boto3
s3 = boto3.client('s3')        # low-level
s3_res = boto3.resource('s3')  # object-oriented


# for listing buckets ---------------------------- 
buckets = s3.list_buckets()
for bkt in buckets['Buckets']:
    print(bkt['Name'])




