from flask import Flask, request, render_template
from bson.json_util import dumps
import pymongo
from pymongo import MongoClient
from flask_pymongo import PyMongo

app = Flask(__name__)
# mongo = MongoClient('mongodb://trial2:seproj1@:/')
mongo = MongoClient("ds243518.mlab.com", 43518)
db = mongo['blood_data']
db.authenticate('trial2', 'seproj1')

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('homepage.html')

@app.route('/about_us', methods=['GET'])
def about_us():
    if request.method == 'GET':
        return render_template('about_us.html')

@app.route('/contact_us', methods=['GET'])
def contact_us():
    if request.method == 'GET':
        return render_template('contact_us.html')

@app.route('/blood_bank', methods=['GET','POST'])
def blood_bank():
    if request.method == 'GET':
        return render_template('blood_bank.html')
    if request.method == 'POST':
        bg = request.form['blood_group']
        if bg in ['A+','A-','O+','O-','B+','B-','AB+','AB-','a+','a-','o+','o-','b+','b-','ab+','ab-'] :
            op = db.blood_bank.find({bg:{"$gt":0}},{"_id":0}).sort(bg,pymongo.DESCENDING)

            return render_template('q_out.html',bg = bg,data=dumps(op))
        else :
            pass
if __name__ == '__main__':
 app.run(host='0.0.0.0', debug=True)
