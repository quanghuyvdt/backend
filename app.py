from flask import request, jsonify
from bson.objectid import ObjectId
from __init__ import app, db

@app.route("/")
def home():
    students = list(db.students.find())
    for i in range(len(students)):
        students[i]['_id'] = str(ObjectId(students[i]['_id']))
    return jsonify(students), 200

@app.route('/detail/<string:_id>')
def get_student_by(_id):
    student = db.students.find_one(ObjectId(_id))
    student['_id'] = str(ObjectId(_id))
    return jsonify(student), 200

    
@app.route('/add', methods=['POST'])
def add():
    new_student = request.get_json()
    del new_student['_id']

    result = db.students.insert_one(new_student)
    new_student['_id'] = str(result.inserted_id)
    return jsonify(new_student), 200


@app.route('/update/<string:_id>', methods=['POST'])
def update(_id):
    new_student = request.get_json()
    del new_student['_id']
    
    result = db.students.find_one_and_update(
        {"_id": ObjectId(_id)},
        {"$set": new_student},
        upsert=False,
        return_document = True
    )
    if result:
        result['_id'] = str(result['_id'])
        return jsonify(result), 200
    return jsonify({'Error': 'Student not found'}), 404



@app.route('/delete/<string:_id>', methods=['POST'])
def delete(_id):
    result = db.students.find_one_and_delete(ObjectId(_id))
    if result:
        jsonify({'message': 'Delete student successfully!'}), 200
    return jsonify({'message': 'Student doesnt exist!'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
