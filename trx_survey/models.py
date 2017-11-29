from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

import random

def validate_nonzero(value):
    if value == 0:
        raise ValidationError(
            _('%(value)s is not an acceptable answer'),
            params={'value': value},
        )

author = 'James Flynn'

doc = """
Transcription Negotiation
"""

class Constants(BaseConstants):
    name_in_url = 'trx_survey'
    players_per_group = None
    num_rounds = 1
    mturk_ids = {1:'A3KR3JXXEHZDGV',
                 2:'A1A02K56ENPSO',
                 3:'A3RQPPTVFJB6EE',
                 4:'A2QRYZKNA9XT4T',
                 5:'APZQ9ADUXTS7N',
                 6:'A115C4B2OHIESF',
                 7:'A3VO62XB3T2TLB',
                 8:'A198SS8SV0LWKB',
                 9:'A1N474MXOPLSJ2',
                 10:'A3NSJ6GJC7TZSG',
                 11:'A3OV174HQJIJK8',
                 12:'A35F2841BY4XB4',
                 13:'A36MRQBG3LDR7I',
                 14:'A3S2E0M3MI59QD',
                 15:'ACJYC1XM245T1',
                 16:'AVC1PLLFS210S',
                 17:'A16G6PPH1INQL8',
                 18:'A20H1EL2ZO41DP',
                 19:'A3T1FM3126RW25',
                 20:'A3JMJIKX36UNC7'}

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
	pass

P1_CHOICES = (('3','$15, for 5 pages transcribed ($3 per page, 95% accuracy)'),('2','$9, no transcription required '))
P2_CHOICES = (('4','$20, for 5 pages transcribed ($4 per page, 95% accuracy)'),('2','$9, no transcription required '))
P3_CHOICES = (('5','$25, for 5 pages transcribed ($5 per page, 95% accuracy)'),('2','$9, no transcription required '))
P4_CHOICES = (('6','$30, for 5 pages transcribed ($6 per page, 95% accuracy)'),('2','$9, no transcription required '))
P5_CHOICES = (('7','$35, for 5 pages transcribed ($7 per page, 95% accuracy)'),('2','$9, no transcription required '))


class Player(BasePlayer):
    howLong = models.PositiveIntegerField(validators=[validate_nonzero],default=0,min=0,max=180,widget=widgets.SliderInput(attrs={'step': '5'}))
    bid = models.CurrencyField()
    pref1 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal(choices=P1_CHOICES))
    pref2 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal(choices=P2_CHOICES))
    pref3 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal(choices=P3_CHOICES))
    pref4 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal(choices=P4_CHOICES))
    pref5 = models.PositiveIntegerField(widget=widgets.RadioSelectHorizontal(choices=P5_CHOICES))

