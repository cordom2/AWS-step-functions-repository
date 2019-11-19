import boto3

# This function is coming directly from the S3 Bucket
def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(event['S3Bucket'])
    key = event['S3Key']
    objs = list(bucket.objects.filter(Prefix=key))
    if len(objs) > 0 and objs[0].key == key:
        event['fileExists'] = True
    else:
        event['fileExists'] = False

    return event