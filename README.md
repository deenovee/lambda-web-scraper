# Forex Factory Data Scraping and Reporting Project

## Overview

This project is designed to scrape data from the Forex Factory website and publish the data to an AWS SNS topic. The Lambda function, triggered daily, sends the scraped data to an email subscriber through the SNS topic.

## Prerequisites

Before deploying the project, ensure you have the following:

- AWS Account
- AWS CLI installed and configured
- Python environment for local development

## Parameters

- **Email:**
  - Type: String
  - Description: Email address to receive the report

- **S3Bucket:**
  - Type: String
  - Description: S3 bucket name to store the report

- **SourceFile:**
  - Type: String
  - Description: Path to the source file
  - Default: "lambda_function.py"

## Deployment

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_directory>

2. Deploy the Cloudformation Stack:

aws cloudformation create-stack --stack-name ForexFactoryReportStack --template-body file://cloudformation.yml --parameters file://parameters.json --capabilities CAPABILITY_IAM

3. Monitor the Stack creation.

Project Structure
lambda_function.py: Lambda function code for scraping data and sending reports.
cloudformation_template.yml: CloudFormation template for creating AWS resources.
parameters.json: JSON file containing parameter values for CloudFormation.


Local Development
To test and develop locally, make sure you have Python installed. You can run the Lambda function code locally by executing:

python3 lambda_function.py

Note: Adjust the code as needed for local testing.

To delete the CloudFormation Stack:

aws cloudformation delete-stack --stack-name ForexFactoryReportStack


parameters.json Ex:

[
  {
    "ParameterKey": "Email",
    "ParameterValue": "your_email@example.com"
  },
  {
    "ParameterKey": "S3Bucket",
    "ParameterValue": "your-s3-bucket-name"
  },
  {
    "ParameterKey": "SourceFile",
    "ParameterValue": "lambda_function.py"
  }
]
