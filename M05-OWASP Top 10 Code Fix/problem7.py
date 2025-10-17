from flask import Flask, request
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

# vurnability Insecure Design
# issue user.password not handled correctly, stored as plain text

@app.route('/reset-password', methods=['POST'])
def reset_password():
    email = request.form['email']
    new_password = request.form['new_password']
    user = User.query.filter_by(email=email).first()
    user.password = new_password
    db.session.commit()
    return 'Password reset'

# fixed version
# saves the password as a hash instead of plain text

import problem4

@app.route('/reset-password', methods=['POST'])
def reset_password():
    email = request.form['email']
    new_password = request.form['new_password']

    user = User.query.filter_by(email=email).first()
    if not user:
        return 'User not found', 404

    user.password = problem4.hash_password_fixed(new_password)

    db.session.commit()
    return 'Password reset successfully'

