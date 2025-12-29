import boto3
import os
from dotenv import load_dotenv

load_dotenv()

access_key = os.getenv('AWS_ACCESS_KEY_ID')
secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
bucket = os.getenv('AWS_STORAGE_BUCKET_NAME')
region = os.getenv('AWS_S3_REGION_NAME')

print(f'Access Key: {access_key[:10]}...')
print(f'Secret Key: {secret_key[:10]}...')
print(f'Bucket: {bucket}')
print(f'Region: {region}')

try:
    s3 = boto3.client('s3', region_name=region, aws_access_key_id=access_key, aws_secret_access_key=secret_key)
    response = s3.list_objects_v2(Bucket=bucket, MaxKeys=5)
    print('\nS3 Connection OK!')
    print(f'Files in bucket: {response.get("KeyCount", 0)}')
    for obj in response.get('Contents', [])[:3]:
        print(f'  - {obj["Key"]}')
except Exception as e:
    print(f'ERROR: {e}')
    import traceback
    traceback.print_exc()
