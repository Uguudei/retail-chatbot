# -*- coding: utf-8 -*-
"""
You can create a file called `.env` in the root of the repo, containing your local env vars.
It will be automatically loaded when starting the action server.
"""
import os
from dotenv import load_dotenv

# Load environment variables
# needs to happen before anything else (to properly instantiate constants)

load_dotenv(verbose=True)

# rasa_x_host = os.environ.get("RASA_X_HOST", "rasa-x:5002")
rasa_x_password = os.environ.get("RASA_X_PASSWORD", "")

rasa_x_username = os.environ.get("RASA_X_USERNAME", "me")
rasa_x_host_schema = os.environ.get("RASA_X_HOST_SCHEMA", "http")
