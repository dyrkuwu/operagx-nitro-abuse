import json
import requests
import uuid
import re

PROMOTION_ID = "1180231712274387115"
DISCORD_BASE_URL = "https://discord.com/billing/partner-promotions"
DISCORD_API_URL = "https://api.discord.gx.games/v1/direct-fulfillment"

def claim_rewards():
    t = generate_uuid()
    generate_and_show_promo_url(t)

def generate_and_show_promo_url(t):
    print(f"{DISCORD_BASE_URL}/{PROMOTION_ID}/{init_request_to_discord(t)['token']}")

def init_request_to_discord(user_id):
    data = {
        "partnerUserId": user_id
    }
    try:
        response = requests.post(
            DISCORD_API_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data)
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(e)

def generate_uuid():
    uuid_format = "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx"
        
    def replace_x(match):
        return str(uuid.uuid4().hex[:1])

    def replace_y(match):
        return str(8 + int(uuid.uuid4().hex[:1], 16) % 4)

    uuid_value = uuid_format
    uuid_value = re.sub('x', replace_x, uuid_value)
    uuid_value = re.sub('y', replace_y, uuid_value)

    return uuid_value

user_id = "operagxsucks"
claim_rewards()