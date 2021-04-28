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

    money_id = [5,7,8,11,12,14,15,16,17,21,22,23,24,26]
    religion_id = [1,2,3,4,6,9,10,13,18,19,20,25,27,28]


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

