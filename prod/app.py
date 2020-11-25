from pprint import pprint
import json
import boto3
def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb',region_name='ca-central-1')
    table = dynamodb.Table('webpage')
    item = table.get_item(
        Key={
            "pageId":0,
        }
        )
    table.update_item(
        Key={
            "pageId":0,
        },
        UpdateExpression='SET quantity = :val1',
        ExpressionAttributeValues={
            ':val1': item['Item']['quantity'] + 1
        }
    )

    return {
        "statusCode": 200,
        "body": {"Visit_Count": str(item['Item']['quantity'] + 1)}
    }
