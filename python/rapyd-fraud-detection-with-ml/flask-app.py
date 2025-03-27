from flask import Flask, request, jsonify
import hmac
import hashlib
import base64
from utilities import make_request

app = Flask(__name__)

# Webhook handler
# Webhook received: {'id': 'wh_9b2f22855290da11d14cf19a042b0a5a', 'type': 'QUARANTINE_DECLINED', 'data': {'token': 'qm_84fb141090016196921ff60ece9b86d0', 'limits': None, 'reason': 'rapyd_protect', 'source': 'rapyd_protect', 'status': 'DEC', 'created_at': 1740830223, 'error_code': None, 'updated_at': 1740830223, 'action_type': 'create_payment', 'resolved_at': 0, 'target_tokens': ['payment_19ab7f7df9f818b320b5713f31e9d191'], 'action_flow_id': '1beb2ecc-ec53-4540-9f44-50fb8ee9bc6a', 'duplicated_action_flow_id': None}, 'trigger_operation_id': '90624b30-4adf-4ad9-ba0a-0fa9dee6d8a5', 'status': 'NEW', 'created_at': 1740830223, 'extended_timestamp': 1740830223510}

# Webhook received: {'id': 'wh_44cc5fa0ed8a5e62fab7c425ad09f370', 'type': 'QUARANTINE_DECLINED', 'data': {'token': 'qm_a0557bf7a130108812e9248d6f462bd4', 'limits': None, 'reason': 'rapyd_protect', 'source': 'rapyd_protect', 'status': 'DEC', 'created_at': 1740990176, 'error_code': None, 'updated_at': 1740990176, 'action_type': 'create_payment', 'resolved_at': 0, 'target_tokens': ['payment_e2919ace73cdc222ce72fbc959713fc1'], 'action_flow_id': '2cf4dd0f-ff73-46a9-98cb-b617075657d7', 'duplicated_action_flow_id': None}, 'trigger_operation_id': 'a65d36cc-637b-4ddb-b922-c89e87e22be6', 'status': 'NEW', 'created_at': 1740990176, 'extended_timestamp': 1740990176952}
# 127.0.0.1 - - [03/Mar/2025 13:52:57] "POST /webhook HTTP/1.1" 200 -

# use via ngrok
@app.route('/webhook', methods=['POST'])
def webhook():

    event = request.json
    print("Webhook received:", event)
    
    return jsonify({"status": "Webhook processed"})

if __name__ == '__main__':
    app.run(debug=True)
