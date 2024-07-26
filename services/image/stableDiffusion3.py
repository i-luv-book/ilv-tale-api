import requests
import os
from dotenv import load_dotenv
from services.image.S3 import *

load_dotenv("~/EvalServer/.env")

def genarateImage(prompt):
    response = requests.post(
        f"https://api.stability.ai/v2beta/stable-image/generate/sd3",
        headers={
            "authorization": f"Bearer {os.getenv("STABLE_DIFFUSION_KEY")}",
            "accept": "image/*"
        },
        files={"none": ''},
        data={
            "prompt": prompt,
            "seed" : 127,
            "output_format": "jpeg",
            "model" : "sd3-large-turbo",
        },
    )
    return response

def getImageURL(gptManager,promptManger,parseManager,s3Client,region,tale,isTest):

    if isTest :
        imgURL = "https://iluvbook-bucket.s3.ap-northeast-2.amazonaws.com/taleimage/523ce727-5b39-4980-a7d7-dbe35aff9b8b"
        return imgURL

    taleToKeywords = gptManager.taleToKeywords(promptManger.taleToKeywordsPrompt, tale)
    imageKeywords = parseManager.parseImageKeywords(taleToKeywords)
    img = genarateImage(imageKeywords)
    imgURL = uploadImageToS3(s3Client, img.content, region)

    return imgURL
