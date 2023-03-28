# This is a sample Python script.

import config
from index import handler



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    config.load_config()

    req = {"requestContext": {"requestId": "884bdb1f7ca4175954958f79317e6386", "apiId": "8b5961e552ab4c5da2e78b487b766b7c", "stage": "RELEASE"}, "queryStringParameters": {"signature": "316db43b1dee34c64abbf151abe4625bb0889196", "openid": "osRxAs1NM8hTkWrVlAwYajNjZrYw", "nonce": "1045843945", "timestamp": "1679979471"}, "path": "/wx", "httpMethod": "POST", "isBase64Encoded": True, "headers": {"host": "www.huqidev.top", "content-type": "text/xml", "x-real-ip": "162.62.80.57", "accept": "*/*", "x-forwarded-proto": "http", "content-length": "283", "pragma": "no-cache", "user-agent": "Mozilla/4.0", "x-forwarded-port": "80", "x-forwarded-host": "www.huqidev.top", "x-forwarded-for": "162.62.80.57", "x-request-id": "884bdb1f7ca4175954958f79317e6386"}, "body": "PHhtbD48VG9Vc2VyTmFtZT48IVtDREFUQVtnaF83ZTc5ZjMyMmVmZTJdXT48L1RvVXNlck5hbWU+CjxGcm9tVXNlck5hbWU+PCFbQ0RBVEFbb3NSeEFzMU5NOGhUa1dyVmxBd1lhak5qWnJZd11dPjwvRnJvbVVzZXJOYW1lPgo8Q3JlYXRlVGltZT4xNjc5OTc5NDcxPC9DcmVhdGVUaW1lPgo8TXNnVHlwZT48IVtDREFUQVt0ZXh0XV0+PC9Nc2dUeXBlPgo8Q29udGVudD48IVtDREFUQVvlv6vpgJ/mjpLluo9dXT48L0NvbnRlbnQ+CjxNc2dJZD4yNDA1MTUyNDY5MDEwNDM4NTwvTXNnSWQ+CjwveG1sPg==", "pathParameters": {}}
    resp = handler(req, None)

    print(resp)

