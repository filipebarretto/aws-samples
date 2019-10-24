# Translate Text from Image

### About
From an uploaded image to Amazon S3, invokes a AWS Lambda function that uses Amazon Recognition to detect text and Amazon Translate to translate the detected text to Portuguese. After the text is processed, emails user using SNS with the translated text.


### AWS Services Used
This sample application uses:

- Amazon S3
- Amazon SNS
- AWS Lambda
- Amazon Rekognition
- Amazon Translate

### Architecture

![Lambda Image Processing Architecture](https://github.com/filipebarretto/aws-samples/blob/master/architecture-diagrams/translate-text-from-image-architecture.png?raw=true)