from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired

class LearnyWebForm(FlaskForm):
    textinput = StringField('Ihr Text', validators=[DataRequired()], widget=TextArea())
    submit = SubmitField('erstellen')
    clozetest_btn = SubmitField('Lückentext')
    wordsearch_btn = SubmitField('Suchsel')
    syllables_btn = SubmitField('Silben')
    presentOrPast_btn = SubmitField('Zeitformen')
    infinitive_btn = SubmitField('Infinitiv')
