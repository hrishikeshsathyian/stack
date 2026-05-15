# script to try extrct jobs via ATS Platform Lever 
import os
from dotenv import load_dotenv
import requests

load_dotenv()
url = os.getenv("LEVER_URL")

if url is None:
    raise ValueError("LEVER_JOBS_URL is not set in .env file")

LEVER_SLUGS = {
    "CSIT" : "csit",
    "Shopback" : "shopback-2"
}

for k, v in LEVER_SLUGS.items(): 
    url = f"https://api.lever.co/v0/postings/{v}"
    response = requests.get(url)
    jobs = response.json()
    for job in jobs:
        job_type = job["categories"]["commitment"]
        if job_type == "Intern":    
            print(job["text"])
            print("\n")

