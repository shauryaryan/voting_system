# from flask import request, jsonify
# from app import app, db, bcrypt
# from models import User, Vote
# from pyfingerprint.pyfingerprint import PyFingerprint
#
# # Initialize fingerprint sensor
# try:
#     fingerprint_sensor = PyFingerprint('/dev/ttyUSB0', 57600)
#     if not fingerprint_sensor.verifyPassword():
#         raise ValueError('The given fingerprint sensor password is wrong!')
# except Exception as e:
#     print('The fingerprint sensor could not be initialized!')
#     print('Exception message: ' + str(e))
#     exit(1)
#
# def capture_fingerprint():
#     """Captures a fingerprint and returns the template"""
#     print('Waiting for finger...')
#     while not fingerprint_sensor.readImage():
#         pass
#
#     fingerprint_sensor.convertImage(0x01)
#     result = fingerprint_sensor.searchTemplate()
#     position_number = result[0]
#
#     if position_number >= 0:
#         print('Template already exists at position #' + str(position_number))
#         return None
#
#     fingerprint_sensor.createTemplate()
#     template = fingerprint_sensor.downloadCharacteristics(0x01)
#     return template
#
# @app.route('/register', methods=['POST'])
# def register():
#     data = request.get_json()
#     template = capture_fingerprint()
#     if template is None:
#         return jsonify({'message': 'Fingerprint already exists!'}), 400
#
#     hashed_fingerprint = bcrypt.generate_password_hash(str(template)).decode('utf-8')
#     new_user = User(name=data['name'], fingerprint_hash=hashed_fingerprint)
#     new_user.save()
#     return jsonify({'message': 'User registered successfully'}), 201
#
# @app.route('/authenticate', methods=['POST'])
# def authenticate():
#     data = request.get_json()
#     user = db.users.find_one({'name': data['name']})
#
#     if user:
#         template = capture_fingerprint()
#         if template and bcrypt.check_password_hash(user['fingerprint_hash'], str(template)):
#             return jsonify({'message': 'Authentication successful'}), 200
#
#     return jsonify({'message': 'Authentication failed'}), 401
#
# @app.route('/vote', methods=['POST'])
# def vote():
#     data = request.get_json()
#     user = db.users.find_one({'name': data['name']})
#
#     if user:
#         template = capture_fingerprint()
#         if template and bcrypt.check_password_hash(user['fingerprint_hash'], str(template)):
#             new_vote = Vote(user_id=user['_id'], candidate_id=data['candidate_id'])
#             new_vote.save()
#             return jsonify({'message': 'Vote cast successfully'}), 201
#
#     return jsonify({'message': 'Authentication failed'}), 401
#
# @app.route('/admin/votes', methods=['GET'])
# def admin_votes():
#     votes = db.votes.find()
#     results = [{'id': str(vote['_id']), 'user_id': str(vote['user_id']), 'candidate_id': vote['candidate_id'], 'timestamp': vote['timestamp']} for vote in votes]
#     return jsonify(results), 200

# from flask import request, jsonify
# from app import app, db, bcrypt
# from models import User, Vote
#
# def capture_fingerprint():
#     """Mock function to return a fixed template for testing purposes"""
#     print('Mocking fingerprint capture...')
#     # Example mock template (a list of integers representing a fingerprint template)
#     return [120, 245, 365, 478, 590, 655, 712, 834, 911, 1023]
#
# @app.route('/api/register', methods=['POST'])
# def register():
#     data = request.get_json()
#     template = capture_fingerprint()
#     if template is None:
#         return jsonify({'message': 'Fingerprint already exists or sensor not found!'}), 400
#
#     hashed_fingerprint = bcrypt.generate_password_hash(str(template)).decode('utf-8')
#     new_user = User(name=data['name'], fingerprint_hash=hashed_fingerprint)
#     new_user.save()
#     return jsonify({'message': 'User registered successfully'}), 201
#
# @app.route('/api/authenticate', methods=['POST'])
# def authenticate():
#     data = request.get_json()
#     user = db.users.find_one({'name': data['name']})
#
#     if user:
#         template = capture_fingerprint()
#         if template and bcrypt.check_password_hash(user['fingerprint_hash'], str(template)):
#             return jsonify({'message': 'Authentication successful'}), 200
#
#     return jsonify({'message': 'Authentication failed'}), 401
#
# @app.route('/api/vote', methods=['POST'])
# def vote():
#     data = request.get_json()
#     user = db.users.find_one({'name': data['name']})
#
#     if user:
#         template = capture_fingerprint()
#         if template and bcrypt.check_password_hash(user['fingerprint_hash'], str(template)):
#             new_vote = Vote(user_id=user['_id'], candidate_id=data['candidate_id'])
#             new_vote.save()
#             return jsonify({'message': 'Vote cast successfully'}), 201
#
#     return jsonify({'message': 'Authentication failed'}), 401
#
# @app.route('/api/admin/votes', methods=['GET'])
# def admin_votes():
#     votes = db.votes.find()
#     results = [{'id': str(vote['_id']), 'user_id': str(vote['user_id']), 'candidate_id': vote['candidate_id'], 'timestamp': vote['timestamp']} for vote in votes]
#     return jsonify(results), 200

from flask import request, jsonify
from app import app, db, bcrypt
from models import User, Vote

def capture_fingerprint():
    """Mock function to return a fixed template for testing purposes"""
    print('Mocking fingerprint capture...')
    return [120, 245, 365, 478, 590, 655, 712, 834, 911, 1023]

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    template = capture_fingerprint()
    if template is None:
        return jsonify({'message': 'Fingerprint already exists or sensor not found!'}), 400

    hashed_fingerprint = bcrypt.generate_password_hash(str(template)).decode('utf-8')
    new_user = User(name=data['name'], fingerprint_hash=hashed_fingerprint)
    new_user.save()
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/api/authenticate', methods=['POST'])
def authenticate():
    data = request.get_json()
    user = db.users.find_one({'name': data['name']})

    if user:
        template = capture_fingerprint()
        if template and bcrypt.check_password_hash(user['fingerprint_hash'], str(template)):
            return jsonify({'message': 'Authentication successful'}), 200

    return jsonify({'message': 'Authentication failed'}), 401

@app.route('/api/vote', methods=['POST'])
def vote():
    data = request.get_json()
    user = db.users.find_one({'name': data['name']})

    if user:
        template = capture_fingerprint()
        if template and bcrypt.check_password_hash(user['fingerprint_hash'], str(template)):
            new_vote = Vote(user_id=user['_id'], candidate_id=data['candidate_id'])
            new_vote.save()
            return jsonify({'message': 'Vote cast successfully'}), 201

    return jsonify({'message': 'Authentication failed'}), 401

@app.route('/api/admin/votes', methods=['GET'])
def admin_votes():
    votes = db.votes.find()
    results = []
    for vote in votes:
        results.append({
            'id': str(vote['_id']),
            'user_id': str(vote['user_id']),
            'candidate_id': vote['candidate_id'],
            'timestamp': vote.get('timestamp', 'No timestamp')
        })
    return jsonify(results), 200
