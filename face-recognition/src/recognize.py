import os
import io
import json
import boto3


rekognition = boto3.client('rekognition')

THRESHOLD = 80
MAX_FACES = 2
COLLECTION_ID = "MY_SAMPLE_COLLECTION"

def main(event, context):
    print("Running recognize.py to identify user from photo...")
    print(event)
    
    # GET IMAGE INFO FROM S3 EVENT
    s3_bucket = event["Records"][0]["s3"]["bucket"]["name"]
    s3_obj = event["Records"][0]["s3"]["object"]["key"]
    
    print("S3 Bucket: " + s3_bucket)
    print("S3 Object: " + s3_obj)
    
    # GET ORIGINAL IMAGE
    
    

    response = rekognition.search_faces_by_image(CollectionId = COLLECTION_ID,
                                          Image={'S3Object':{'Bucket': s3_bucket,'Name': s3_obj}},
                                          FaceMatchThreshold = THRESHOLD,
                                          MaxFaces = MAX_FACES)
        
    faceMatches=response['FaceMatches']
    print ('Matching faces')
    for match in faceMatches:
        print ('FaceId:' + match['Face']['FaceId'])
        print ('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")
        print

