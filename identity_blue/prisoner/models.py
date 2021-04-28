from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random
from random import shuffle

doc = """
This is a one-shot "Prisoner's Dilemma". Two players are asked separately
whether they want to cooperate or defect. Their choices directly determine the
payoffs.
"""


class Constants(BaseConstants):
    name_in_url = 'prisoner'
    players_per_group = 2
    num_rounds = 6

    instructions1_template = 'prisoner/Instructions1.html'
    instructions2_template = 'prisoner/Instructions2.html'

    # payoff if 1 player defects and the other cooperates""",
    betray_payoff = c(300)
    betrayed_payoff = c(0)

    # payoff if both players cooperate or both defect
    both_cooperate_payoff = c(200)
    both_defect_payoff = c(100)


class Subsession(BaseSubsession):
    def creating_session(self):
        print('in creating_session PD')
        if self.round_number == 1:
            self.session.vars['choice_PD_1'] = random.randint(1, Constants.num_rounds)
            self.session.vars['selected_game_for_payoff'] = random.randint(1, 2)


    # payoff if 1 player defects and the other cooperates"""
    betray_payoff = models.CurrencyField(initial=120)
    betrayed_payoff = models.CurrencyField(initial=10)

    # payoff if both players cooperate or both defect
    both_cooperate_payoff = models.CurrencyField(initial=100)
    both_defect_payoff = models.CurrencyField(initial=20)

    chosen_game_type = models.IntegerField(min=1,max=2)

    def do_my_shuffle(self):
        # note: to use this function
        # you would need to call self.subsession.make_groups()
        # from somewhere, such as after_all_players_arrive

        if self.round_number == 1:
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
            print('Group Matrix for this', self.round_number, 'round is', group_matrix)

        elif self.round_number == 4:
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
                print('Group Matrix for this', self.round_number, 'round is', group_matrix)

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

        elif self.round_number == 5:
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

        elif self.round_number == 3:
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

        elif self.round_number == 6:
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

    def get_partner(self):
        return self.get_others_in_group()[0]


    decision = models.StringField(
        choices=['Cooperate', 'Defect'],
        doc="""This player's decision""",
        widget=widgets.RadioSelect
    )

    question1 = models.IntegerField(label= "How much you would earn if you pick MINUS and your partner picks MINUS?",
                                   choices=[[1,'100'],[2,'120'],[3,'10'],[4,'20']],
                                   widget=widgets.RadioSelect
                                   )

    question2 = models.IntegerField(label="How much you would earn if you pick PLUS and your partner picks PLUS?",
                                    choices=[[1, '10'], [2, '120'], [3, '100'], [4, '20']],
                                    widget=widgets.RadioSelect
                                    )

    question3 = models.IntegerField(label="How much will your partner earn if you pick MINUS and your partner picks PLUS?",
                                    choices=[[1, '20'], [2, '100'], [3, '120'], [4, '10']],
                                    widget=widgets.RadioSelect
                                    )



    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):


        payoff_matrix = {
            'Cooperate':
                {
                    'Cooperate': self.subsession.both_cooperate_payoff,
                    'Defect': self.subsession.betrayed_payoff
                },
            'Defect':
                {
                    'Cooperate': self.subsession.betray_payoff,
                    'Defect': self.subsession.both_defect_payoff
                }
        }

        if self.subsession.round_number == self.session.vars['choice_PD_1']:
            self.payoff = payoff_matrix[self.decision][self.other_player().decision]
            self.participant.vars['payoff_prisoner_sym'] = self.payoff
        else:
            self.payoff = 0

        print('payoff matrix is', payoff_matrix)

    session_vars_dump = models.StringField()


