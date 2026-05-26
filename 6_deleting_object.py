import boto3
s3 = boto3.client('s3')        # low-level
s3_res = boto3.resource('s3')  # object-oriented


s3.delete_object(Bucket='my-test-bucket-uniquename', Key='localfile.txt')
