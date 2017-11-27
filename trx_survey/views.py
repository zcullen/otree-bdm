from otree.api import Currency as c, currency_range, safe_json
from . import models
from ._builtin import Page, WaitPage
from .models import Constants, Player
from django.conf import settings
import random

class Introduction(Page):   # extra manager intro

    def vars_for_template(self):
#        if self.session.mturk_HITId:
#            for p in self.session.get_participants():
#                wid = p.mturk_worker_id
#                return {'wid': wid}
        idx = random.randint(1,20)
        if ( idx == 1):
            wid = 'A3KR3JXXEHZDGV'
            qno = 1
            ans = 2
            niner = True
        elif ( idx == 2):
            wid = 'A1A02K56ENPSO'
            qno = 1
            ans = 2
            niner = True
        elif ( idx == 3):
            wid = 'A3RQPPTVFJB6EE'
            qno = 4
            ans = 6
            niner = False
        elif ( idx == 4):
            wid = 'A2QRYZKNA9XT4T'
            qno = 2
            ans = 4
            niner = False
        elif ( idx == 5):
            wid = 'APZQ9ADUXTS7N'
            qno = 5
            ans = 7
            niner = False
        elif ( idx == 6):
            wid = 'A115C4B2OHIESF'
            qno = 1
            ans = 2
            niner = True
        elif ( idx == 7):
            wid = 'A3VO62XB3T2TLB'
            qno = 4
            ans = 6
            niner = False
        elif ( idx == 8):
            wid = 'A198SS8SV0LWKB'
            qno = 5
            ans = 7
            niner = False
        elif ( idx == 9):
            wid = 'A1N474MXOPLSJ2'
            qno = 1
            ans = 2
            niner = True
        elif ( idx == 10):
            wid = 'A3NSJ6GJC7TZSG'
            qno = 3
            ans = 5
            niner = False
        elif ( idx == 11):
            wid = 'A3OV174HQJIJK8'
            qno = 3
            ans = 5
            niner = False
        elif ( idx == 12):
            wid = 'A35F2841BY4XB4'
            qno = 2
            ans = 2
            niner = True
        elif ( idx == 13):
            wid = 'A36MRQBG3LDR7I'
            qno = 2
            ans = 4
            niner = False
        elif ( idx == 14):
            wid = 'A3S2E0M3MI59QD'
            qno = 3
            ans = 2
            niner = True
        elif ( idx == 15):
            wid = 'ACJYC1XM245T1'
            qno = 1
            ans = 2
            niner = True
        elif ( idx == 16):
            wid = 'AVC1PLLFS210S'
            qno = 1
            ans = 2
            niner = True
        elif ( idx == 17):
            wid = 'A16G6PPH1INQL8'
            qno = 1
            ans = 2
            niner = True
        elif ( idx == 18):
            wid = 'A20H1EL2ZO41DP'
            qno = 3
            ans = 5
            niner = False
        elif ( idx == 19):
            wid = 'A3T1FM3126RW25'
            qno = 1
            ans = 2
            niner = True
        elif ( idx == 20):
            wid = 'A3JMJIKX36UNC7'
            qno = 1
            ans = 2
            niner = True
        return{'wid': wid,
                'qno': qno+2,
                'qno5': (qno+2)*5,
                'ans': ans,
                'niner': niner}        


class Sample(Page):      # transcription sample for manager
    form_model = models.Player
    form_fields = ['howLong']

class Preferences(Page):
    form_model = models.Player
    form_fields = ['pref1','pref2','pref3','pref4','pref5']

class Bid(Page):             
    form_model = models.Player
    form_fields = ['bid']
   
    def before_next_page(self):
        self.participant.vars['bid'] = self.player.bid

page_sequence = [

    Introduction
#    Sample,
#    Preferences,
#    Bid
]