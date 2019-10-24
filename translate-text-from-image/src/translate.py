import os
import io
import json
import boto3


rekognition = boto3.client('rekognition')
translate = boto3.client(service_name='translate', region_name='us-east-1', use_ssl=True)

def main(event, context):
    print("Running translate.py to translate text from images...")
    print(event)
    
    # GET IMAGE INFO FROM S3 EVENT
    s3_bucket = event["Records"][0]["s3"]["bucket"]["name"]
    s3_obj = event["Records"][0]["s3"]["object"]["key"]
    
    print("S3 Bucket: " + s3_bucket)
    print("S3 Object: " + s3_obj)
    
    # GET ORIGINAL IMAGE
    
    response = rekognition.detect_text(Image={'S3Object':{'Bucket':s3_bucket,'Name':s3_obj}})
    
    textDetections = response['TextDetections']
    
    str = ""
    print ('Detected text')
    for text in textDetections:
        print ('Detected text: ' + text['DetectedText'])
        str += text['DetectedText'] + " "
        print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
        print ('Id: {}'.format(text['Id']))
        if 'ParentId' in text:
            print ('Parent Id: {}'.format(text['ParentId']))
            print ('Type:' + text['Type'])
            print("\n")


    print("Final String: " + str)

    result = translate.translate_text(Text= str, SourceLanguageCode="auto", TargetLanguageCode="pt")
    print('TranslatedText: ' + result.get('TranslatedText'))

