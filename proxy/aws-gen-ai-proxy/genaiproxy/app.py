import json
import ai21
import os

# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # get the payload including all params 
    payload = json.loads(event["body"])
    #print(payload)
    #print(type(payload))

    print("calling endpoint {0}".format(os.environ['llm_endpoint_name']))

    response = ai21.Completion.execute(destination=ai21.SageMakerDestination(os.environ['llm_endpoint_name']),
                                   prompt=payload['prompt'],
                                   maxTokens=payload['max_token'],
                                   temperature=payload['temperature'],
                                   numResults=1)


    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": response['completions'][0]['data']['text'],
            # "location": ip.text.replace("\n", "")
        }),
    }
