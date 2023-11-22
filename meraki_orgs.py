import meraki
import os
from dotenv import load_dotenv
import pprint

# Load environment variables
load_dotenv()

# Defining your API key as a variable in source code is not recommended
API_KEY = os.getenv('MERAKI_API_KEY')

dashboard = meraki.DashboardAPI(API_KEY,output_log=False)


response = dashboard.organizations.getOrganizations()

pprint.pprint(response)