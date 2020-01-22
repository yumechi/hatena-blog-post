import json
from copy import deepcopy
import urllib.parse


def has_required_params(event):
    """
    必須キーチェック
    """
    required_key = ["title", "content"]
    for key in required_key:
        if key not in event:
            raise ValueError(key)

def normalize_params(params):
    """
    特定のキーをhtmlエンコードする(最終的にXMLリクエストするため)
    """ 
    normalized_key = ["title", "content", "category"]
    params_ = deepcopy(params)
    for key in normalized_key:
        if key in params_:
            params_[key] = urllib.parse.quote(params_[key])
    return params_


def blog_post(event, context):
    try:
        has_required_params(event)
    except:
        return response = {
            "statusCode": 500,
            "error": "Invalid request",
            "detail": "Missing required params",
        }
    normalized_params = normalize_params(event["body"])

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
