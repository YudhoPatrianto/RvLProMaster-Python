# Load Library
from dotenv import load_dotenv
import os

# Activate Environment
load_dotenv()

class secret:
    def __init__(self):
        self.token = os.environ.get('token')
        self.endpoint = f"{os.environ.get('endpoint')}/bot{os.environ.get('token')}"
        
GetSecret = secret()