import boto3
from datetime import datetime

def lambda_handler(event, context):

    if 'Name' in event:
        _Name = event['Name']
    else:
        _Name = 'state-machine-EMR-cluster'
    if 'LogUri' in event:
        _LogUri = event['LogUri']
    else:
        _LogUri = 's3://us-dev-us-east-1-logs/'
    if 'Ec2SubnetId' in event:
        Ec2SubnetId = event['Ec2SubnetId']
    else:
        Ec2SubnetId = 'subnet-0a0dfb41d41350224'
    if 'EmrManagedMasterSecurityGroup' in event:
        EmrManagedMasterSecurityGroup = event['EmrManagedMasterSecurityGroup']
    else:
        EmrManagedMasterSecurityGroup = 'sg-05186248c810d09a3'
    if 'EmrManagedSlaveSecurityGroup' in event:
        EmrManagedSlaveSecurityGroup = event['EmrManagedSlaveSecurityGroup']
    else:
        EmrManagedSlaveSecurityGroup = 'sg-0c9d9eae7eb81c911'
    if 'ScaleDownBehavior' in event:
        _ScaleDownBehavior = event['ScaleDownBehavior']
    else:
        _ScaleDownBehavior = 'TERMINATE_AT_TASK_COMPLETION'
    if 'KeepJobFlowAliveWhenNoSteps' in event:
        KeepJobFlowAliveWhenNoSteps = event['KeepJobFlowAliveWhenNoSteps']
    else:
        KeepJobFlowAliveWhenNoSteps = True
    if 'Ec2KeyName' in event:
        Ec2KeyName = event['Ec2KeyName']
    else:
        Ec2KeyName = ''
    if 'JobFlowRole' in event:
        _JobFlowRole = event['JobFlowRole']
    else:
        _JobFlowRole = event['ServiceRole']
    if 'Applications' in event:
        _Applications = event['Applications']
    else:
        _Applications = [
            {
                'Name':'Spark'
            },
            {
                'Name': 'Hadoop'
            },
            {
                'Name': 'Hive'
            },
            {
                'Name': 'ganglia'
            },
            {
                'Name': 'pig'
            }
        ]

    connection = boto3.client('emr')
    cluster_id = connection.run_job_flow(
        Name = _Name + '_' + datetime.today().strftime('%Y%m%d'),
        ReleaseLabel = event['EMR_RELEASE_LABEL'],
        LogUri = _LogUri,
        Instances = {
            'Ec2KeyName': Ec2KeyName,
            'Ec2SubnetId': Ec2SubnetId,
            'EmrManagedMasterSecurityGroup': EmrManagedMasterSecurityGroup,
            'EmrManagedSlaveSecurityGroup': EmrManagedSlaveSecurityGroup,
            'KeepJobFlowAliveWhenNoSteps': KeepJobFlowAliveWhenNoSteps,
            'InstanceGroups': [
                {
                    'Name': 'Master nodes',
                    'Market': 'ON_DEMAND',
                    'InstanceRole': 'MASTER',
                    'InstanceType': event['MASTER_INSTANCE_TYPE'],
                    'InstanceCount': 1
                },
                {
                    'Name': 'Slave nodes',
                    'Market': 'SPOT',
                    'InstanceRole': 'CORE',
                    'InstanceType': event['CORE_INSTANCE_TYPE'],
                    'InstanceCount': event['CORE_INSTANCE_COUNT']
                }
            ]
        },
        ServiceRole = event['ServiceRole'],
        JobFlowRole = _JobFlowRole,
        VisibleToAllUsers = True,
        ScaleDownBehavior = _ScaleDownBehavior

    )

    event['JobFlowId'] = cluster_id['JobFlowId']
    return event
