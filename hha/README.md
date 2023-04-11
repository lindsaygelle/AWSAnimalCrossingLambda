# HHA Category
HHA Category AWS Lambda.

## AWS Lambda Function for Category Data
This AWS Lambda function is written in Python and is designed to connect to a storage location on AWS to access data associated with the "category" data source from the Happy Home Academy (HHA) endpoint. This README file provides a brief overview of the function and instructions for setting up and deploying it.

## Functionality
The Lambda function connects to an AWS storage location using the appropriate credentials and retrieves the data associated with the "HHA category". The function then processes this data and performs the necessary operations before returning the result, which can include 0 to N items from the data store.

# Setup
Before deploying the Lambda function, you will need to set up the following:

- An AWS account with appropriate permissions to create and manage Lambda functions.
- Local AWS credentials configured on your machine.
- Docker installed on your machine to be able to use the AWS SAM CLI.
- Terraform installed on your machine to be able to deploy AWS resources.
- AWS SAM CLI installed on your machine to be able to build and deploy the Lambda function.
- A storage location on AWS with the data associated with HHA category.
- Appropriate credentials to access the storage location.
