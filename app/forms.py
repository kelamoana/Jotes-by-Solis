from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    ingredients = StringField('Ingredients', validators=[DataRequired()])
    #sorting = RadioField('Sort by: ', choices=[('Highest Ratings','description'),('Trendiness','whatever')])
    submit = SubmitField('Search Recipes')