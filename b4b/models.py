from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime

# adding flask security for passwords
from werkzeug.security import generate_password_hash, check_password_hash

# import for secrets module (given by python)
import secrets 

from flask_login import LoginManager, UserMixin
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(150), nullable = True, default = '')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = True)
    g_auth_verify = db.Column(db.Boolean, default = False)
    token = db.Column(db.String, default = '', unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self,email, first_name ='',last_name = '', id = '', password = '', token = '', g_auth_verify = False):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self,password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def set_token(self,length):
        return secrets.token_hex(length)

    def __repr__(self):
        return f'User {self.email} has been added to the Database'


class Card(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    card_name = db.Column(db.String(150))
    card_description = db.Column(db.String(250), nullable = True)
    supply_line = db.Column(db.String(100), nullable = True)
    supply_track = db.Column(db.String(100), nullable = True)

    def __init__(self, card_name, card_description, supply_line, supply_track):
        self.id = self.id
        self.card_name = card_name
        self.card_description = card_description
        self.supply_line = supply_line
        self.supply_track = supply_track



    def __repr__(self):
        return f'The following card has been added: {self.card_name}'

class Deck(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)
    deck_name = db.Column(db.String(150))
    card_1 = db.Column(db.Integer, nullable = True)
    card_2 = db.Column(db.Integer, nullable = True)
    card_3 = db.Column(db.Integer, nullable = True)
    card_4 = db.Column(db.Integer, nullable = True)
    card_5 = db.Column(db.Integer, nullable = True)
    card_6 = db.Column(db.Integer, nullable = True)
    card_7 = db.Column(db.Integer, nullable = True)
    card_8 = db.Column(db.Integer, nullable = True)
    card_9 = db.Column(db.Integer, nullable = True)
    card_10 = db.Column(db.Integer, nullable = True)
    card_11 = db.Column(db.Integer, nullable = True)
    card_12 = db.Column(db.Integer, nullable = True)
    card_13 = db.Column(db.Integer, nullable = True)
    card_14 = db.Column(db.Integer, nullable = True)
    card_15 = db.Column(db.Integer, nullable = True)

    def __init__(self, user_token, deck_name, card_1,card_2,card_3,card_4,card_5,card_6,card_7,card_8,card_9,card_10,card_11,card_12,card_13,card_14,card_15):
        self.id = self.id
        self.user_token = user_token
        self.deck_name = deck_name
        self.card_1 = card_1
        self.card_2 = card_2
        self.card_3 = card_3
        self.card_4 = card_4
        self.card_5 = card_5
        self.card_6 = card_6
        self.card_7 = card_7
        self.card_8 = card_8
        self.card_9 = card_9
        self.card_10 = card_10
        self.card_11 = card_11
        self.card_12 = card_12
        self.card_13 = card_13
        self.card_14 = card_14
        self.card_15 = card_15


    def __repr__(self):
        return f'The following card has been added: {self.deck_name}'


# creation of API schema via the marshmallow object
class CardSchema(ma.Schema):
    class Meta:
        fields = ['id','card_name','card_description','supply_line', 'supply_track']


card_schema = CardSchema()
cards_schema = CardSchema(many = True)