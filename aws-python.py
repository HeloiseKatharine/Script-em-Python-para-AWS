import boto3

s3 = boto3.resource('s3')

name_bucket = 'name_bucket'
name_file = 'arquivo.zip'

# Upload do aquivo
data = open(name_file, 'rb')
s3.Bucket(name_bucket).put_object(Key=name_file, Body=data)