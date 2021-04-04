from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, TextAreaField
from flask_wtf.csrf import CSRFProtect
from wtforms.validators import DataRequired,Email



def create_app():
    app = flask(__name__)
    csrf.init_app(app)


class ContactForm(FlaskForm):
    name=StringField('Name',validators=[DataRequired()]);
    email=StringField('Email',validators=[DataRequired(), Email()]);
    subject=StringField('Subject',validators=[DataRequired()]);
    message=TextAreaField('Message',validators=[DataRequired()]);
   
