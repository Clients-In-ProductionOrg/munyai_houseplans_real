import boto3
import os
from dotenv import load_dotenv

load_dotenv()

access_key = os.getenv('AWS_ACCESS_KEY_ID')
secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
bucket = os.getenv('AWS_STORAGE_BUCKET_NAME')
region = os.getenv('AWS_S3_REGION_NAME')

print(f'Bucket: {bucket}')
print(f'Region: {region}')

try:
    s3 = boto3.client('s3', region_name=region, aws_access_key_id=access_key, aws_secret_access_key=secret_key)
    
    # Try to upload a test file
    print('\nAttempting to upload test file to S3...')
    test_content = b'Test file content'
    test_key = f'plans/test_{os.urandom(4).hex()}.txt'
    
    s3.put_object(Bucket=bucket, Key=test_key, Body=test_content)
    print(f'✓ Upload successful!')
    print(f'✓ File location: s3://{bucket}/{test_key}')
    print(f'✓ Public URL: https://{bucket}.s3.{region}.amazonaws.com/{test_key}')
    
except Exception as e:
    print(f'✗ ERROR: {e}')
    import traceback
    traceback.print_exc()
