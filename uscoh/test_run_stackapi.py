from stackapi import StackAPI

#1: buscar por tags
#2: 


try:
    SITE = StackAPI('stackoverflow')
    SITE.page_size = 1
    SITE.max_pages = 1
    comments = SITE.fetch('search', tagged='haskell', sort="votes", filter="!7qBwspMQR3L7c4q7tesaRX(_gP(rj*U-.H")
    print(comments)
    
except stackapi.StackAPIError as e:
    print("   Error URL: {}".format(e.url))
    print("   Error Code: {}".format(e.code))
    print("   Error Error: {}".format(e.error))
    print("   Error Message: {}".format(e.message))