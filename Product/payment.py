import requests
# from apiCore.apiCore.agentsModel import WebTransactions, Users

DOMAIN_NAME = ""
class ZarinRest:
    def __init__(self, merchant_id: str = None, user_id: str = None, mode: str = 'main'):
        self.merchant_id = merchant_id
        self.callback_url = f'http://{DOMAIN_NAME}/api/v1/zarinpal/{user_id}'
        self.mode = mode
    def _send_request(self, url, data):
        response = requests.post(
            url=url,
            data={
                'merchant_id': self.merchant_id,
                'callback_url': self.callback_url,
                **data
            }
        )
        return response.json()

    def payment_request(self, amount, description, mobile=None, email=None):
        if self.mode == 'sandbox':  
            url = 'https://sandbox.zarinpal.com/pg/v4/payment/request.json'
        else:
            url = 'https://api.zarinpal.com/pg/v4/payment/request.json'
        data = {
            'amount': amount,
            'description': description,
            'mobile': mobile,
            'email': email,
        }
        return self._send_request(url=url, data=data)

    def verify_payment(self, amount, authority):
        if self.mode == 'sandbox':
            url = 'https://sandbox.zarinpal.com/pg/v4/payment/verify.json'
        else:
            url = 'https://api.zarinpal.com/pg/v4/payment/verify.json'
        data = {
            'amount': amount,
            'authority': authority
        }
        return self._send_request(url=url, data=data)
