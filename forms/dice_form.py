from wtforms import Form, IntegerField, validators
from config import MAX_DIE_ALLOWED, MAX_REPEATS_ALLOWED

RENDER_OPT = {'onblur': 'validateAllInputs()'}  # validateInput is a JS function called when leaving focus
DICE_VALIDATOR = validators.NumberRange(0, MAX_DIE_ALLOWED)
REPEATS_VALIDATOR = validators.NumberRange(1, MAX_REPEATS_ALLOWED)

class DiceForm(Form):
    d2 = IntegerField('d2', default=0, validators=[DICE_VALIDATOR], render_kw=RENDER_OPT)
    d4 = IntegerField('d4', default=0, validators=[DICE_VALIDATOR], render_kw=RENDER_OPT)
    d6 = IntegerField('d6', default=0, validators=[DICE_VALIDATOR], render_kw=RENDER_OPT)
    d8 = IntegerField('d8', default=0, validators=[DICE_VALIDATOR], render_kw=RENDER_OPT)
    d10 = IntegerField('d10', default=0, validators=[DICE_VALIDATOR], render_kw=RENDER_OPT)
    d12 = IntegerField('d12', default=0, validators=[DICE_VALIDATOR], render_kw=RENDER_OPT)
    d20 = IntegerField('d20', default=0, validators=[DICE_VALIDATOR], render_kw=RENDER_OPT)
    d100 = IntegerField('d100', default=0, validators=[DICE_VALIDATOR], render_kw=RENDER_OPT)
    n_repeats = IntegerField('n_repeats', default=1, validators=[REPEATS_VALIDATOR], render_kw=RENDER_OPT)
