import requests
import json

Authorization = "key=AAAAIhcBOLY:APA91bH4aaTqjxCtKJUslhqqC7kwXuHkJCUBVdsc9GFSlPPZ1QZx-duLnL8vgNVjO0djsCTkJDeceGOj3R2W0hVJq6RQfSYSEAoqe9jP7XwZDlnA__A7Fp5l-HjGByWcy6awNy1Of0eM"

def send_fcm_notification(device_id, shop_name, notification_text):
    URL = "https://fcm.googleapis.com/fcm/send"

    header = {
        "Content-Type" : "application/json",
        "Authorization" : Authorization
    }

    context = {
        "to" : device_id,
        "notification" : {
            "title" : shop_name,
            "body" : notification_text
        }
    }
    response = requests.post(url = URL, headers=header, data = json.dumps(context))
    print(response.text)

if __name__ == "__main__":
    device_id = "f_AK6TEOSFGhhwnu6ru2q7:APA91bGhTHx4hJ7wYocyr_S0MPeXdVt6z-ECWaenrU6QoWjNW4IvAiJgl1j1QR47QLlucZ9VZ25MpRxtt2jNsG-9Z-JX_tZfoGp4Mpmq6ynxKqt10IQaljgTL2RuwqG0wukfOu5Ow68P"
    shop_name = "ABC Shop"
    notification_text = "Get 100% off on our shop"
    send_fcm_notification(device_id, shop_name, notification_text)