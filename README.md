# gve_devnet_meraki_device_status_tracker
This Python script is designed to periodically track and record the status of devices in a Cisco Meraki organization. It fetches the number of online devices in the organization and saves this data to both CSV and JSON files.


## Contacts
* Jorge Banegas

## Solution Components
* Meraki

## Prerequisites
#### Meraki API Keys
In order to use the Meraki API, you need to enable the API for your organization first. After enabling API access, you can generate an API key. Follow these instructions to enable API access and generate an API key:
1. Login to the Meraki dashboard
2. In the left-hand menu, navigate to `Organization > Settings > Dashboard API access`
3. Click on `Enable access to the Cisco Meraki Dashboard API`
4. Go to `My Profile > API access`
5. Under API access, click on `Generate API key`
6. Save the API key in a safe place. The API key will only be shown once for security purposes, so it is very important to take note of the key then. In case you lose the key, then you have to revoke the key and a generate a new key. Moreover, there is a limit of only two API keys per profile.

> For more information on how to generate an API key, please click [here](https://developer.cisco.com/meraki/api-v1/#!authorization/authorization). 

> Note: You can add your account as Full Organization Admin to your organizations by following the instructions [here](https://documentation.meraki.com/General_Administration/Managing_Dashboard_Access/Managing_Dashboard_Administrators_and_Permissions).

## Installation/Configuration
1. Clone this repository with `git clone [repository name]`.
2. In the cloned repository, you'll find a `.env` file. Open this file and fill in your Meraki API key and Organization ID:
   ```bash
   MERAKI_API_KEY=your_api_key_here
   MERAKI_ORG_ID=your_organization_id_here
   ```
   Remember to keep your API key confidential and ensure not to commit or share your `.env` file with others.

   If you do not know your Meraki ORG ID you can run the script meraki_orgs.py to it will print out all the organizations associated with the MERAKI_API_KEY provided. 

3. Set up a Python virtual environment. Ensure Python 3 is installed in your environment. If not, download Python [here](https://www.python.org/downloads/). Activate the virtual environment following the instructions found [here](https://docs.python.org/3/tutorial/venv.html).
4. Install the required packages with `pip3 install -r requirements.txt`.

## Usage
- **Scheduled Script (`meraki_device_tracker.py`)**: Runs automatically at specified intervals. Modify `SCHEDULE_INTERVAL` and `SCHEDULE_UNIT` in the script to adjust the frequency.
- **Manual Script (`meraki_device_tracker_manual.py`)**: For manual execution.

To run the script, use the command:
```bash
$ python3 meraki_device_tracker.py  # For the scheduled script
$ python3 meraki_device_tracker_manual.py  # For the manual 
```

# Screenshots

![/IMAGES/0image.png](/IMAGES/output.png)

![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.