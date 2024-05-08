from wtforms import Form, IntegerField, validators
from config import MAX_DIE_ALLOWED, MAX_REPEATS_ALLOWED

class DiceForm(Form):
    d2 = IntegerField('d2', validators=[validators.NumberRange(0, MAX_DIE_ALLOWED)], default=0)
    d4 = IntegerField('d4', validators=[validators.NumberRange(0, MAX_DIE_ALLOWED)], default=0)
    d6 = IntegerField('d6', validators=[validators.NumberRange(0, MAX_DIE_ALLOWED)], default=0)
    d8 = IntegerField('d8', validators=[validators.NumberRange(0, MAX_DIE_ALLOWED)], default=0)
    d10 = IntegerField('d10', validators=[validators.NumberRange(0, MAX_DIE_ALLOWED)], default=0)
    d12 = IntegerField('d12', validators=[validators.NumberRange(0, MAX_DIE_ALLOWED)], default=0)
    d20 = IntegerField('d20', validators=[validators.NumberRange(0, MAX_DIE_ALLOWED)], default=0)
    d100 = IntegerField('d100', validators=[validators.NumberRange(0, MAX_DIE_ALLOWED)], default=0)
    n_repeats = IntegerField('n_repeats', validators=[validators.NumberRange(1, MAX_REPEATS_ALLOWED)], default=1)
