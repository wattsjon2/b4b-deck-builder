from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    # email, password, submit_button
    email = StringField('Email', validators= [DataRequired(),Email()])
    password = PasswordField('Password', validators= [DataRequired()])
    submit_button = SubmitField()


class CardSearchForm(FlaskForm):
    searchfield = StringField('Search', validators= [DataRequired()])
    search = SubmitField() 
    reset = SubmitField()
    showsupply = SubmitField()

class NewDeckForm(FlaskForm):
    newdeckname = StringField('NewDeckName', validators= [DataRequired()])
    save = search = SubmitField()

class UpdateDeckForm(FlaskForm):
    updatedeckname = StringField('UpdateDeckName', validators= [DataRequired()])
    update = SubmitField()
    cancel = SubmitField()
