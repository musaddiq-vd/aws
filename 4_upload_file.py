import boto3

s3 = boto3.client('s3')
s3_res = boto3.resource('s3')

#s3.upload_file(Filename, Bucket, Key)

#s3.upload_file('localfile.txt', 'my-bucket', 'myfolder/localfile.txt')

# Local file upload
s3.upload_file(r'C:\Users\HP\Desktop\interview\boto3\1_listing_bucket.py',  # " r "  use this 
               'give-name-bucket7722', 
               'localfile.txt')  # Bucket me ye naam se upload hoga
