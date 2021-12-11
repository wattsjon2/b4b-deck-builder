from re import I
from flask import Blueprint, render_template, request, jsonify,Flask, flash, redirect,json
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

deck = []
deckid = []
decknamelist = []
location = []

@site.route('/', methods = ['GET', 'POST'])
def home():
    cards = Card.query
    search = CardSearchForm()
    newdeck = NewDeckForm()
    updatedeck = UpdateDeckForm()
    searchField = ''
    mydecks = Deck.query



    if request.method == 'POST':
        if search.search.data:
            searchField = search.searchfield.data
            location.clear()
            location.append('search-loc')
            view = location[0]
            if decknamelist != []:
                deckname = decknamelist[0]
            else:
                deckname = ''
            return render_template('index.html', cards = cards, search = search, searchField = searchField, deck = deck, newdeck = newdeck, mydecks = mydecks, deckid = deckid, updatedeck = updatedeck,  deckname = deckname, view = view)

        save = request.form.get('save')
        add = request.form.get('add')
        moveRight = request.form.get('moveRight')
        moveLeft = request.form.get('moveLeft')
        removeCard = request.form.get('removeCard')
        show = request.form.get('show')
        duplicate = request.form.get('duplicate')
        delete = request.form.get('delete')
        cancel = request.form.get('cancel')
        update = request.form.get('update')
        


        if newdeck.save.data and deck != []:

            while len(deck) < 15:
                deck.append(0)

            user_token = current_user.token
            deck_name = request.form.get('newdeckname')
            card_1 = deck[0]
            card_2 = deck[1]
            card_3 = deck[2]
            card_4 = deck[3]
            card_5 = deck[4]
            card_6 = deck[5]
            card_7 = deck[6]
            card_8 = deck[7]
            card_9 = deck[8]
            card_10 = deck[9]
            card_11 = deck[10]
            card_12 = deck[11]
            card_13 = deck[12]
            card_14 = deck[13]
            card_15 = deck[14]
            newDeck = Deck(user_token, deck_name, card_1,card_2,card_3,card_4,card_5,card_6,card_7,card_8,card_9,card_10,card_11,card_12,card_13,card_14,card_15)
            db.session.add(newDeck)
            db.session.commit()

            deck.clear()
            
            location.clear()
            location.append('saved-loc')
            # {% if deck['user_token'] == current_user.token %}

            return redirect(  url_for('site.home')  )
        if save and deck == []:
            #TODO popup add cards
            pass

        if add:
            if len(deck) < 15:
                deck.append(int(add))

                location.clear()
                location.append('add-loc')

                return redirect(  url_for('site.home')  )
            else:
                pass
            # TODO    
            #    flash('You have reached the maximum amount of cards your deck can hold')
        #if request.form['moveRight']:
        if moveRight:
            currenti = int(moveRight)
            current = deck[currenti]
            switch = deck[currenti + 1]
            deck[currenti] = switch
            deck[currenti + 1] = current

            location.clear()
            location.append('deck-loc')

            return redirect(  url_for('site.home')  )

        if moveLeft:
            currenti = int(moveLeft)
            current = deck[currenti]
            switch = deck[currenti - 1]
            deck[currenti] = switch
            deck[currenti - 1] = current

            location.clear()
            location.append('deck-loc')

            return redirect(  url_for('site.home')  ) 

        if removeCard:
            currenti = int(removeCard)
            deck.pop(currenti)

            location.clear()
            location.append('deck-loc')

            return redirect(  url_for('site.home')  ) 

        if show:
            deck.clear()
            deckid.clear()
            deckid.append(show)

            updateddeck = Deck.query.filter_by(id = int(show))
            for update in updateddeck:
                deck.append(update.card_1)
                deck.append(update.card_2)
                deck.append(update.card_3)
                deck.append(update.card_4)
                deck.append(update.card_5)
                deck.append(update.card_6)
                deck.append(update.card_7)
                deck.append(update.card_8)
                deck.append(update.card_9)
                deck.append(update.card_10)
                deck.append(update.card_11)
                deck.append(update.card_12)
                deck.append(update.card_13)
                deck.append(update.card_14)
                deck.append(update.card_15)
                deckname = update.deck_name
                decknamelist.append(update.deck_name)

            while 0 in deck:
                deck.remove(0)

            location.clear()
            location.append('deck-loc')
            view = location[0]

            
            return render_template('index.html', cards = cards, search = search, searchField = searchField, deck = deck, newdeck = newdeck, mydecks = mydecks, deckid = deckid, updatedeck = updatedeck, deckname = deckname, view = view)
        
        if update:

            while len(deck) < 15:
                deck.append(0)

            DeckUpdated = Deck.query.filter_by(id = int(deckid[0])).update(dict(deck_name = request.form.get('updatedeckname'),
            card_1 = deck[0], card_2 = deck[1], card_3 = deck[2], card_4 = deck[3], card_5 = deck[4], card_6 = deck[5], card_7 = deck[6], card_8 = deck[7],
            card_9 = deck[8], card_10 = deck[9], card_11 = deck[10], card_12 = deck[11], card_13 = deck[12], card_14 = deck[13], card_15 = deck[14]))
            
            db.session.commit()    

            deckid.clear()
            deck.clear()
            decknamelist.clear()
            location.clear()
            location.append('save-loc')

            return redirect(  url_for('site.home')  )

        if duplicate:
            dupdeck = Deck.query.filter_by(id = int(duplicate))
            deck.clear()

            for dup in dupdeck:
                deck.append(dup.card_1)
                deck.append(dup.card_2)
                deck.append(dup.card_3)
                deck.append(dup.card_4)
                deck.append(dup.card_5)
                deck.append(dup.card_6)
                deck.append(dup.card_7)
                deck.append(dup.card_8)
                deck.append(dup.card_9)
                deck.append(dup.card_10)
                deck.append(dup.card_11)
                deck.append(dup.card_12)
                deck.append(dup.card_13)
                deck.append(dup.card_14)
                deck.append(dup.card_15)

            while 0 in deck:
                deck.remove(0)
            
            location.clear()
            location.append('deck-loc')

            return redirect(  url_for('site.home') ) 

        if delete:
            Deck.query.filter_by(id = int(delete)).delete()
            db.session.commit()

            location.clear()
            location.append('saved-loc')

            return redirect(  url_for('site.home') ) 
            
        if cancel:
            deckid.clear()
            deck.clear()
            decknamelist.clear()

            location.clear()
            location.append('deck-loc')


            return redirect(  url_for('site.home' )) 
    
    if decknamelist != []:
        deckname = decknamelist[0]
    else:
        deckname = ''
    if location == []:
        view = ''
    else:
        view = location[0]
    return render_template('index.html',  cards = cards, search = search, searchField = searchField, deck = deck, newdeck = newdeck, mydecks = mydecks, deckid = deckid, updatedeck = updatedeck,  deckname = deckname, view = view)


@site.route('/profile', methods = ['GET','POST'])
@login_required
def profile():
    return render_template('profile.html')
