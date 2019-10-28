import os
import io
import json
import boto3


rekognition = boto3.client('rekognition')
COLLECTION_ID = "MY_SAMPLE_COLLECTION"


def add_faces_to_collection(bucket, photo):
    
    response=client.index_faces(CollectionId = COLLECTION_ID,
                                Image={'S3Object':{'Bucket': bucket, 'Name': photo}},
                                ExternalImageId = photo,
                                MaxFaces = 1,
                                QualityFilter = "AUTO",
                                DetectionAttributes = ['ALL'])
        
    print ('Results for ' + photo)
    print('Faces indexed:')
    for faceRecord in response['FaceRecords']:
        print('  Face ID: ' + faceRecord['Face']['FaceId'])
        print('  Location: {}'.format(faceRecord['Face']['BoundingBox']))

    print('Faces not indexed:')
    for unindexedFace in response['UnindexedFaces']:
        print(' Location: {}'.format(unindexedFace['FaceDetail']['BoundingBox']))
        print(' Reasons:')
        for reason in unindexedFace['Reasons']:
            print('   ' + reason)

    return len(response['FaceRecords'])


def main(event, context):
    print("Running catalog.py to catalog image in collection...")
    print(event)
    
    # GET IMAGE INFO FROM S3 EVENT
    s3_bucket = event["Records"][0]["s3"]["bucket"]["name"]
    s3_obj = event["Records"][0]["s3"]["object"]["key"]
    
    print("S3 Bucket: " + s3_bucket)
    print("S3 Object: " + s3_obj)
    
    # GET ORIGINAL IMAGE
    indexed_faces_count=add_faces_to_collection(bucket, photo, collection_id)
    print("Faces indexed count: " + str(indexed_faces_count))

