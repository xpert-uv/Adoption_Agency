from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import AnyOf, Optional, URL, NumberRange


class PetForm(FlaskForm):

    name = StringField("Pets Name")
    species = StringField(
        "Species", validators=[AnyOf(values=['cat', 'dog', 'porcupine'])])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(
        min=0, max=30, message="Pet with age between 0-30 years are acceptable")])
    notes = StringField("Notes")
