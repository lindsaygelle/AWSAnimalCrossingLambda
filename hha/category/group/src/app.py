"""app"""
from typing import Any, AnyStr, Dict
import json


def lambda_handler(
    event: Dict[AnyStr, Any], context: Dict[AnyStr, Any]
) -> Dict[AnyStr, Any]:
    """lambda_handler"""
    return {
        "body": json.dumps(
            {
                "event": event,
            }
        ),
        "statusCode": 200,
    }
