from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'payment'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    participant_vars_full = models.StringField()

    family_income = models.IntegerField(min=0,max=10000000, label='''What is your family's annual income, from all sources? Please enter the amount below.''')

    mother_tongue = models.StringField(label='What is your mother tongue?')

    english_fluency = models.StringField(choices=['None', 'Beginner', 'Fluent', 'Native'],
                                  widget=widgets.RadioSelectHorizontal,
                                  label='How fluent are you in English?')

    hindi_fluency = models.StringField(choices=['None', 'Beginner', 'Fluent', 'Native'],
                                  widget=widgets.RadioSelectHorizontal,
                                  label='How fluent are you in Hindi?')

    outfit = models.LongStringField(label='How would you describe what you are wearing today?')



    def random_payments(self):
        dictator_payoffs = [self.participant.vars['dictator_round_1_payoff'],
                            self.participant.vars['dictator_round_2_payoff'],
                            self.participant.vars['dictator_round_3_payoff']]
        print(self.id_in_group,dictator_payoffs)
        ultimatum_payoffs = [self.participant.vars['ultimatum_round_1_payoff'],
                             self.participant.vars['ultimatum_round_2_payoff'],
                             self.participant.vars['ultimatum_round_3_payoff']]
        print(self.id_in_group, ultimatum_payoffs)
        dp = random.shuffle(dictator_payoffs)
        up = random.shuffle(ultimatum_payoffs)
        dictator_final_payoff = random.choice(dictator_payoffs)
        ultimatum_final_payoff = random.choice(ultimatum_payoffs)
        self.participant.vars['dictator_final_payoff'] = dictator_final_payoff
        self.participant.vars['ultimatum_final_payoff'] = ultimatum_final_payoff

        if self.participant.vars['type'] == 4:
            self.participant.payoff = self.participant.vars['election_payoff'] + self.participant.vars['dictator_final_payoff'] + self.participant.vars['ultimatum_final_payoff'] + c(300)
            self.participant_vars_full = str(self.participant.vars)
        else:
            self.participant.payoff = self.participant.vars['election_payoff'] + self.participant.vars['dictator_final_payoff'] + self.participant.vars['ultimatum_final_payoff'] + c(100)
            self.participant_vars_full = str(self.participant.vars)