#Python Lambda Function - First Test
#Andrew Seibert 4/24/2020

import json

def test_function(event, context):

    body={'message':'OK'}

    params = event['eventStringParameters']



    name =str(params['name'])

    helloString = "Hello, did this work: " + name

    body['helloString'] = helloString



    response={

        'StatusCode':200,

        'body':json.dumps(body),

    }



    return response