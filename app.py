import profile
from xml.dom.minidom import Document
from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/notbot"
mongo = PyMongo(app)
db = mongo.db




doc_url = 'https://shrikrushnazirape.s3.amazonaws.com/te-min-compressed.pdf'



@app.route("/")
def hello():
    return "Hello, This is testing of Notbot!"





@app.route('/bot', methods=['POST'])
def bot():

    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    profile_name = request.values.get('ProfileName', '')
    profile_wid = request.values.get('WaId', '')
    from_msg = request.values.get('From', '')
    to_msg = request.values.get('To', '')
    sent_msg = request.values.get('Body', '')
    status = request.values.get('MessageStatus', '')


    db.notbot.insert_one({
        'Profile Name ': profile_name,
        'profile_wid' : profile_wid,
        'from': from_msg,
        'to': to_msg,
        'sent msg' : sent_msg,
        

    })

    if incoming_msg == '1':
        msg.body('Hey there, again from Notbot')
        responded = True


    if incoming_msg == '2':
        msg.media('https://picsum.photos/200')
        responded = True
    
    
    if incoming_msg == '3':
       
        msg.media(doc_url)
        responded = True
    

    if incoming_msg == '4':
        msg.body('1. Send Message\n2. Send Image\n3. Send Document\n4. Send List\n5. Send My Name')
        responded = True

    if incoming_msg == '5':
        msg.body("Your Name is : "+profile_name)
        responded = True

    if not responded:
        
        msg.body('Hey, Notbot here !!\nPlease choose from below options : \n1. Send Message\n2. Send Image\n3. Send Document\n4. Send List\n5. Send My Name')
    
  

    return str(resp)


if __name__ == '__main__':
    app.run(debug=True)
