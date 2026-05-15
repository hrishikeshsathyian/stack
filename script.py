import requests
from dotenv import load_dotenv
from pydantic import BaseModel, field_validator
import datetime
import os

load_dotenv()
url = os.getenv("CAREERS_GOV_DATA_URL")

if url is None:
    raise ValueError("CAREERS_GOV_DATA_URL is not set in .env file")

INTERNSHIP_EMPLOYMENT_TYPE = "Internship"
INTERNSHIP_EMPLOYMENT_TYPE_CODE = "0005"
INDUSTRY_FIELD_CODE_OTHERS = "0025"
INDUSTRY_FIELD_CODE_IT = "0017"

class Job(BaseModel): 
    postingNo: str                  # unique posting GUID 
    jobId: str                      # numeric job ID
    jobTitle: str                   # jobTitle 
    agency: str                     # agency name 
    startDate: datetime.datetime    # Job posting start date as Unix timestamp in milliseconds (e.g., "1770681600000")
    closingDate: datetime.datetime
    remainingDays: str              # readable string for the amount of days left 
    employmentType: str             # this should be eventually fixed to be internship 
    employmentTypeCode: str         # secondary verification 
    industry: str                   # industry categorization
    fieldCode: str
    @field_validator('startDate', 'closingDate', mode='before')
    @classmethod
    def convert_time(cls, value : str):
        return datetime.datetime.fromtimestamp(
            int(value) / 1000,  # convert milliseconds to seconds
            datetime.timezone(datetime.timedelta(hours=8))  # SGT
        )

response = requests.get(url)
jobs = response.json()

filteredJobs = [
    job for job in jobs 
    if job["employmentType"] == INTERNSHIP_EMPLOYMENT_TYPE 
        and job["employmentTypeCode"] == INTERNSHIP_EMPLOYMENT_TYPE_CODE
        and job["fieldCode"] == INDUSTRY_FIELD_CODE_IT
]

jobs = [Job(**job) for job in filteredJobs]
for job in jobs:
    print(job)
    print('\n')
