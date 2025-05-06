import subprocess
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment
aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")

if not aws_access_key or not aws_secret_key:
    raise EnvironmentError("AWS credentials are missing. Check your .env file.")

os.makedirs("../data/raw", exist_ok=True)

# Download data from S3
subprocess.run([
    "aws", "s3", "cp", "--recursive", "s3://covid-eo-data/xco2-mean/", "./data/raw"
], check=True)
