from re import I
from flask import Blueprint, render_template, request, jsonify,Flask, flash, redirect,json, session
from flask.helpers import total_seconds, url_for
from flask_login.utils import login_required
from wtforms.fields.simple import SearchField
from b4b.models import db, Card, Deck
from flask_login import login_user, logout_user, current_user, login_required
from b4b.forms import CardSearchForm, NewDeckForm, UpdateDeckForm


"""
    Note that in the below code, some arguments are specified when createing blueprint objects
    The first argument, 'site' is the Blueprint's name, which flask uses for routing
    The second arugment, __name__, is the blueprint's import name which flask uses to locate the Blueprint's resources
"""

site = Blueprint('site',__name__,template_folder = 'site_templates')


@site.route('/', methods = ['GET', 'POST'])
def home():
    cards = Card.query
    search = CardSearchForm()
    newdeck = NewDeckForm()
    updatedeck = UpdateDeckForm()
    mydecks = Deck.query

    allCards = []




   # session['search'] = 'test'
    session.setdefault('test', 'teststring')        #the test function
    session.setdefault('deck', [])
    session.setdefault('deckid','')
    session.setdefault('deckname','')
    session.setdefault('location','')
    session.setdefault('search','')
    session.setdefault('search_cards','empty')
    session.setdefault('show_decks','False')
    session.setdefault('my_decks',[])
    



    if request.method == 'POST':

        save = request.form.get('save')
        show = request.form.get('show')
        duplicate = request.form.get('duplicate')
        delete = request.form.get('delete')
        cancel = request.form.get('cancel')
        update = request.form.get('update')
        
        


        if newdeck.save.data and session.get('deck') != []:

            mydeck = session.get('deck')

            while len(mydeck) < 15: 
                mydeck.append(0)


            user_token = current_user.token
            deck_name = request.form.get('newdeckname')
            card_1 = mydeck[0]
            card_2 = mydeck[1]
            card_3 = mydeck[2]
            card_4 = mydeck[3]
            card_5 = mydeck[4]
            card_6 = mydeck[5]
            card_7 = mydeck[6]
            card_8 = mydeck[7]
            card_9 = mydeck[8]
            card_10 = mydeck[9]
            card_11 = mydeck[10]
            card_12 = mydeck[11]
            card_13 = mydeck[12]
            card_14 = mydeck[13]
            card_15 = mydeck[14]
            newDeck = Deck(user_token, deck_name, card_1,card_2,card_3,card_4,card_5,card_6,card_7,card_8,card_9,card_10,card_11,card_12,card_13,card_14,card_15)
            db.session.add(newDeck)
            db.session.commit()

            session['deck'] = []
            
            
            session['location'] = 'saved-loc'

            return redirect(  url_for('site.home')  )
        if save and session.get('deck') == []:
            #TODO popup add cards
            pass


        if show:
            session['deckid'] = show
            mydeck = []


            updateddeck = Deck.query.filter_by(id = int(show))
            for update in updateddeck:
                mydeck.append(update.card_1)
                mydeck.append(update.card_2)
                mydeck.append(update.card_3)
                mydeck.append(update.card_4)
                mydeck.append(update.card_5)
                mydeck.append(update.card_6)
                mydeck.append(update.card_7)
                mydeck.append(update.card_8)
                mydeck.append(update.card_9)
                mydeck.append(update.card_10)
                mydeck.append(update.card_11)
                mydeck.append(update.card_12)
                mydeck.append(update.card_13)
                mydeck.append(update.card_14)
                mydeck.append(update.card_15)
                session['deckname'] = update.deck_name

            while 0 in mydeck:
                mydeck.remove(0)

            session['deck'] = mydeck     

            session['location'] = 'deck-loc'

            
            return render_template('index.html', cards = cards, search = search, newdeck = newdeck, mydecks = mydecks, updatedeck = updatedeck)
        
        if update:

            mydeck = session.get('deck')

            while len(mydeck) < 15:
                mydeck.append(0)

            DeckUpdated = Deck.query.filter_by(id = int(session.get('deckid'))).update(dict(deck_name = request.form.get('updatedeckname'),
            card_1 = mydeck[0], card_2 = mydeck[1], card_3 = mydeck[2], card_4 = mydeck[3], card_5 = mydeck[4], card_6 = mydeck[5], card_7 = mydeck[6], card_8 = mydeck[7],
            card_9 = mydeck[8], card_10 = mydeck[9], card_11 = mydeck[10], card_12 = mydeck[11], card_13 = mydeck[12], card_14 = mydeck[13], card_15 = mydeck[14]))
            
            db.session.commit()    

            session['deckid'] = ''
            
            
            session['deck'] = []
            session['deckname'] = ''
            session['location'] = 'saved-loc'

            return redirect(  url_for('site.home')  )

        if duplicate:
            dupdeck = Deck.query.filter_by(id = int(duplicate))
            
            mydeck = []

            for dup in dupdeck:
                mydeck.append(dup.card_1)
                mydeck.append(dup.card_2)
                mydeck.append(dup.card_3)
                mydeck.append(dup.card_4)
                mydeck.append(dup.card_5)
                mydeck.append(dup.card_6)
                mydeck.append(dup.card_7)
                mydeck.append(dup.card_8)
                mydeck.append(dup.card_9)
                mydeck.append(dup.card_10)
                mydeck.append(dup.card_11)
                mydeck.append(dup.card_12)
                mydeck.append(dup.card_13)
                mydeck.append(dup.card_14)
                mydeck.append(dup.card_15)

            while 0 in mydeck:
                mydeck.remove(0)

            session['deckname'] = ''
            session['deck'] = mydeck 
            session['location'] = 'deck-loc'

            return redirect(  url_for('site.home') ) 

        if delete:
            Deck.query.filter_by(id = int(delete)).delete()
            db.session.commit()

            session['location'] = 'saved-loc'

            return redirect(  url_for('site.home') ) 
            
        if cancel:
            session['deckname'] = ''
            session['deckid'] = ''
            session['deck'] = [] 
            
            

            session['location'] = 'deck-loc'


            return redirect(  url_for('site.home' )) 

    for card in cards:
        allCards.append(
        {
            'id':card.id
            }
        )
    session['cards'] = allCards   

    
    return render_template('index.html',  cards = cards, search = search, newdeck = newdeck, mydecks = mydecks, updatedeck = updatedeck)


@site.route('/profile', methods = ['GET','POST'])
@login_required
def profile():
    return render_template('profile.html')


@site.route('/test', methods = ['GET','POST'])
def test():
    if request.method == "POST":
        newSession = request.json['test_data']

        session['test'] = newSession

        return jsonify({'result':'success'})

@site.route('/_moveright', methods = ['GET','POST'])
def moveRightAjax():
    if request.method == "POST":
        index = request.json['index']
        mydeck = session.get('deck')
        currenti = int(index)
        current = mydeck[currenti]        
        switch = mydeck[currenti + 1]    
        mydeck[currenti] = switch         
        mydeck[currenti + 1] = current

        session['deck'] = mydeck

        return jsonify({'result':'success'})

@site.route('/_moveleft', methods = ['GET','POST'])
def moveLeftAjax():
    if request.method == "POST":
        index = request.json['index']
        mydeck = session.get('deck')
        currenti = int(index)
        current = mydeck[currenti]        
        switch = mydeck[currenti - 1]    
        mydeck[currenti] = switch         
        mydeck[currenti - 1] = current

        session['deck'] = mydeck

        return jsonify({'result':'success'})

@site.route('/_remove', methods = ['GET','POST'])
def removeCardAjax():  
    if request.method == "POST":
        index = request.json['index']
        mydeck = session.get('deck')
        currenti = int(index)
        mydeck.pop(currenti)

        session['deck'] = mydeck

        return jsonify({'result':'success'})

@site.route('/_add', methods = ['GET','POST'])
def addCardAjax():  
    if request.method == "POST":
        cardid = request.json['card_id']
        mydeck = session.get('deck')
        if len(mydeck) < 15:
                mydeck.append(int(cardid))
                session['deck'] = mydeck

        return jsonify({'result':'success'})

@site.route('/_search', methods = ['GET','POST'])
def searchAjax():  
    if request.method == "POST":
        searchString = request.json['search_text']
        cards = Card.query
        
        searchCards = []
        for card in cards:
            if searchString.lower() in card.card_name.lower() or searchString.lower() in card.card_description.lower():
                searchCards.append(
                {
                    'id':card.id
                    }
                )
        


        session['search_cards'] = searchCards
        session['search'] = searchString

        return jsonify({'result':'success'})

@site.route('/_reset', methods = ['GET','POST'])
def resetAjax():  
    if request.method == "POST":
        
        session['search'] = ''
        session['search_cards'] = 'empty'

        return jsonify({'result':'success'})

@site.route('/_showdecks', methods = ['GET','POST'])
def showDecksAjax():  
    if request.method == "POST":
        
        token = request.json['user']
        
        session['test'] = token

        session['show_decks'] = 'True'

        mydeckslist = []
        mydecks = Deck.query.filter_by(user_token = token)
        for deck in mydecks:
            mydeckslist.append({
                'id':deck.id,
                'deck_name':deck.deck_name
            })

        session['my_decks'] = mydeckslist

        

        return jsonify({'result':'success'})

@site.route('/_hidedecks', methods = ['GET','POST'])
def hideDecksAjax():  
    if request.method == "POST":

        testString = request.json['user']
        
        session['my_decks'] = []
        session['test'] = testString
        session['show_decks'] = 'False'

        return jsonify({'result':'success'})


