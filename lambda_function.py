import json
import datetime

print('Loading function')

# Line defining the function (NO indent)
def lambda_handler(event, context):
    # Line 8: MUST be indented (e.g., 4 spaces)
    print("Received event: " + json.dumps(event, indent=2))

    # Subsequent lines inside the function MUST have the same indent
    now = datetime.datetime.now()
    current_time_str = now.strftime("%Y-%m-%d %H:%M:%S")

    response_body = {
        'message': "Hello from your Lambda function!",
        'currentTime': current_time_str,
        'inputEvent': event
    }

    # The return statement MUST also be indented
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(response_body)
    }

# Code outside the function starts back at NO indent
# def helper_function():
#     pass