from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class CityForm(FlaskForm):
    search = StringField(
        render_kw={
            'placeholder':'Enter city',
            'style':'width: 1000%;'
                    'position: absolute;'
                    'top: 0;'
                    'left: 100px;'
        })
    submit = SubmitField('Search')