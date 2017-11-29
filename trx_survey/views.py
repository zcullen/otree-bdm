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
        wid = Constants.mturk_ids[random.randint(1,20)]

        if (wid == Constants.mturk_ids[1]):
            qno = 1
            ans = 2
            niner = True
        elif (wid == Constants.mturk_ids[2]):
            qno = 1
            ans = 2
            niner = True
        elif (wid == Constants.mturk_ids[3]):
            qno = 4
            ans = 6
            niner = False
        elif (wid == Constants.mturk_ids[4]):
            qno = 2
            ans = 4
            niner = False
        elif (wid == Constants.mturk_ids[5]):
            qno = 5
            ans = 7
            niner = False
        elif (wid == Constants.mturk_ids[6]):
            qno = 1
            ans = 2
            niner = True
        elif (wid == Constants.mturk_ids[7]):
            qno = 4
            ans = 6
            niner = False
        elif (wid == Constants.mturk_ids[8]):
            qno = 5
            ans = 7
            niner = False
        elif (wid == Constants.mturk_ids[9]):
            qno = 1
            ans = 2
            niner = True
        elif (wid == Constants.mturk_ids[10]):
            qno = 3
            ans = 5
            niner = False
        elif (wid == Constants.mturk_ids[11]):
            qno = 3
            ans = 5
            niner = False
        elif (wid == Constants.mturk_ids[12]):
            qno = 2
            ans = 2
            niner = True
        elif (wid == Constants.mturk_ids[13]):
            qno = 2
            ans = 4
            niner = False
        elif (wid == Constants.mturk_ids[14]):
            qno = 3
            ans = 2
            niner = True
        elif (wid == Constants.mturk_ids[15]):
            qno = 1
            ans = 2
            niner = True
        elif (wid == Constants.mturk_ids[16]):
            qno = 1
            ans = 2
            niner = True
        elif (wid == Constants.mturk_ids[17]):
            qno = 1
            ans = 2
            niner = True
        elif (wid == Constants.mturk_ids[18]):
            qno = 3
            ans = 5
            niner = False
        elif (wid == Constants.mturk_ids[19]):
            qno = 1
            ans = 2
            niner = True
        elif (wid == Constants.mturk_ids[20]):
            qno = 1
            ans = 2
            niner = True
        return{ 'wid': wid,
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