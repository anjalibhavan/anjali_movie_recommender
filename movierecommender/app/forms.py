from flask_wtf import FlaskForm
from wtforms import IntegerField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class RecoForm(FlaskForm):
    movie1 = IntegerField('Movie 1', validators=[DataRequired(),NumberRange(min=1, max=102, message='Please enter a valid movie number (between 1 and 102).')])
    ratings1 = IntegerField('Rating',validators=[DataRequired(),NumberRange(min=1,max=5,message='Please enter a valid rating (between 1 and 5).')])
    movie2 = IntegerField('Movie 2', validators=[DataRequired(),NumberRange(min=1, max=102, message='Please enter a valid movie number (between 1 and 102).')])
    ratings2 = IntegerField('Rating',validators=[DataRequired(),NumberRange(min=1,max=5,message='Please enter a valid rating (between 1 and 5).')])
    movie3 = IntegerField('Movie 3', validators=[DataRequired(),NumberRange(min=1, max=102, message='Please enter a valid movie number (between 1 and 102).')])
    ratings3 = IntegerField('Rating',validators=[DataRequired(),NumberRange(min=1,max=5,message='Please enter a valid rating (between 1 and 5).')])
    movie4 = IntegerField('Movie 4', validators=[DataRequired(),NumberRange(min=1, max=102, message='Please enter a valid movie number (between 1 and 102).')])
    ratings4 = IntegerField('Rating',validators=[DataRequired(),NumberRange(min=1,max=5,message='Please enter a valid rating (between 1 and 5).')])
    movie5 = IntegerField('Movie 5', validators=[DataRequired(),NumberRange(min=1, max=102, message='Please enter a valid movie number (between 1 and 102).')])
    ratings5 = IntegerField('Rating', validators=[DataRequired()])
    submit = SubmitField('Submit')