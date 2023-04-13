# pylint: disable=C0114
from typing import Any, AnyStr, Dict
import json

# pylint: disable=W0613
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
