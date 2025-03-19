import json

from datetime import date

def days_between(year, month, day):
    static_date = date(2024, 9, 3)
    today = date.today()
    difference = today - static_date
    return difference.days


# https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html
def lambda_handler(event, context):
    # Extract information from the event object, which represents the incoming request
    http_method = event['httpMethod']
    path = event['path']

    # Process the request based on its method and path
    if http_method == 'GET' and path == '/jobhunt':
        response_body = {'message': f'{days_between(2024, 9, 3)} days since I started unemployment'}
        status_code = 200
    else:
        response_body = {'error': 'Not found'}
        status_code = 404

    # Construct the response object
    response = {
        'statusCode': status_code,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(response_body)
    }

    return response

