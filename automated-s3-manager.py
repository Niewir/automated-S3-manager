# Run minio server from terminal using:
# MINIO_ROOT_USER=minioadmin MINIO_ROOT_PASSWORD=minioadmin \ minio server ~/minio-data --console-address ":9001"

# minio client config object call and assign
from s3_client import get_s3_client
s3 = get_s3_client()

# create a bucket
s3.create_bucket(Bucket='solo-bucket')

# create two files and store them in solo-bucket
with open("test1.txt", "x") as file:
    file.write("This file is the first test for s3 stuff.")
s3.upload_file("test1.txt", "solo-bucket", "test1.txt")

with open("test2.txt", "x") as file:
    file.write("This file is the second test.")
s3.upload_file("test2.txt", "solo-bucket", "test2.txt")

# print contents of solo-bucket
response = s3.list_objects_v2(Bucket='solo-bucket')
for item in response.get("Contents", []):
    print(item["Key"])

# download test2.txt from the solo-bucket
s3.download_file("solo-bucket", "test2.txt", "test2-download.txt")

print('done')