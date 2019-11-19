def lambda_handler(event, context):
    event['stepNumber'] = event['stepNumber'] + 1

    stepNum = event['stepNumber']

    if stepNum < len(event['Steps']):
        return event
    else:
        event['noMoreSteps'] = True

    return event
