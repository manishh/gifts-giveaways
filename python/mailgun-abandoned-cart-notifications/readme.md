# Mailgun Abandoned Cart Notifications

**Author:** [Manish Hatwalne](https://www.mailgun.com/blog/author/manish-hatwalne/)

This project demonstrates how to implement an abandoned cart email workflow using Mailgun. It includes a Flask-based backend that processes abandoned cart data, generates HTML email templates, and sends notification emails via the Mailgun API.

![Mailgun: Trigger Abandoned Cart](https://i.imgur.com/Qos5lQa.png)

## Prerequisites

1. A **Mailgun account** to send emails via Mailgun's API. If you don't have an account, follow this [quick start guide](https://documentation.mailgun.com/docs/mailgun/quickstart-guide/quickstart/) to set one up for free.

2. **Python 3.8** or higher installed on your machine.

3. Familiarity with **HTML** and **JavaScript** to understand the UI code.

## Setup Instructions

1. **Clone the Repository**  
   
   ```bash
   git clone https://github.com/manishh/gifts-giveaways.git
   cd gifts-giveaways/python/mailgun-abandoned-cart-notifications
   ```

2. **Install Dependencies**

   ```bash 
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**

    Rename `.env.example` file as `.env` and update following variables:

    ```python
    MAILGUN_API_KEY=your-mailgun-api-key
    MAILGUN_DOMAIN=your-mailgun-domain
    ```
4. **Run the Flask Server**

   ```bash 
   python app.py
   ```

5. **Test the Workflow**

    - Open the UI in a browser: http://localhost:5000
    - Add items to the cart and wait for the abandoned cart timeout.
    - Check the terminal logs for email delivery status.
    - Verify the abandoned cart email in the recipient’s inbox.

## Monitoring Emails

To track email delivery, open rates, and failures, go to Mailgun **Dashboard → Reporting → Metrics.**

---

