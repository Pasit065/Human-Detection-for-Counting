
import requests

class LineNotifyService():
    def __init__(self):
            self.sent_line_message = ""

    def set_sent_line_message_and_status(self, message):
        self.sent_line_message = message

    def reset_sent_line_message(self):
        self.sent_line_message = ""

    def sheety_quota_out_notificate(self, line_notify_token):
        token = line_notify_token
                
        headers = {
            "Authorization": f"Bearer {token}"
        }

        json_params = {
            "message":"Your package quota for sheety api is out now, please upgrade your sheety api for updating data in real time."
        }
                
        return requests.post(url = "https://notify-api.line.me/api/notify", params = json_params, headers = headers)
         

    def sending_message(self, tokens_list, image_path):
        for token in tokens_list:
            headers = {
            "Authorization":f"Bearer {token}"
            }

            json_params = {
            "message":self.sent_line_message
            }

            file_params = {
                "imageFile":open(image_path, "rb")
            }
                
            response = requests.post(url = "https://notify-api.line.me/api/notify", params = json_params, headers = headers, files = file_params)
            response.raise_for_status()
            print("message has been sends.")