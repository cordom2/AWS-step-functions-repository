def lambda_handler(event, context):

    if event['timeoutIncrement'] < event['TIMEOUT_AFTER_X_HOURS']*4:
        event['timeoutIncrement'] = event['timeoutIncrement']+1
    else:
        event['hasClusterTimedOut'] = True

    return event