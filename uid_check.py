import requests

uid = input("Enter UID: ")

url = "https://shop.garena.sg/api/auth/player_id_login"
payload = {"account_id": uid, "app_id": 100067}

res = requests.post(url, json=payload)
data = res.json()

if "nickname" in data:
    print(f"Nickname: {data['nickname']}")
    print(f"Region: {data['region']}")
else:
    print("Invalid UID or API Error:", data)
