from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv

app=Flask(__name__)

@app.route("/", methods=["POST"])
def sms_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("Hello! Thanks for texting me!")

    return str(resp)

if __name__ == "__main__":
    load_dotenv(override=True)
    app.run(debug=True)