from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


doc = """
One player decides how to divide a certain amount between himself and the other
player.

See: Kahneman, Daniel, Jack L. Knetsch, and Richard H. Thaler. "Fairness
and the assumptions of economics." Journal of business (1986):
S285-S300.

"""


class Constants(BaseConstants):
    name_in_url = 'dictator_v21'
    players_per_group = 2
    num_rounds = 1

    instructions_template = 'dictator/Instructions.html'

    # Initial amount allocated to the dictator
    endowment = c(50)

    type_a1 = [1, 5, 9, 13, 17, 21, 25]  # ph1
    type_a2 = [23, 27, 3, 7, 11, 15, 19]  # ph2
    type_b = [26, 2, 6, 10, 14, 18, 22]  # pm
    type_c = [20, 24, 28, 4, 8, 12, 16]  # rh



class Subsession(BaseSubsession):
    def creating_session(self):
        print('in creating_session')

        new_structure = [[ 9,  4], [17, 20], [13, 24], [ 1, 12], [ 5, 16], [21,  8], [25, 28], [23, 10], [15, 26], [ 7,  2], [11, 14], [27,  6], [19, 22], [ 3, 18]]

        self.set_group_matrix(new_structure)
        print(self.get_group_matrix())


class Group(BaseGroup):
        pass


class Player(BasePlayer):

    participant_vars_dump = models.StringField()
    payoff = models.CurrencyField()

    def get_partner(self):
        return self.get_others_in_group()[0]

    kept = models.CurrencyField(
        doc="""Amount dictator decided to keep for himself""",
        min=0, max=Constants.endowment,
    )

    sent = models.CurrencyField(
        doc="""Amount dictator decided to keep for himself""",
        min=0, max=Constants.endowment,
    )

    subject_id = models.IntegerField(min=0, max=28, label='Subject ID')

    def set_type(self):
        self.subject_id = self.participant.id_in_session
        self.participant.vars['subject_id'] = self.subject_id
        if self.participant.vars['subject_id'] in Constants.type_a1:
            self.participant.vars['type'] = 1
        elif self.participant.vars['subject_id'] in Constants.type_a2:
            self.participant.vars['type'] = 2
        elif self.participant.vars['subject_id'] in Constants.type_b:
            self.participant.vars['type'] = 3
        elif self.participant.vars['subject_id'] in Constants.type_c:
            self.participant.vars['type'] = 4
        print('player belongs to category type:', self.participant.vars['type'])