import requests
from dotenv import load_dotenv
from pydantic import BaseModel
import os
import logging

load_dotenv()
url = os.getenv("CAREER_LISTING_URL")
logging.basicConfig(level=logging.DEBUG)

class Job(BaseModel): 
    postingNo: str  # unique posting GUID 
    jobId: str      # numeric job ID
    jobTitle: str   # jobTitle 


if url is not None:
    logging.info("Fetching Jobs..")
    response = requests.get(url)
    jobs = response.json()
    jobs = jobs[:10]
    jobs = [Job(**job) for job in jobs]
    print(jobs)
