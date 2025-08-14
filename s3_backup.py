import boto3

s3 = boto3.resource("s3")

def s3_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)


def create_bucket(s3, bucket_name, location):
    if location == "us-east-1":
        s3.create_bucket(Bucket=bucket_name)
    else:
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': location}
        )
    print(f"Bucket {bucket_name} created successfully.")


def upload_backup(s3, bucket_name, file_path, key_name):
    with open(file_path, 'rb') as data:
        s3.Bucket(bucket_name).put_object(Key=key_name or file_path, Body=data)
    print("Backup uploaded successfully.")

file_path = "C:/Users/rupal/OneDrive/Desktop/Python/backups/backup_2025-08-07.tar.gz"
bucket_name = "backup-using-python"
location = "us-east-1"

create_bucket(s3, bucket_name, location)
upload_backup(s3, bucket_name, file_path, "backup_2025-08-07.tar.gz")