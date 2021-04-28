from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

doc = """
Ultimatum game with two treatments: direct response and strategy method.
In the former, one player makes an offer and the other either accepts or rejects.
It comes in two flavors, with and without hypothetical questions about the second player's response to offers other than the one that is made.
In the latter treatment, the second player is given a list of all possible offers, and is asked which ones to accept or reject.
"""


class Constants(BaseConstants):
    name_in_url = 'ultimatum_final'
    players_per_group = 2
    num_rounds = 3

    instructions_template = 'ultimatum_final/Instructions.html'

    endowment = c(100)
    payoff_if_rejected = c(0)
    offer_increment = c(10)

    offer_choices = currency_range(0, endowment, offer_increment)
    offer_choices_count = len(offer_choices)

    type_a1 = [1, 5, 9, 13, 17, 21, 25]  # ph1
    type_a2 = [23, 27, 3, 7, 11, 15, 19]  # ph2
    type_b = [26, 2, 6, 10, 14, 18, 22]  # pm
    type_c = [20, 24, 28, 4, 8, 12, 16]  # rh


    keep_give_amounts = []
    for offer in offer_choices:
        keep_give_amounts.append((offer, endowment - offer))


class Subsession(BaseSubsession):
    def creating_session(self):
        # randomize to treatments
        for g in self.get_groups():
            if 'use_strategy_method' in self.session.config:
                g.use_strategy_method = self.session.config['use_strategy_method']
            else:
                g.use_strategy_method = random.choice([True])


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

            # pop elements from a1_players until it's empty
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


def make_field(amount):
    return models.BooleanField(
        widget=widgets.RadioSelectHorizontal,
        label='Would you accept an offer of {}?'.format(c(amount)))


class Group(BaseGroup):
    use_strategy_method = models.BooleanField(initial=1,
        doc="""Whether this group uses strategy method"""
    )


class Player(BasePlayer):
    amount_offered = models.CurrencyField(choices=Constants.offer_choices)

    offer_accepted = models.BooleanField(
        doc="if offered amount is accepted (direct response method)"
    )

    # for strategy method, see the make_field function above
    response_0 = make_field(0)
    response_10 = make_field(10)
    response_20 = make_field(20)
    response_30 = make_field(30)
    response_40 = make_field(40)
    response_50 = make_field(50)
    response_60 = make_field(60)
    response_70 = make_field(70)
    response_80 = make_field(80)
    response_90 = make_field(90)
    response_100 = make_field(100)

    # subject_id = models.IntegerField(min=0, max=28, label='Subject ID')

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

    def get_partner(self):
        return self.get_others_in_group()[0]

    def set_payoffs(self):

        if self.group.use_strategy_method:
            partner = self.get_others_in_group()[0]

            self.offer_accepted = getattr(self, 'response_{}'.format(
                int(self.amount_offered)))

            if self.offer_accepted:
                self.payoff = Constants.endowment - self.amount_offered + partner.amount_offered
