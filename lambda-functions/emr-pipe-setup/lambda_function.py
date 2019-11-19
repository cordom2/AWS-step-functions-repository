def lambda_handler(event, context):
    event['stepNumber'] = 0
    event['noMoreSteps'] = False
    event['timeoutIncrement'] = 0
    event['hasClusterTimedOut'] = False
    if 'emr-configs-input' in event:
        event.update(event.pop('emr-configs-input'))

    return event