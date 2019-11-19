import boto3

def lambda_handler(event, context):
    connection = boto3.client('emr')
    step_info = connection.describe_step(
        ClusterId=event['JobFlowId'],
        StepId=event['response']['StepIds'][0]
    )
    event['StepStatus'] = step_info['Step']['Status']['State']

    cluster_info = connection.describe_cluster(
        ClusterId=event['JobFlowId']
    )
    event['ClusterStatus'] = cluster_info['Cluster']['Status']['State']

    return event