from flask import Flask
from flask import request
from flask import jsonify
from datetime import datetime, timedelta
from flask_cors import CORS, cross_origin
import flask_back.DB.parser  
from bson.json_util import loads, dumps
from bson.raw_bson import RawBSONDocument
import bson
import bsonjs
from flask_back.DB.habits import Habits

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)


@app.route('/')
def index():
    return '''<div>Hey</div>'''


@app.route('/authorization')
@cross_origin(origin='*')
def authorization(): 
    return jsonify(str(flask_back.DB.parser.get_person_id(request.args.get('login'),request.args.get('password'))))

@app.route('/get_person_data')
@cross_origin(origin='*')
def get_data(): 
    habits = (flask_back.DB.parser.get_person_data(request.args.get('_id')))
    json_record2 = bsonjs.dumps(bson.BSON.encode({'results': habits}))
    return json_record2

@app.route('/add_person')
@cross_origin(origin='*')
def add_person():
    return jsonify(str(flask_back.DB.parser.add_person(request.args.get('login'),request.args.get('password'))))

@app.route('/add_person_habit')
@cross_origin(origin='*')
def add_person_habit():
    return jsonify(str(flask_back.DB.parser.add_person_habit(request.args.get('_id'),request.args.get('name'),request.args.get('start'), request.args.get('end'))))

@app.route('/add_check_for_person_habit')
@cross_origin(origin='*')
def add_check_for_persons_habit():
    return jsonify(str(flask_back.DB.parser.add_check_for_person_habit(request.args.get('_id_habit'),request.args.get('start'), request.args.get('end'))))

@app.route('/get_consecutive_days')
@cross_origin(origin='*')
def get_consecutive_days():
    return jsonify(str(flask_back.DB.parser.get_consecutive_days(request.args.get('_id_habit'))))

@app.route('/delete_habit')
@cross_origin(origin='*')
def delete_habit():
    db_habits = Habits()
    return jsonify(str(db_habits.delete(request.args.get('_id_habit'))))

@app.route('/delete_check')
@cross_origin(origin='*')
def del_check_for_person_habit():
    return jsonify(str(flask_back.DB.parser.del_check_for_person_habit(request.args.get('_id_habit'), request.args.get('data_del'))))
