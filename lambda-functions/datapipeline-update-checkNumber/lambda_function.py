def lambda_handler(event, context):
    event['setup']['checkNumber'] = event['setup']['checkNumber']+1
    return event
