import json
import boto3
from datetime import datetime
from urllib.parse import unquote

def lambda_handler(event, context):

    event['Records'][0]['s3']['object']['key'] = unquote(event['Records'][0]['s3']['object']['key'])

    s3_resource = boto3.resource('s3')
    s3_obj = s3_resource.Object(
        'us-dev-us-east-1-data',
        'step-function-testing/inputs/Datapipeline-StateMachine-Input.json'
    )

    cluster_configs = json.loads(s3_obj.get()['Body'].read().decode('utf-8'))

    temp = event['Records']
    event = cluster_configs
    event['Records'] = temp

    if 'dt='+datetime.today().strftime('%Y%m%d')+'/_SUCCESS' in event['Records'][0]['s3']['object']['key']:
        sfn_client = boto3.client('stepfunctions')
        response = sfn_client.start_execution(
            stateMachineArn='arn:aws:states:us-east-1:849776797214:stateMachine:Datapipeline-StateMachine',
            input=json.dumps(cluster_configs)
        )

    return event
