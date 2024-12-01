from aws_utils import initialize_s3_clients


def exec_test():
    s3 = initialize_s3_clients()
    bucket_name = "my-bucket"
    print("Welcome to the S3 example test")
    file_name = input("Enter file name: ")
    input_text = input("Type your message: ")
    if file_name and input_text:
        # Write an object to an S3 bucket
        object_key = f"{file_name}.txt"
        s3.put_object(Bucket=bucket_name, Key=object_key, Body=input_text)
        print(f"Sent message in {object_key} file to S3 bucket")
    else:
        print("No file name or input text provided")
    print("After finish process this is the stored buckets")
    # List buckets and objects
    buckets = s3.list_buckets()
    print("S3 Buckets: ", buckets.get("Buckets", []))

    objects = s3.list_objects_v2(Bucket=bucket_name)
    print("S3 Objects: ", objects.get("Contents", []))

if __name__ == "__main__":
    exec_test()