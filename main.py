# This is a sample Python script.

import config
from index import handler


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print(cache.get("aa"))
    #cache.set_key("bb", "bb")
    #print(cache.get("bb"))
    config.load_config()

    req = {"requestContext": {"requestId": "59d0ee05a18b1d586ef7602fb1dfc0f8", "apiId": "8b5961e552ab4c5da2e78b487b766b7c", "stage": "RELEASE"}, "queryStringParameters": {"signature": "27b851c7933b59fb592a472bc26bab8968019845", "msg_signature": "3a496157a49b8301b1dad6ccd3544b672634152d", "timestamp": "1679887349", "openid": "osRxAs1NM8hTkWrVlAwYajNjZrYw", "nonce": "2084766652", "encrypt_type": "aes"}, "path": "/wx", "httpMethod": "POST", "isBase64Encoded": True, "headers": {"host": "www.huqidev.top", "content-type": "text/xml", "x-real-ip": "162.62.81.123", "accept": "*/*", "x-forwarded-proto": "http", "content-length": "820", "pragma": "no-cache", "user-agent": "Mozilla/4.0", "x-forwarded-port": "80", "x-forwarded-host": "www.huqidev.top", "x-forwarded-for": "162.62.81.123", "x-request-id": "59d0ee05a18b1d586ef7602fb1dfc0f8"}, "body": "PHhtbD4KICAgIDxUb1VzZXJOYW1lPjwhW0NEQVRBW2doXzdlNzlmMzIyZWZlMl1dPjwvVG9Vc2VyTmFtZT4KICAgIDxGcm9tVXNlck5hbWU+PCFbQ0RBVEFbb3NSeEFzMU5NOGhUa1dyVmxBd1lhak5qWnJZd11dPjwvRnJvbVVzZXJOYW1lPgogICAgPENyZWF0ZVRpbWU+MTY3OTg4NzM0ODwvQ3JlYXRlVGltZT4KICAgIDxNc2dUeXBlPjwhW0NEQVRBW3RleHRdXT48L01zZ1R5cGU+CiAgICA8Q29udGVudD48IVtDREFUQVvlpKnlpKfnmoTnrJHor51dXT48L0NvbnRlbnQ+CiAgICA8TXNnSWQ+MjQwNTAyMDQ1MjY1NDg3NDY8L01zZ0lkPgogICAgPEVuY3J5cHQ+PCFbQ0RBVEFbTklRU2I5RGdpNFc2Tk1ocW56Mzd0cnAvaFNNWmFDUmV4L2I5UFp0N0JvT0ZrQmpSbWhYT1Y4L1IzQ1c3azdYQ3N1L1FGcjg0eGdYYnJaREh1bW5xdklHQ0ZOclhRODhzbHgwODA0ckFvbTZ4blUxVEZ4OFRmOEJlNm9JellLVTJwNFg0SEo3K2NqWm5WdXZxTk91M0laaVJ1L2dYWlVVNTluaVlUUkt1SGQ3ck15RkNtRHpaMGlZKzNCdTNDWmFaUmlTWW5DTExrSEZBWTlKc2M4bnVsR0d1WDhDS0ZEeGpBT2NiZGRpQnFlcVNSSW1EcmlTNlNJVFpuV2VobXNrUzVRYmdObHAxSkZSMk9DZ3FQc3RONm50c3pPNWVzdmJqRmV6bHRqeUJQZitldGVNajNtK0RWQVRoWmM1VWo1eERpNEg2bll3QUJvWC9LdmxGZnBsbEJYd0Q0MTlyVWtkeFp1RFp2aDdpYTNpa2JvVlNscXhqeU42OXgva1hRSzNXeE1Ndmc3SDdJTzIxRkZ1enc1QXFockt6Z2szLzBnaHFwOS9QWGRWdkJ1ODBVd2NPaGpmT1p2WDhkYm1TRDBQOXJlNjlEcVdqY2l4YTI3MXpLYzZDWlE9PV1dPjwvRW5jcnlwdD4KPC94bWw+Cg==", "pathParameters": {}}
    resp = handler(req, None)

    print_hi(resp)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
