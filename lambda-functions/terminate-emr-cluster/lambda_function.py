import boto3

def lambda_handler(event, context):
    connection = boto3.client('emr')
    connection.terminate_job_flows(
        JobFlowIds = [
            event['JobFlowId']
        ]
    )

    return event
