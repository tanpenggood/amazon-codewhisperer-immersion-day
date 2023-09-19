import boto3
import re

# Create SES client
ses = boto3.client('ses')

# function to verify email address and use ses