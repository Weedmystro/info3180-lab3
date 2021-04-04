from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField



class myForm(FlaskForm):
    name=StringField('Name',validators=[DataRequired()]);
    email=StringField('Email',validators=[DataRequired()]);
    subject=StringField('Subject',validators=[DataRequired()]);
    message = StringField('Message'),validators=[DataRequired()]);
    msg=TextAreaField('Message',validators=[DataRequired()]);



class ContactForm(FlaskForm):
    name = StringField('Name (Required)')
    email = StringField('Email (Required)')
    subject = StringField('Subject (Required)')
    message = StringField('Message (Required)')
    submit = SubmitField('Send')

