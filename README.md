# AWS Samples
Sample codes using AWS services and serverless framework.


### Lambda Image Processing

#### About
From an uploaded image to Amazon S3, invokes AWS Lambda functions running in parallel to generate processed images such as:

- Applying watermark
- Thumbnail
- Black and White

And also has a structure to include new types of image processing in new AWS Lambda functions with configured serverless.yml

#### AWS Services Used
This sample application uses:

- Amazon S3
- Amazon SNS
- AWS Lambda

#### Architecture

![Lambda Image Processing Architecture](https://raw.githubusercontent.com/filipebarretto/aws-samples/dev/architecture-diagrams.lambda-image-processing-achitecture.png)


### Translate Text from Image

#### About
From an uploaded image to Amazon S3, invokes a AWS Lambda function that uses Amazon Recognition to detect text and Amazon Translate to translate the detected text to Portuguese. After the text is processed, emails user using SNS with the translated text.


#### AWS Services Used
This sample application uses:

- Amazon S3
- Amazon SNS
- AWS Lambda
- Amazon Rekognition
- Amazon Translate