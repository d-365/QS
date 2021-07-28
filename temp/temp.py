import requests
import json

url = "http://testdrktm.wanqiandaikuan.com/api/tmk/user/saveUser"

payload = json.dumps({
  "name": "dd",
  "phone": "11111111119",
  "account": "13642152858",
  "password": "fd8e1b2ec2f403c60d5085b62722b704",
  "status": True
})
headers = {
  'token': 'AUTH_TMK_6_fen_interface_9d380f4f0bcf44279c8707b38a331191',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

if __name__ == '__main__':

    print(response.text)