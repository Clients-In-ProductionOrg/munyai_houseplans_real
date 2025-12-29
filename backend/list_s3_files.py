import boto3
import os
from dotenv import load_dotenv

load_dotenv()

access_key = os.getenv('AWS_ACCESS_KEY_ID')
secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
bucket = os.getenv('AWS_STORAGE_BUCKET_NAME')
region = os.getenv('AWS_S3_REGION_NAME')

print(f'\n=== Checking S3 Bucket: {bucket} ===\n')

try:
    s3 = boto3.client('s3', region_name=region, aws_access_key_id=access_key, aws_secret_access_key=secret_key)
    
    # List objects in plans/ folder
    print(f'Files in plans/ folder:\n')
    paginator = s3.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket=bucket, Prefix='plans/')
    
    file_count = 0
    for page in pages:
        if 'Contents' in page:
            for obj in page['Contents']:
                file_count += 1
                print(f'  - {obj["Key"]} ({obj["Size"]} bytes, modified: {obj["LastModified"]})')
    
    if file_count == 0:
        print(f'  ✗ No files found in plans/ folder')
    else:
        print(f'\n✓ Total files: {file_count}')
        
except Exception as e:
    print(f'ERROR: {e}')
