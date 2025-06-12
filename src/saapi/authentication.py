import time
import hashlib


class Authentication:
    def __init__(self, app_id: str, secret: str):
        self.app_id = app_id
        self.secret = secret

    def get_headers(self, payload):
        timestamp = int(time.time())
        sign_factor = f"{self.app_id}{timestamp}{payload}{self.secret}"
        signature = hashlib.sha256(sign_factor.encode()).hexdigest()
        auth = "SHA256 Credential={0}, Timestamp={1}, Signature={2}".format(
            self.app_id,
            timestamp,
            signature
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": auth
        }
        return headers
