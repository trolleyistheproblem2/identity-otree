from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'essay'
    players_per_group = None
    num_rounds = 1

    money_id = [2,5,6,9,10,13,14,17,19,20,24,25,27,28]
    religion_id = [1,3,4,7,8,11,12,16,18,21,22,23,15,26]


class Subsession(BaseSubsession):
    pass



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    essay_text = models.LongStringField()

    def set_essay_topic(self):
        if self.participant.vars['subject_id'] in Constants.money_id:
            self.participant.vars['essay_topic'] = 1
        elif self.participant.vars['subject_id'] in Constants.religion_id:
            self.participant.vars['essay_topic'] = 2

