# from app import db
#
# class User:
#     def __init__(self, name, fingerprint_hash):
#         self.name = name
#         self.fingerprint_hash = fingerprint_hash
#
#     def save(self):
#         db.users.insert_one({
#             'name': self.name,
#             'fingerprint_hash': self.fingerprint_hash
#         })
#
# class Vote:
#     def __init__(self, user_id, candidate_id):
#         self.user_id = user_id
#         self.candidate_id = candidate_id
#
#     def save(self):
#         db.votes.insert_one({
#             'user_id': self.user_id,
#             'candidate_id': self.candidate_id
#         })
#
from app import db
from datetime import datetime

class User:
    def __init__(self, name, fingerprint_hash):
        self.name = name
        self.fingerprint_hash = fingerprint_hash

    def save(self):
        db.users.insert_one({
            'name': self.name,
            'fingerprint_hash': self.fingerprint_hash
        })

class Vote:
    def __init__(self, user_id, candidate_id):
        self.user_id = user_id
        self.candidate_id = candidate_id
        self.timestamp = datetime.utcnow()  # Add a timestamp field

    def save(self):
        db.votes.insert_one({
            'user_id': self.user_id,
            'candidate_id': self.candidate_id,
            'timestamp': self.timestamp  # Ensure the timestamp is saved
        })
