import boto3

def lambda_handler(event, context):
    connection = boto3.client('emr')
    cluster_info = connection.describe_cluster(
        ClusterId=event['JobFlowId']
    )
    event['ClusterStatus'] = cluster_info['Cluster']['Status']['State']
    return event