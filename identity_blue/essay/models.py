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

    money_id = [1,4,10,11,13,14,16,17,20,23,24,25,26,27]
    religion_id = [2,3,5,6,7,8,9,12,15,18,19,21,22,28]


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

