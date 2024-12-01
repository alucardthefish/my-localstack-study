# AWS localstack study

Learning about Amazon Web Services (AWS) through LocalStack tool.

## Docker

```commandline
docker-compose up -d --build
```

### Access container
```commandline
docker exec -it <container-name> bash
```

You can use awslocal wrapper tool from both containers

### example in localstack container 

```commandline
awslocal s3 ls
```

### example in my-app-container container 

```commandline
awslocal --endpoint-url=http://localstack:4566 s3 ls
```

## Run S3 example script

```commandline
docker exec -it my-app-container bash
python bucket_sample.py
```
