import requests
import logging

import os
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)  # set log level
load_dotenv()  # for reading API key from `.env` file.

# Sandbox API URL format: https://api.mailgun.net/v3/sandbox<ID>.mailgun.org/messages
MAILGUN_API_URL = "https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages"
FROM_EMAIL_ADDRESS = "Sender Name <SENDER_EMAIL_ID>"    # your domain, or Mailgun sandbox


def _send_email(to_address: str, subject: str, message: str):
    """
    Send single email to the given email address using Mailgun API.

    :param to_address:
    :param subject:
    :param message:
    """
    try:
        api_key = os.getenv("MAILGUN_API_KEY")  # get API-Key from the `.env` file

        resp = requests.post(MAILGUN_API_URL, auth=("api", api_key),
                             data={"from": FROM_EMAIL_ADDRESS,
                                   "to": to_address, "subject": subject, "html": message})
        if resp.status_code == 200:  # success
            logging.info(f"Successfully sent an email to '{to_address}' via Mailgun API.")
        else:   # error
            logging.error(f"Could not send the email, reason: {resp.text}")

    except Exception as ex:
        logging.exception(f"Mailgun error: {ex}")


def _notify_registration(user_name: str, user_email: str):
    """
    Notify user on successful registration using `_send_email`

    :param user_name:
    :param user_email:
    """

    # Use your own formatted HTML message here, with an appropriate link
    registration_msg = f'Dear {user_name},<br/><br/> You have successfully registered on our site.'
    _send_email(user_email, "Registration successful", registration_msg)


def register_user(user_name: str, user_email: str):
    """
    Register the user and notify the user on successful registration.

    :param user_name:
    :param user_email:
    """

    # actual code to register the user

    logging.info(f"Sending registration email to the user: {user_name}...")
    _notify_registration(user_name, user_email)


def _notify_subscription(user_name: str, user_email: str):
    """
    Double opt-in confirmation for user subscription.

    :param user_name:
    :param user_email:
    """

    # Use your own formatted HTML message here, with an appropriate link
    subscription_msg = f'Dear {user_name},<br/><br/> Please confirm your subscription to our newsletter by clicking ' \
                       f'this link: <a href="https://example.com/confirm-subscription?id=abcdef1234567xyz">' \
                       f'https://example.com/confirm-subscription?id=abcdef1234567xyz</a>'

    _send_email(user_email, "Confirm subscription", subscription_msg)


def subscribe_user(user_name: str, user_email: str):
    """
    Subscribe user and send opt-in confirmation message.

    :param user_name:
    :param user_email:
    """

    # code to subscribe user with pending confirmation
    logging.info(f"Sending subscription confirmation email to the user: {user_name}...")
    _notify_subscription(user_name, user_email)


def _notify_password_reset(user_name: str, user_email: str):
    """
    Send password reset email to the user

    :param user_name:
    :param user_email:
    """

    # Use your own formatted HTML message here
    registration_msg = f'Dear {user_name},<br/><br/> Please use the following link to reset your password: ' \
                       f'<a href="https://example.com/password-reset?token=lmnopqr7654321abc">' \
                       f'https://example.com/password-reset?token=lmnopqr7654321abc</a>'

    _send_email(user_email, "Reset password", registration_msg)


def reset_user_password(user_name: str, user_email: str):
    """
    Initiate password-reset and notify user

    :param user_name:
    :param user_email:
    """

    # Password reset code for the user
    logging.info(f"Sending password reset email to the user: {user_name}...")
    _notify_password_reset(user_name, user_email)


# Demo of automated transactional emails
if __name__ == "__main__":
    register_user("Kirstin",  "Kirstin <kirstin@example.com>")
    subscribe_user("Jakkie",  "Jakkie <jakkie@example.com>")
    reset_user_password("Manish",  "Manish <manish@example.com>")


########################### OUTPUT ###########################
# $ python main.py
# INFO:root:Successfully sent an email to 'Kirstin <kirstin@example.com>' via Mailgun API.
# INFO:root:Registration email sent to the user: Kirstin.
# INFO:root:Successfully sent an email to 'Jakkie <jakkie@example.com>' via Mailgun API.
# INFO:root:Subscription confirmation email sent to the user: Jakkie.
# INFO:root:Successfully sent an email to 'Manish <manish@example.com>' via Mailgun API.
# INFO:root:Password reset email sent to the user: Manish.
# $
########################### OUTPUT ###########################