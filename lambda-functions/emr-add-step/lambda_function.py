import boto3

def lambda_handler(event, context):
    stepNum = event['stepNumber']

    if 'ActionOnFailure' in event['Steps'][stepNum]:
        ActionOnFailure = event['Steps'][stepNum]['ActionOnFailure']
    else:
        ActionOnFailure = 'CONTINUE'
    if 'Name' in event['Steps'][stepNum]:
        Name = event['Steps'][stepNum]['Name']
    else:
        Name = 'emr-step'
    if 'MainClass' in event['Steps'][stepNum]:
        MainClass = event['Steps'][stepNum]['MainClass']
    else:
        MainClass = ''
    if 'Properties' in event['Steps'][stepNum]:
        Properties = event['Steps'][stepNum]['Properties']
    else:
        Properties = []

    connection = boto3.client('emr')
    event['response'] = connection.add_job_flow_steps(
        JobFlowId = event['JobFlowId'],
        Steps = [
            {
                'Name': Name,
                'ActionOnFailure': ActionOnFailure,
                'HadoopJarStep': {
                    'Jar': event['Steps'][stepNum]['Jar'],
                    'MainClass': MainClass,
                    'Properties': Properties,
                    'Args': event['Steps'][stepNum]['Args']
                }
            }
        ]

    )

    return event
