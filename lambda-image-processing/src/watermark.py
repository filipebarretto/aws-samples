import os
import io
import json
import boto3
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

s3 = boto3.resource("s3")


def main(event, context):
    print("Running watermark.py to apply watermark to image...")
    print(event)
    
    # GET IMAGE INFO FROM S3 EVENT
    msg = json.loads(event['Records'][0]["Sns"]["Message"])
    s3_bucket = msg["Records"][0]["s3"]["bucket"]["name"]
    s3_obj = msg["Records"][0]["s3"]["object"]["key"]
    img = s3_obj.split("/")[-1]
    
    print("S3 Bucket: " + s3_bucket)
    print("S3 Object: " + s3_obj)
    print("Image File: " + img)
    
    # GET ORIGINAL IMAGE AND WATERMARK
    foreground = Image.open("./src/assets/watermark.png")
    
    s3.Object(s3_bucket, s3_obj).download_file("/tmp/raw.png")
    background = Image.open("/tmp/raw.png")

    # CONCATENATE LAYERS
    print("Applying watermark to image...")
    background.paste(foreground, (0, 0), foreground)
    
    # GENERATE PROCESSED IMAGE
    print("Saving processed image to tmp...")
    background.save("/tmp/" + img)
    
    # SAVE FILE TO S3
    print("Uploading processed image to S3...")
    s3.Object(s3_bucket, "watermarks/" + img).upload_file("/tmp/" + img)

    print("Watermark applied to " + img + " and saved to s3.")

