from typing import Any, Dict
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import datetime
import logging
import json
import os
from dotenv import load_dotenv
import requests

# For reading the API key from the `.env` file
load_dotenv()

MAILGUN_API_URL = f"https://api.mailgun.net/v3/{os.getenv('MAILGUN_DOMAIN')}/messages"
FROM_EMAIL_ADDRESS = f"Your Shop<info@{os.getenv('MAILGUN_DOMAIN')}>"

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__, static_folder='images')
CORS(app)  # Enable CORS to allow requests from your frontend


@app.route('/abandoned-cart', methods=['GET', 'POST'])
def abandoned_cart():
    """
    Endpoint to receive abandoned cart data including user information.
    It sends email notification to the concerned user.
    """
    if request.method == "GET":
       return render_template('shopping_cart.html') # just show shopping cart for abandoned request
         
    try:
        # Get cart data from request
        cart_data = request.json
        
        # Extract user information
        user_info = cart_data.get('user', {})
        user_email = user_info.get('email', 'unknown')
        
        # Log the received data
        logger.info(f"Abandoned cart received from {user_email} at {datetime.datetime.now()}, Total items: {len(cart_data.get('items', []))}")
        
        # send email about the abandoned cart
        html_message = _generate_abandoned_cart_email(cart_data)
        _send_email(f"{user_info.get('name', user_email)} <{user_email}>", "Your cart is waiting...", html_message)
                
        # Return success response
        return jsonify({
            "status": "success",
            "message": f"Abandoned cart notification sent to: {user_info.get('email')}",
            "timestamp": datetime.datetime.now().isoformat(),
        }), 200
        
    except Exception as e:
        logger.error(f"Error processing abandoned cart: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500


def _send_email(to_address: str, subject: str, html_message: str):
    """
    Sends a single email to the given email address using Mailgun API.

    :param to_address:
    :param subject:
    :param message:
    """
    api_key = os.getenv("MAILGUN_API_KEY")  # Get API-Key from the `.env` file

    resp = requests.post(MAILGUN_API_URL, auth=("api", api_key),
                            data={"from": FROM_EMAIL_ADDRESS,
                                "to": to_address, "subject": subject, "html": html_message})
    if resp.status_code == 200:  # success
        logging.info(f"Successfully sent an email to '{to_address}' via Mailgun API.")
    else:   # error
        raise RuntimeError(f"Could not send the email, reason: {resp.text}")

# [url=https://postimg.cc/SYMFJZ3c][img]https://i.postimg.cc/SYMFJZ3c/bluetooth-speaker.jpg[/img][/url]

# [url=https://postimg.cc/2bJNjpcz][img]https://i.postimg.cc/2bJNjpcz/portable-charger.jpg[/img][/url]

# [url=https://postimg.cc/7bGys6hb][img]https://i.postimg.cc/7bGys6hb/smart-watch.jpg[/img][/url]

# [url=https://postimg.cc/wy3ddxkf][img]https://i.postimg.cc/wy3ddxkf/wireless-headphone.jpg[/img][/url]        

def _generate_abandoned_cart_email(cart_data: Dict[str, Any]) -> str:
    """
    Generate an HTML email for an abandoned cart using the provided cart data.
    
    Args: 
        cart_data: Dictionary containing cart information including user details and items
    
    Returns:
        HTML string for the email
    """
    try:
        # Extract data with error handling
        user_name = cart_data.get('user', {}).get('name', 'Valued Customer')
        first_name = user_name.split()[0] if ' ' in user_name else user_name
        items = cart_data.get('items', [])
        total_value = cart_data.get('totalValue', 0)
        
        # Format timestamp if available
        timestamp_str = cart_data.get('timestamp', '')
        abandonment_time = ''
        if timestamp_str:
            try:
                timestamp = datetime.datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
                abandonment_time = timestamp.strftime('%B %d at %I:%M %p')
                abandonment_time = f"on <b>{abandonment_time}</b>"
            except (ValueError, TypeError):
                abandonment_time = 'recently'
        else:
            abandonment_time = 'recently'
        
        # Generate the HTML content
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Your Cart Is Waiting!</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    color: #333333;
                    margin: 0;
                    padding: 0;
                }}
                .container {{
                    max-width: 600px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                .header {{
                    background-color: #0f2138;
                    color: white;
                    padding: 20px;
                    text-align: center;
                    border-radius: 5px 5px 0 0;
                }}
                .content {{
                    background-color: #ffffff;
                    padding: 20px;
                    border-left: 1px solid #dddddd;
                    border-right: 1px solid #dddddd;
                }}
                .footer {{
                    background-color: #f8f8f8;
                    padding: 15px;
                    text-align: center;
                    font-size: 12px;
                    color: #666666;
                    border-radius: 0 0 5px 5px;
                    border: 1px solid #dddddd;
                }}
                .button {{
                    display: inline-block;
                    background-color: #eb5454;
                    color: white!important;
                    padding: 12px 25px;
                    text-decoration: none;
                    border-radius: 4px;
                    font-weight: bold;
                    margin: 20px 0;
                }}
                .item {{
                    display: flex;
                    border-bottom: 1px solid #eeeeee;
                    padding: 15px 0;
                }}
                .item-image {{
                    width: 80px;
                    height: 80px;
                    background-color: #f1f1f1;
                    margin-right: 15px;
                    text-align: center;
                    line-height: 80px;
                }}
                .item-details {{
                    flex-grow: 1;
                }}
                .total {{
                    text-align: right;
                    font-weight: bold;
                    margin-top: 15px;
                    font-size: 18px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Your cart is waiting!</h1>
                </div>
                <div class="content">
                    <p>Hello {first_name},</p>
                    <p>We noticed you left some items in your cart {abandonment_time}. Don't worry, we've saved them for you!</p>
                    
                    <h2>Your Cart Items:</h2>
        """
        
        # Add each item to the email
        for item in items:
            item_name = item.get('name', 'Product')
            item_price = item.get('price', 0)
            item_quantity = item.get('quantity', 1)
            item_image = item.get('image', '')
            item_description = item.get('description', '')
            
            # Calculate subtotal for this item
            subtotal = item_price * item_quantity
            
            # Format image path with fallback
            image_tag = f'<img src="{item_image}" alt="{item_name}" style="max-width: 100%; max-height: 100%;">' if item_image else item_name[0].upper()
            
            html += f"""
                    <div class="item">
                        <div class="item-image">
                            {image_tag}
                        </div>
                        <div class="item-details">
                            <h3 style="margin: 0 0 5px 0;">{item_name}</h3>
                            <p style="margin: 0 0 5px 0; font-size: 14px;">{item_description}</p>
                            <p style="margin: 0; color: #666;">Quantity: {item_quantity}</p>
                            <p style="margin: 0; font-weight: bold;">${item_price:.2f}</p>
                        </div>
                    </div>
            """
        
        # Add total and call to action
        html += f"""
                    <div class="total">
                        Total: ${total_value:.2f}
                    </div>                    
                    <div style="text-align: center;">
                        <a href="#" class="button">Complete Your Purchase</a>
                    </div>                    

                    <p>If you have any questions about your order, please don't hesitate to contact our customer service team.</p>                    
                    <p>Thank you for shopping with us!</p>
                </div>
                <div class="footer">
                    <p>© 2025 Your Company Name. All rights reserved.</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        return html
    except Exception as e:
        # Return a simple fallback email if anything goes wrong
        return f"""
        <!DOCTYPE html>
        <html>
        <body>
            <h1>Your Cart Is Waiting!</h1>
            <p>Hello there,</p>
            <p>You have items waiting in your cart. Click below to complete your purchase!</p>
            <a href="#" class="button">Complete Your Purchase</a>
        </body>
        </html>
        """        

@app.route('/', methods=['GET'])
def shopping_cart():
    """Show the shopping cart"""
    return render_template('shopping_cart.html')

if __name__ == '__main__':
    logger.info("Starting Abandoned Cart Notification server...")
    app.run(port=5000, debug=True)
