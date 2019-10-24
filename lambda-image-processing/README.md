# Lambda Image Processing

### About
From an uploaded image to Amazon S3, invokes AWS Lambda functions running in parallel to generate processed images such as:

- Applying watermark
- Thumbnail
- Black and White

And also has a structure to include new types of image processing in new AWS Lambda functions with configured serverless.yml

### AWS Services Used
This sample application uses:

- Amazon S3
- Amazon SNS
- AWS Lambda

### Architecture

![Lambda Image Processing Architecture](https://github.com/filipebarretto/aws-samples/blob/master/architecture-diagrams/lambda-image-processing-achitecture.png?raw=true)
