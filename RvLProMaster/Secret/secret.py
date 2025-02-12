# Load Library
from dotenv import load_dotenv
import os

# Activate Environment
load_dotenv()

class secret:
    def __init__(self):
        self.token = os.getenv('token')
        self.uri = os.getenv('endpoint')
        self.endpoint = f"{self.uri}{self.token}"

# Create Isntance
obj = secret()

# pull information
endpoint = obj.endpoint