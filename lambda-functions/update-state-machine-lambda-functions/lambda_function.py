import boto3

# Changes to this lambda function must be manually updated, then it can be run to update all the other associated lambda functions.
def lambda_handler(event, context):

    lambda_client = boto3.client('lambda')

    response = lambda_client.update_function_code(
        FunctionName = 'arn:aws:lambda:us-east-1:849776797214:function:check-cluster-status',
        S3Bucket = 'us-dev-us-east-1-data',
        S3Key = 'step-function-testing/lambda-function-zip-files/check-cluster-status.zip'
    )

    response = lambda_client.update_function_code(
        FunctionName = 'arn:aws:lambda:us-east-1:849776797214:function:check-emr-job-status',
        S3Bucket = 'us-dev-us-east-1-data',
        S3Key = 'step-function-testing/lambda-function-zip-files/check-emr-job-status.zip'
    )

    response = lambda_client.update_function_code(
        FunctionName = 'arn:aws:lambda:us-east-1:849776797214:function:check-emr-timeout',
        S3Bucket = 'us-dev-us-east-1-data',
        S3Key = 'step-function-testing/lambda-function-zip-files/check-emr-timeout.zip'
    )

    response = lambda_client.update_function_code(
        FunctionName = 'arn:aws:lambda:us-east-1:849776797214:function:check-s3-file-exists',
        S3Bucket = 'us-dev-us-east-1-data',
        S3Key = 'step-function-testing/lambda-function-zip-files/check-s3-file-exists.zip'
    )

    response = lambda_client.update_function_code(
        FunctionName = 'arn:aws:lambda:us-east-1:849776797214:function:Datapipeline-StateMachine-Trigger',
        S3Bucket = 'us-dev-us-east-1-data',
        S3Key = 'step-function-testing/lambda-function-zip-files/Datapipeline-StateMachine-Trigger.zip'
    )
    response = lambda_client.update_function_code(
        FunctionName = 'arn:aws:lambda:us-east-1:849776797214:function:datapipeline-update-checkNumber',
        S3Bucket = 'us-dev-us-east-1-data',
        S3Key = 'step-function-testing/lambda-function-zip-files/datapipeline-update-checkNumber.zip'
    )
    response = lambda_client.update_function_code(
        FunctionName = 'arn:aws:lambda:us-east-1:849776797214:function:emr-add-step',
        S3Bucket = 'us-dev-us-east-1-data',
        S3Key = 'step-function-testing/lambda-function-zip-files/emr-add-step.zip'
    )
    response = lambda_client.update_function_code(
        FunctionName = 'arn:aws:lambda:us-east-1:849776797214:function:emr-cluster-create',
        S3Bucket = 'us-dev-us-east-1-data',
        S3Key = 'step-function-testing/lambda-function-zip-files/emr-cluster-create.zip'
    )
    response = lambda_client.update_function_code(
        FunctionName = 'arn:aws:lambda:us-east-1:849776797214:function:emr-pipe-setup',
        S3Bucket = 'us-dev-us-east-1-data',
        S3Key = 'step-function-testing/lambda-function-zip-files/emr-pipe-setup.zip'
    )
    response = lambda_client.update_function_code(
        FunctionName = 'arn:aws:lambda:us-east-1:849776797214:function:increment-step-number',
        S3Bucket = 'us-dev-us-east-1-data',
        S3Key = 'step-function-testing/lambda-function-zip-files/increment-step-number.zip'
    )

    response = lambda_client.update_function_code(
        FunctionName = 'arn:aws:lambda:us-east-1:849776797214:function:terminate-emr-cluster',
        S3Bucket = 'us-dev-us-east-1-data',
        S3Key = 'step-function-testing/lambda-function-zip-files/terminate-emr-cluster.zip'
    )

    return response
