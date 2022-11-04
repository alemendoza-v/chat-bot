from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

def getCat(msg):
    return msg.media('https://cataas.com/cat')

@app.route('/bot', methods=['POST'])
def bot():
    memes = {
        "mercy": "Heroes never die!",
        "sigma": "Im literally sigma, What is this melody?",
        "reinhardt": "Hammer down!",
        "dva": "Nerf this!",
        "genji": "龍神の刃を取れ！",
    }

    knownWords = {
        "hello": "Hello, how are you?",
        "good": "That's good!",
        "bad": "That's bad!",
        "bye": "Bye!",
        "thanks": "You're welcome!",
        "what can you do": "I'm a bot, I don't know much",
        "what can you do?": "I'm a bot, I don't know much",
        "what are you doing": "I'm here to help you",
        "what are you doing?": "I'm here to help you",
        "how are you?": "Good, and you?",
        "how are you": "Good, and you?",
    }

    palabrasConocidas = {
        "hola": "Hola, como estas?",
        "bien": "Que bueno!",
        "mal": "Que mal!",
        "adios": "Adios!",
        "gracias": "De nada!",
        "que sabes hacer": "Soy un bot, no se mucho",
        "que sabes hacer?": "Soy un bot, no se mucho",
        "que haces": "Estoy aqui para ayudarte",
        "que haces?": "Estoy aqui para ayudarte",
        "como estas?": "Bien, y tu?",
        "como estas": "Bien, y tu?",
    }

    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    
    if incoming_msg in knownWords:
        msg.body(knownWords[incoming_msg])
        responded = True

    elif incoming_msg in palabrasConocidas:
        msg.body(palabrasConocidas[incoming_msg])
        responded = True 

    elif incoming_msg in memes:
        msg.body(memes[incoming_msg])
        responded = True

    if 'cat' in incoming_msg or 'gato' in incoming_msg or 'kitty' in incoming_msg or 'gatito' in incoming_msg:
        # return a cat pic
        getCat(msg)
        responded = True
    
    if not responded:
        msg.media(incoming_msg)
        # msg.body('No se como responder eso, pero aqui esta un gato | I don\'t know how to respond to that, but here\'s a cat')
        # getCat(msg)

    return str(resp)