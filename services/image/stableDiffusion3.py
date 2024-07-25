import requests
import os
from dotenv import load_dotenv

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
