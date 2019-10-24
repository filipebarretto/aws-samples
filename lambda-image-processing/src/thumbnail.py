import os
import io
import json
import boto3
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

s3 = boto3.resource("s3")

thumbnail_size = 128, 128

def main(event, context):
    print("Running thumbnail to creat thumbnail for original image...")
    print(event)
    
    # GET IMAGE INFO FROM S3 EVENT
    msg = json.loads(event['Records'][0]["Sns"]["Message"])
    s3_bucket = msg["Records"][0]["s3"]["bucket"]["name"]
    s3_obj = msg["Records"][0]["s3"]["object"]["key"]
    img = s3_obj.split("/")[-1]
    
    print("S3 Bucket: " + s3_bucket)
    print("S3 Object: " + s3_obj)
    print("Image File: " + img)
    
    # GET ORIGINAL IMAGE
    s3.Object(s3_bucket, s3_obj).download_file("/tmp/original.png")
    original = Image.open("/tmp/original.png")
    
    # RESIZE IMAGE
    print("Resizing image...")
    original.thumbnail(thumbnail_size, Image.ANTIALIAS)
    original.save("/tmp/" + img)
    
    # SAVE THUMBNAIL TO S3
    print("Uploading thumbnail to S3...")
    s3.Object(s3_bucket, "thumbnails/" + img).upload_file("/tmp/" + img)
    
    print("Thumbnail generated from " + img + " and saved to s3.")

