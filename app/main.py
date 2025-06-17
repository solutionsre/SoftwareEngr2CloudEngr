import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMO_TABLE'])

def lambda_handler(event, context):
    item = {
        'id': '1',
        'message': 'Hello from Lambda with DynamoDB!'
    }
    table.put_item(Item=item)
    return {
        'statusCode': 200,
        'body': json.dumps('Data written to DynamoDB!')
    }
