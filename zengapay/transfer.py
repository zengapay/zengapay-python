from .client import ZengaPayAPI
from .utils import validate_number, validate_phone_number, validate_string
import json


class Transfers(ZengaPayAPI):
    def transfer(self, payload):
        payload["msisdn"] = validate_phone_number(payload.get("msisdn"))
        payload["amount"] = validate_number(payload.get("amount"))
        payload["external_reference"] = validate_string(
            payload.get("external_reference")
        )
        payload["narration"] = validate_string(payload.get("narration"))
        
        # Add `use_contact` field since it is now required according to the API
        # https://developers.zengapay.com/#the-transfer-request-object
        if payload["use_contact"] is None:
            raise Exception("`use_contact` field is required")
        elif payload["use_contact"] == True:
            if payload["contact_id"] is None:
                raise Exception("`contact_id` field is required when `use_contact` is True")
        
        json_payload = json.dumps(payload)

        url = f"{self.config.base_url}/transfers"
        res = self.request("POST", url, post_data=json_payload)

        return res.json()

    def get_all_transfers(self, url=None):
        if url is None:
            url = f"{self.config.base_url}/transfers"
        res = self.request("GET", url)

        return res.json()

    def get_transfer(self, transaction_ref):
        url = f"{self.config.base_url}/transfers/{validate_string(transaction_ref)}"
        res = self.request("GET", url)

        return res.json()

    def get_transaction_status(self, transaction_ref):
        url = f"{self.config.base_url}/transfers/{validate_string(transaction_ref)}"
        res = self.request("GET", url)

        return res.json()["data"]["transactionStatus"]
