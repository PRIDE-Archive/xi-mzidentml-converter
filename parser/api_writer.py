import traceback
import requests

from config_parser import get_api_configs
from parser.writer import Writer


class APIWriter(Writer):
    """Class for writing results to a relational database."""

    def __init__(self, connection_str, user_id=None, upload_id=None, pxid=None):
        self.pxid = pxid
        self.upload_id = upload_id
        configs = get_api_configs()
        self.base_url = configs['base_url']
        self.api_key = configs['api_key']
        self.api_key_value = configs['api_key_value']

    def write_data(self, table, data):
        try:
            API_ENDPOINT = self.base_url+ "/write_data"
            API_KEY_VALUE =  self.api_key_value
            API_KEY =  self.api_key
            headers = {'Content-Type': 'application/json', API_KEY: API_KEY_VALUE}
            payload = {
                "table": table,
                "data": data,
            }
            response = requests.post(url=API_ENDPOINT, headers=headers, json=payload)
            response.raise_for_status()

            # Check the response status code and handle it as needed
            if response.status_code == 200:
                print("Request successful")
            else:
                print(f"Unexpected status code: {response.status_code}")
        except Exception as e:
            print(f"Caught an exception: {e}")
            print(payload)
            traceback.print_exc()
        return response.json()


    def write_new_upload(self, table, data):

        try:
            API_ENDPOINT = self.base_url + "/write_new_upload"
            API_KEY_VALUE = self.api_key_value
            API_KEY = self.api_key
            headers = {'Content-Type': 'application/json', API_KEY: API_KEY_VALUE}
            payload = {
                "table": table,
                "data": data,
            }
            response = requests.post(url=API_ENDPOINT, headers=headers, json=payload)
            response.raise_for_status()

            # Check the response status code and handle it as needed
            if response.status_code == 200:
                print("Request successful")
            else:
                print(f"Unexpected status code: {response.status_code}")
            print(response.json())
        except Exception as e:
            print(f"Caught an exception: {e}")
            traceback.print_exc()
        return response.json()

    def write_mzid_info(self, analysis_software_list, spectra_formats,
                        provider, audits, samples, bib, upload_id):
        try:
            API_ENDPOINT = self.base_url + "/write_mzid_info?upload_id="+str(upload_id)
            API_KEY_VALUE = self.api_key_value
            API_KEY = self.api_key
            headers = {'Content-Type': 'application/json', API_KEY: API_KEY_VALUE}
            payload = {
                "analysis_software_list": analysis_software_list,
                "spectra_formats": spectra_formats,
                "provider": provider,
                "audits": audits,
                "samples": samples,
                "bib": bib,
            }
            response = requests.post(url=API_ENDPOINT, headers=headers, json=payload)
            response.raise_for_status()

            # Check the response status code and handle it as needed
            if response.status_code == 200:
                print("Request successful")
                print(response.json())
            else:
                print(f"Unexpected status code: {response.status_code}")

            print(response.json())
        except Exception as e:
            print(f"Caught an exception: {e}")
            traceback.print_exc()
        return response.json()


    def write_other_info(self, contains_crosslinks, upload_warnings, upload_id):
        try:
            API_ENDPOINT = "/write_other_info?upload_id="+str(upload_id)
            API_KEY_VALUE = self.api_key_value
            API_KEY = self.api_key
            headers = {'Content-Type': 'application/json', API_KEY: API_KEY_VALUE}
            payload = {
                "contains_crosslinks": contains_crosslinks,
                "upload_warnings": upload_warnings,
            }
            response = requests.post(url=API_ENDPOINT, headers=headers, json=payload)
            response.raise_for_status()

            # Check the response status code and handle it as needed
            if response.status_code == 200:
                print("Request successful")
                print(response.json())
            else:
                print(f"Unexpected status code: {response.status_code}")

            print(response.json())
        except Exception as e:
            print(f"Caught an exception: {e}")
            traceback.print_exc()
        return response.json()

    def fill_in_missing_scores(self):
        """
        ToDo: this needs to be adapted to sqlalchemy from old SQLite version
        """
        pass