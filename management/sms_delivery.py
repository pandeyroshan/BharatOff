import requests


def send_username_password(name, phone_number, username, password):
    # DLT Template ID - 1207162626916190672 i.e. Credentials Template
    URL = "http://sms.codicians.in/api/sendhttp.php?authkey=7322A5kha4jntu5ff1a099P6&mobiles={0}&message={1}&sender=BHROFF&route=4&country=91&DLT_TE_ID=1207162626916190672&response=json".format(phone_number, "Hello {0}, thank you for taking up the services of BharatOff. Below are your login details - %0A%0AUsername - {1}%0APassword - {2}%0A%0ARegards, %0ABharatOff".format(name, username, password))

    response = requests.get(URL)

    print(response)

def send_invoice_details(name, phone_number, invoice_number, package_amount):
    # DLT Template ID - 1207162626900102977 i.e. Invoice Template
    URL = "http://sms.codicians.in/api/sendhttp.php?authkey=7322A5kha4jntu5ff1a099P6&mobiles={0}&message={1}&sender=BHROFF&route=4&country=91&DLT_TE_ID=1207162626900102977&response=json".format(phone_number, "Hello {0}, thank you for taking up the services of BharatOff. Below are your purchase details -%0A%0AInvoice No - {1}%0ATotal Paid - {2} INR%0A%0AYou will receive a detailed mail of your transaction soon.%0A%0ARegards, %0ABharatOff".format(name, invoice_number, package_amount))

    response = requests.get(URL)

    print(response)

def send_enquiry_text(shopkeeper_name,shopkeeper_phone_number, customer_phone_number):
    # DLT Template ID - 1207163854045918561
    URL = "http://sms.codicians.in/api/sendhttp.php?authkey=7322A5kha4jntu5ff1a099P6&mobiles={0}&message={1}&sender=BHROFF&route=4&country=91&DLT_TE_ID=1207163854045918561&response=json".format(shopkeeper_phone_number, "Hi {0},%0ASomeone with {1} enquired about your shop and products in BharatOff App.%0A%0ATeam,%0ABharatOff".format(shopkeeper_name, customer_phone_number))
    response = requests.get(URL)

    print(response.text)


if __name__ == '__main__':
    # send_username_password("Roshan Pandey", "7440804918", "roshan", "Linux@123")
    # send_invoice_details("Roshan Pandey", "9752315423", "IN20210716001", "199")
    send_enquiry_text("Simran Manjhi", "7903820334", "9752315423")