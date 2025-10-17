from flask import Flask, jsonify, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }

# vurnability Broken Access Control
# issue user id passed directly in, same as problem 1

@app.route('/account/<user_id>')
def get_account(user_id):
    user = db.query(User).filter_by(id=user_id).first()
    return jsonify(user.to_dict())

# fixed version
# server authenticates the user by the session same as problem 1

@app.route('/account')
def get_account():
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    user = db.query(User).filter_by(id=session['user_id']).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    return jsonify(user.to_dict())