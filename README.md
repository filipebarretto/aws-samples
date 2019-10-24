# AWS Samples
Sample codes using AWS services and serverless framework.

## Index

1. [Lambda Image Processing](#lambda-image-processing) 
2. [Translate Text from Image](#translate-text-from-image)


## Sample Applications

<a name="lambda-image-processing"/>
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

![Lambda Image Processing Architecture](https://github.com/filipebarretto/aws-samples/blob/master/architecture-diagrams/lambda-image-processing-achitecture.png?raw=true)


<a name="translate-text-from-image"/>
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

#### Architecture

![Lambda Image Processing Architecture](https://github.com/filipebarretto/aws-samples/blob/master/architecture-diagrams/translate-text-from-image-architecture?raw=true)