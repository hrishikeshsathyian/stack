# script to try extrct jobs via ATS platform SmartRecruiters 
import os
from dotenv import load_dotenv
import requests

load_dotenv()
BASE_URL = os.getenv("SMART_RECRUITERS_URL")

if BASE_URL is None:
    raise ValueError("LEVER_JOBS_URL is not set in .env file")

SMART_RECRUITER_SLUGS = {
    "Grab"      : "Grab",
    "Bosch"     : "BoschGroup",
    "Visa"      : "Visa",
    "Carousell" : "CarousellGroup",
    "Foodpanda" : "DeliveryHero",
}

for company, slug in SMART_RECRUITER_SLUGS.items(): 
    url = f"{BASE_URL}{slug}/postings"
    response = requests.get(url)
    jobs = response.json()
    for job in jobs["content"]: 
        job_type = job["experienceLevel"]["label"]
        job_location = job["location"]["country"]
        if job_type == "Internship" and job_location == "sg":
            print(job)
            print("\n")
