from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask,json,jsonify,render_template,request

app = Flask(__name__)
client = MongoClient('localhost:27017')
db = client.contactlist

# Routing to index page
@app.route('/')
def index():
	return render_template('index.html')

# Handles the display request by fetching all data from database
@app.route('/showContact', methods=['POST'])
def showContact():
	try:
		contacts = db.contactlist.find()
		contactList = []
		for contact in contacts:
			contactItem = {
				'name': contact['name'],
				'email': contact['email'],
				'number': contact['number'],
				'_id': str(contact['_id'])
			}
			contactList.append(contactItem)
	except Exception,err:
		return str(err)
	return json.dumps(contactList)

# Adding a data passed from html side into the database
@app.route("/addContact",methods=['POST'])
def addContact():
    try:
        json_data = request.json['contact']
        name = json_data['name']
        email = json_data['email']
        number = json_data['number']

        db.contactlist.insert_one({
            'name':name, 'email':email, 'number':number
            })
        return jsonify(status='OK',message='inserted successfully')

    except Exception,e:
        return jsonify(status='ERROR',message=str(e))

# Removing data from database
@app.route("/deleteContact",methods=['POST'])
def deleteContact():
    try:
        id = request.json['id']
        print id
        db.contactlist.remove({'_id':ObjectId(id)})
        return jsonify(status='OK',message='deletion successful')
    except Exception, e:
        return jsonify(status='ERROR',message=str(e))

# Editing a data
@app.route('/editContact',methods=['POST'])
def editContact():
    try:
        id = request.json['id']
        x = db.contactlist.find_one({'_id':ObjectId(id)})
        contact = {
                'name':x['name'],
                'email':x['email'],
                'number':x['number'],
                'id':str(x['_id'])
                }
        return json.dumps(contact)
    except Exception, e:
        return str(e)

# Update an existing data
@app.route("/updateContact", methods=['POST'])
def updateContact():
	try:
		json_data = request.json['contact']
		id = json_data['id']
		name = json_data['name']
		email = json_data['email']
		number = json_data['number']
		db.contactlist.update_one({'_id':ObjectId(id)}, {'$set':{'name':name, 'email':email, 'number':number}})
		return jsonify(status='OK', message='Updated successfully')
	except Exception, e:
		return jsonify(status='ERROR',message=str(e))

if __name__ == "__main__":
    app.run()
		