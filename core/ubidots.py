import time
import requests
import math
import random
import os

EACH_REQUEST_DELAY = 10

class Ubidots:
    device_label :str

    since_last_request: float = 0.0
    token: str

    def __init__(self, device_label) -> None:
        self.token = os.getenv("UBIDOTS_TOKEN")
        self.device_label = device_label
        pass

    def post_request(self,payload):
        # Creates the headers for the HTTP requests
        url = "http://industrial.api.ubidots.com"
        url = "{}/api/v1.6/devices/{}".format(url, self.device_label)
        headers = {"X-Auth-Token": self.token, "Content-Type": "application/json"}

        # Makes the HTTP requests
        status = 400
        attempts = 0
        while status >= 400 and attempts <= 5:
            req = requests.post(url=url, headers=headers, json=payload)
            status = req.status_code
            attempts += 1
            time.sleep(1)

        # Processes results
        print(req.status_code, req.json())
        if status >= 400:
            print("[ERROR] Could not send data after 5 attempts, please check \
                your token credentials and internet connection")
            return False

        print("[INFO] request made properly, your device is updated")
        return True


    def request(self,value: dict[str, any], current_time: float):
        elasped_time_since_last_request = round(current_time - self.since_last_request) 

        if elasped_time_since_last_request > EACH_REQUEST_DELAY :
            self.since_last_request = current_time
            
            print("[INFO] Attemping to send data")
            print("[SENDED DATA] ", value)
            self.post_request(value)
            print("[INFO] finished")

        
