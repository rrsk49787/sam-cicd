def lambda_handler(event, context):
   html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AWS SAM Demo</title>
<style>
           body {
               font-family: Arial, sans-serif;
               text-align: center;
               background-color: #f4f4f9;
               padding: 50px;
           }
           h1 {
               color: #333;
           }
           .button {
               background-color: #008cba;
               color: white;
               padding: 10px 20px;
               text-decoration: none;
               font-size: 16px;
               margin-top: 20px;
               display: inline-block;
               border-radius: 5px;
           }
           .button:hover {
               background-color: #005f73;
           }
</style>
</head>
<body>
<h1>Welcome to My AWS SAM Demo!</h1>
<p>This is a simple HTML page served from AWS SAM CI/CD pipeline!</p>
<a href="https://aws.amazon.com" class="button">Learn More About AWS</a>
</body>
</html>
   """
   return {
       "statusCode": 200,
       "headers": {
           "Content-Type": "text/html"
       },
       "body": html_content
   }
