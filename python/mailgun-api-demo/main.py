import json
import requests
import logging

import os
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)  # set log level
load_dotenv()  # for reading API key from `.env` file.

MAILGUN_API_URL = "https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages"
FROM_EMAIL_ADDRESS = "Sender Name <SENDER_EMAIL_ID>"    # your domain, or Mailgun sandbox


def send_email_with_attachment(to_address: str, subject: str, message: str):
    try:
        api_key = os.getenv("MAILGUN_API_KEY")  # get API-Key from the `.env` file

        files = {'attachment': open('./cover-letter.txt', 'rb')}   # file you want to attach
        # files = {'inline': open('./zen-attachment.jpg', 'rb')}   # file you want to attach

        resp = requests.post(MAILGUN_API_URL, auth=("api", api_key), files=files,
                             data={"from": FROM_EMAIL_ADDRESS,
                                   "to": to_address, "subject": subject, "html": message})
        if resp.status_code == 200:  # success
            logging.info(f"Successfully sent an email to '{to_address}' via Mailgun API.")
        else:   # error
            logging.error(f"Could not send the email, reason: {resp.text}")

    except Exception as ex:
        logging.exception(f"Mailgun error: {ex}")


def send_single_email(to_address: str, subject: str, message: str):
    try:
        api_key = os.getenv("MAILGUN_API_KEY")  # get API-Key from the `.env` file

        resp = requests.post(MAILGUN_API_URL, auth=("api", api_key),
                     data={"from": FROM_EMAIL_ADDRESS,
                           "to": to_address, "subject": subject, "text": message})
        if resp.status_code == 200:  # success
            logging.info(f"Successfully sent an email to '{to_address}' via Mailgun API.")
        else:   # error
            logging.error(f"Could not send the email, reason: {resp.text}")

    except Exception as ex:
        logging.exception(f"Mailgun error: {ex}")


def send_batch_emails(recipients: dict, subject: str, message: str):
    try:
        api_key = os.getenv("MAILGUN_API_KEY")  # get API-Key from the `.env` file

        to_address = list(recipients.keys())  # get only email addresses
        recipients_json = json.dumps(recipients)

        logging.info(f"Sending email to {len(to_address)} IDs...")
        resp = requests.post(MAILGUN_API_URL, auth=("api", api_key),
                             data={"from": FROM_EMAIL_ADDRESS,
                                   "to": to_address, "subject": subject, "text": message,
                                   "recipient-variables": recipients_json})
        if resp.status_code == 200:  # success
            logging.info(f"Successfully sent email to {len(recipients)} recipients via Mailgun API.")
        else:   # error
            logging.error(f"Could not send emails, reason: {resp.text}")
    except Exception as ex:
        logging.exception(f"Mailgun error: {ex}")


if __name__ == "__main__":
    # send_single_email("Manish <manish@exanple.com>", "Single email test", "Testing Mailgun API for a single email")
    # send_email_with_attachment("Manish Attached <manish@exanple.com>", "Attachment test", "<h2>Testing Mailgun API email attachment</h2>")

    _recipients = {"manish@example.com": {"name": "Manish", "id": 1},
                   "jakkie@example.com": {"name": "Jakkie", "id": 2},
                   "elzet@example.com": {"name": "Elzet", "id": 3}}

    send_batch_emails(_recipients, "Hi, %recipient.name%!", "Testing Mailgun API. This email is sent via Mailgun API.")
