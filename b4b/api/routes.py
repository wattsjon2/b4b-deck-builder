from flask import Blueprint,request,jsonify
from b4b.helpers import token_required
from b4b.models import db, User, Card, card_schema, cards_schema


api = Blueprint('api',__name__, url_prefix ='/api')

@api.route('/getdata')
@token_required
def getdata(current_user_token):
    return { 'some':'value'}

# retrive all cards endpoint
@api.route('/cards/all', methods = ['GET'])
@token_required
def get_cards_from_all_users(current_user_token):
    cards = Card.query.all()
    response = cards_schema.dump(cards)
    return jsonify(response)

@api.route('/cards', methods = ['POST'])
@token_required
def create_card(current_user_token):
    card_name = request.json['card_name']
    card_description = request.json['card_description']

    card = Card(card_name, card_description)
    db.session.add(card)
    db.session.commit()
    response = card_schema.dump(card)
    return jsonify(response)


# retrieve single hero endpoint
@api.route('/cards/<id>', methods = ['GET'])
@token_required
def get_card(current_user_token, id):
    card = Card.query.get(id)
    response = card_schema.dump(card)
    return jsonify(response)

# update hero endpoint
@api.route('/cards/<id>', methods = ['POST','PUT'])
@token_required
def update_card(current_user_token, id):

    card = Card.query.get(id) #Get the card

    card.card_name = request.json['card_name']
    card.card_description = request.json['card_description']

    db.session.commit()
    response = card_schema.dump(card)
    return jsonify(response)

# delete hero Endpoint
@api.route('cards/<id>', methods = ['DELETE'])
@token_required
def delete_card(current_user_token, id):
    card = Card.query.get(id)
    db.session.delete(card)
    db.session.commit()

    response = card_schema.dump(card)
    return jsonify(response)