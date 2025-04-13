import json
import datetime # Example of importing a standard library

print('Loading function') # Runs during 'cold start'

def lambda_handler(event , context):
# 1. Log the incoming event
    print("Received event: " + json.dumps(event , indent=2))

# 2. Get current time
now = datetime.datetime.now()
current_time_str = now.strftime("%Y-%m-%d %H:%M:%S")

# 3. Prepare the response
response_body = {
'message': "Hello from your Lambda function!",
'currentTime': current_time_str ,
'inputEvent': event # Echo back event data
}

# 4. Return a suitable response structure
return {
'statusCode': 200,
'headers': {
'Access -Control -Allow -Origin': '*',
'Access -Control -Allow -Headers': 'Content -Type',
'Access -Control -Allow -Methods': 'OPTIONS ,POST ,GET'
},
'body': json.dumps(response_body)
}

# Helper functions can be defined outside the handler
def helper_function():
    pass