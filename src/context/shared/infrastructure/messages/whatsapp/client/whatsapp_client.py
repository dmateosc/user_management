from twilio.rest import Client
import os
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "your_account_sid")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "your_auth_token")
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

class WhatsappClient():
  def __init__(self, phone_number: str):
    self.phone_number = phone_number
    
  def send_message(self, message:str):
    client.messages.create(
      body=message.body,
      from_=TWILIO_WHATSAPP_NUMBER,
      to=f"whatsapp:{message.to}"
    )
  
  def cron(self):
    pass