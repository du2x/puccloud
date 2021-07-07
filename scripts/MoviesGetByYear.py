from pprint import pprint
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key

import boto3

def get_movies(year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Movies')

    try:
        response = table.query(KeyConditionExpression=Key('year').eq(year))
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        pprint(response)
        return response['Items']
        
        
if __name__ == '__main__':
    movies = get_movies(2016)
    if movies:
        print("Get movies succeeded:")
        pprint(movies)
