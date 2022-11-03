from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

chatbot = ChatBot('Charlie')

trainer = ListTrainer(chatbot)

trainer.train([
    "Hi, can I help you?",
    "Sure, I'd like to book a flight to Iceland.",
    "Your flight has been booked."
])

@app.route('/bot', methods=['POST'])
def bot():

    knownWords = {
        "hello": "Hello, how are you?",
        "good": "That's good!",
        "bad": "That's bad!",
        "bye": "Bye!",
        "thanks": "You're welcome!",
        "what can you do": "I'm a bot, I don't know much",
        "what are you doing": "I'm here to help you",
        "what are you doing?": "I'm here to help you",
        "how are you?": "Good, and you?",
        "how are you": "Good, and you?",
    }

    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    res = chatbot.get_response(incoming_msg)
    return str(res)
    
    for word in incoming_msg.split():
        if word in knownWords:
            msg.body(knownWords[word])
            responded = True
            break
    """
    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    """
    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    
    if not responded:
        msg.body('I only know about famous quotes and cats, sorry!')
    return str(resp)