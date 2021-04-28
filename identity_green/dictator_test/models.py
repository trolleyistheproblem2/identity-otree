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
    name_in_url = 'dictator_test'
    players_per_group = 2
    num_rounds = 3

    instructions_template = 'dictator/Instructions.html'

    # Initial amount allocated to the dictator
    endowment = c(100)

    type_a1 = [1, 5, 9, 13, 17, 21, 25]  # ph1
    type_a2 = [23, 27, 3, 7, 11, 15, 19]  # ph2
    type_b = [26, 2, 6, 10, 14, 18, 22]  # pm
    type_c = [20, 24, 28, 4, 8, 12, 16]  # rh



class Subsession(BaseSubsession):
    def creating_session(self):
        print('in creating_session')
        if self.round_number == 1:
            self.session.vars['choice_dictator_1'] = random.randint(1, Constants.num_rounds)

    def do_my_shuffle(self):
        # note: to use this function
        # you would need to call self.subsession.do_my_shuffle()
        # from somewhere, such as after_all_players_arrive


        if self.round_number == 3:
            players = self.get_players()

            a1_players = [p for p in players if p.participant.vars['type'] == 1]
            a2_players = [p for p in players if p.participant.vars['type'] == 2]
            b_players = [p for p in players if p.participant.vars['type'] == 3]
            c_players = [p for p in players if p.participant.vars['type'] == 4]

            random.shuffle(a1_players)
            random.shuffle(a2_players)
            random.shuffle(b_players)
            random.shuffle(c_players)
            print('shuffled a1', a1_players)
            print('shuffled a2', a2_players)
            print('shuffled b', b_players)
            print('shuffled c', c_players)

            group_matrix = []

            # pop elements from M_players until it's empty
            while a1_players:
                new_group = [
                    a1_players.pop(),
                    a2_players.pop(),
                            ]
                group_matrix.append(new_group)
            while b_players:
                new_group = [
                    b_players.pop(),
                    c_players.pop(),
                            ]
                group_matrix.append(new_group)

            self.set_group_matrix(group_matrix)
            print('Group Matrix for this',self.round_number,'round is',group_matrix)

        elif self.round_number == 2:
            players = self.get_players()

            a1_players = [p for p in players if p.participant.vars['type'] == 1]
            a2_players = [p for p in players if p.participant.vars['type'] == 2]
            b_players = [p for p in players if p.participant.vars['type'] == 3]
            c_players = [p for p in players if p.participant.vars['type'] == 4]

            random.shuffle(a1_players)
            random.shuffle(a2_players)
            random.shuffle(b_players)
            random.shuffle(c_players)
            print('shuffled a1', a1_players)
            print('shuffled a2', a2_players)
            print('shuffled b', b_players)
            print('shuffled c', c_players)

            group_matrix = []

            # pop elements from M_players until it's empty
            while a1_players:
                new_group = [
                    a1_players.pop(),
                    b_players.pop(),
                ]
                group_matrix.append(new_group)
            while a2_players:
                new_group = [
                    a2_players.pop(),
                    c_players.pop(),
                ]
                group_matrix.append(new_group)

            self.set_group_matrix(group_matrix)
            print('Group Matrix for this', self.round_number, 'round is', group_matrix)

        elif self.round_number == 1:
            players = self.get_players()

            a1_players = [p for p in players if p.participant.vars['type'] == 1]
            a2_players = [p for p in players if p.participant.vars['type'] == 2]
            b_players = [p for p in players if p.participant.vars['type'] == 3]
            c_players = [p for p in players if p.participant.vars['type'] == 4]

            random.shuffle(a1_players)
            random.shuffle(a2_players)
            random.shuffle(b_players)
            random.shuffle(c_players)
            print('shuffled a1', a1_players)
            print('shuffled a2', a2_players)
            print('shuffled b', b_players)
            print('shuffled c', c_players)

            group_matrix = []

            # pop elements from M_players until it's empty
            while a1_players:
                new_group = [
                    a1_players.pop(),
                    c_players.pop(),
                ]
                group_matrix.append(new_group)
            while a2_players:
                new_group = [
                    a2_players.pop(),
                    b_players.pop(),
                ]
                group_matrix.append(new_group)

            self.set_group_matrix(group_matrix)
            print('Group Matrix for this', self.round_number, 'round is', group_matrix)


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