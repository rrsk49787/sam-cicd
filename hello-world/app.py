import json
def lambda_handler(event, context):
   return {
       "statusCode": 200,
       "body": json.dumps({
           "message": "Hello from SAM CI/CD pipeline!",
       }),
      for i in range (10):
        print(i)
   }
