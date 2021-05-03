from flask import Flask, request
from webexteamssdk import WebexTeamsAPI, Webhook
from cardcontent import *
from newcard import *
import smartsheet

app = Flask(__name__)

#The access token should go in an environment variable.
api = WebexTeamsAPI(access_token="NjhiZGM5YmQtNTMzNC00YWExLWFiYzktNTkzNDg3ZGU0MTI4OGU5NjI1NWQtZTBl_PF84_consumer")

@app.route('/', methods=['POST', 'GET'])
def home():
    return 'OK', 200


@app.route('/webhookreq', methods=['POST'])
def webhookreq():

    if request.method == 'POST':
        req = request.get_json()

        #iD = req.get("id")
        #name = req.get("name")
        #resource = req.get("resource")
        #event = req.get("event")
        #filter = req.get("filter")
        #orgId = req.get("orgId")
        #createdBy = req.get("createdBy")
        #appId = req.get("appId")
        #ownedBy = req.get("ownedBy")
        #status = req.get("status")
        #actorId = req.get("actorId")
        #data_id = req['data']['id']
        data_roomId = req['data']['roomId'] #Yyou need this one.
        data_personId = req['data']['personId'] # And you'll need this one, too.
       #data_personEmail = req['data']['personEmail']
       #data_created = req['data']['created']
        
        #Loop prevention VERY IMPORTNAT!
        me = api.people.me()
        if data_personId == me.id:
            return 'OK', 200
                                    # Y2lzY29zcGFyazovL3VzL1JPT00vM2I1MmE1NDAtM2U3MS0xMWVhLThkYWYtMDk1M2EyYTRhYTQ2
        else:
            if api.messages.create(roomId=data_roomId, text='Blah...', attachments=[{"contentType": "application/vnd.microsoft.card.adaptive", "content": newCard}]):
                return "OK"


    elif request.method == 'GET':
        return "Yes, this is working."

@app.route('/cardsubmitted', methods=['POST'])
def cardsubmitted():
    if request.method == 'POST':
        req = request.get_json()

        #iD = req.get("id")
        #name = req.get("name")
        #resource = req.get("resource")
        #event = req.get("event")
        #orgId = req.get("orgId")
        #appId = req.get("appId")
        #ownedBy = req.get("ownedBy")
        #status = req.get("status")
        #actorId = req.get("actorId")
        data_id = req['data']['id']
        #data_type = req['data']['type']
        #data_messageId = req['data']['messageId']
        #data_personId = req['data']['personId']
        #data_roomId = req['data']['roomId']
        #data_created = req['data']['created']
      
        attachment_actions = api.attachment_actions.get(data_id)
        inputs = attachment_actions.inputs
        
        myName = inputs['myName']
        myEmail = inputs['myEmail']
        myTel = inputs['myTel']
        
        print(myName)
        print(myEmail)
        print(myTel)

        smart = smartsheet.Smartsheet('sh22dq152173x0fxccwym76wyx') #Smartsheet API Key
        smart.errors_as_exceptions(True)

        # Specify cell values for the added row                         
        newRow = smartsheet.models.Row()
        newRow.to_top = True
                                                                                                # So the above variables are the incoming JSON
        newRow.cells.append({ 'column_id': 1843593802475396, 'value': myName })                   # Then we take those variables, and use them 
        newRow.cells.append({ 'column_id': 6347193429845892, 'value': myEmail, 'strict': False })   # as the values that should be added to the 
        newRow.cells.append({ 'column_id': 4095393616160644, 'value': myTel, 'strict': False }) # Smartsheet via the Smartsheet API
        #You'll have to retrieve the column IDs above by making a GET request to smart sheet via Postman
        #Send to https://api.smartsheet.com/2.0/sheets/{sheetID}. Dont' forget your Baerer token.
        #The values (mail, url, etc) are merely the variables created above from the incoming json.
        #Don't know why strict is used in all instances except the first.

        # Add rows to sheet
        response = smart.Sheets.add_rows(4356261866170244, newRow)
        # The number above -- 4356261866170244 -- is the sheet ID.

        return 'OK', 200

if __name__=='__main__':
    app.run(debug=True)


# ngrok
# ngrok http 5000