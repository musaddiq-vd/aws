
import boto3

s3 = boto3.client('s3')
s3_res = boto3.resource('s3')

#s3.download_file(Bucket, Key (Bucket me file ka naam), Filename)
s3.download_file('my-test-bucket-uniquename', 'localfile.txt', 'downloaded.txt')
#------------------------------------------------------------------------------------
s3.download_file('my-bucket', 'folder1/file.txt', 'C:/Users/HP/Desktop/file.txt')
