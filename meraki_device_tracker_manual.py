import meraki
import csv
import json
import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# Your Meraki API key and Organization ID
API_KEY = os.getenv('MERAKI_API_KEY')
ORG_ID = os.getenv('MERAKI_ORG_ID')

# Schedule variables
SCHEDULE_INTERVAL = 2  # Interval number
SCHEDULE_UNIT = 'minutes' # Unit of time, can be 'minutes', 'hours', 'days', etc.

# Initialize the Meraki dashboard API
dashboard = meraki.DashboardAPI(API_KEY,output_log=False)

def fetch_and_save_device_data():
    try:
        online_devices_count = 0
        per_page = 1000
        page = 1

        while True:
            # Fetch the status of devices in the organization with pagination
            device_statuses = dashboard.organizations.getOrganizationDevicesStatuses(
                ORG_ID, perPage=per_page, startingAfter=(page-1)*per_page
            )

            # Count the number of online devices in this batch
            online_count_this_page = sum(1 for device in device_statuses if device.get('status') == 'online')
            online_devices_count += online_count_this_page

            # Check if we have reached the last page
            if len(device_statuses) < per_page:
                break

            page += 1

        # Prepare data for saving
        data = {
            'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'online_devices': online_devices_count
        }

        # Save to CSV
        with open('organization_device_data.csv', 'a', newline='') as csvfile:
            fieldnames = ['date', 'online_devices']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(data)

        # Save to JSON
        json_filename = 'organization_device_data.json'
        try:
            # Read existing data
            with open(json_filename, 'r') as jsonfile:
                data_list = json.load(jsonfile)
        except FileNotFoundError:
            # If file does not exist, start a new list
            data_list = []

        # Append new data
        data_list.append(data)

        # Write updated data back to file
        with open(json_filename, 'w') as jsonfile:
            json.dump(data_list, jsonfile, indent=4)

        print(f"Data saved on {data['date']}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    fetch_and_save_device_data()
