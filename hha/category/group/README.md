# HHA Category Group
HHA Category Group AWS Lambda Function.

## Setup
Here's a brief set of steps to run AWS SAM locally from the `/category/group` directory:

1. Make sure you have `Docker` installed on your machine.
2. Open a terminal window and navigate to the `/category/group` directory.
3. Run the following command to build the Lambda function and generate a CloudFormation stack:

```bash
sam build
```

4. Run the following command to start a local API Gateway to test the function:

```bash
sam local start-api
```

5. Send a test request to the local API Gateway using a tool like `curl` or a web browser to test the Lambda function. For example:

```bash
curl http://127.0.0.1:3000/
```

This will send a GET request to the `/categories` endpoint of the local API Gateway, which should trigger the Lambda function and return a response.


## AWS Serverless Resources
Below are some additional resources relating to AWS Serverless.

### Globals
Resources in a SAM template tend to have shared configuration such as Runtime, Memory, VPC Settings, Environment Variables, Cors, etc. Instead of duplicating this information in every resource, you can write them once in the Globals section and let all resources inherit it.

https://github.com/awslabs/serverless-application-model/blob/master/docs/globals.rst

### Function Resource
Creates a Lambda function, IAM execution role, and event source mappings which trigger the function.

https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction

### API Event Source
If an `AWS::Serverless::Api` resource is defined, the path and method values MUST correspond to an operation in the OpenAPI definition of the API. If no `AWS::Serverless::Api` is defined, the function input and output are a representation of the HTTP request and HTTP response. For example, using the JavaScript API, the status code and body of the response can be controlled by returning an object with the keys statusCode and body.

https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#api

### SAM Implicit Resources
This is called an "Implicit API". There can be many functions in the template that define these APIs. Behind the scenes, SAM will collect all implicit APIs from all Functions in the template, generate a Swagger, and create an implicit AWS::Serverless::Api using this Swagger. This API defaults to a StageName called "Prod" that cannot be configured.

https://github.com/awslabs/serverless-application-model/blob/master/docs/internals/generated_resources.rst#api
