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
    name_in_url = 'ultimatum_v33'
    players_per_group = 2
    num_rounds = 1

    instructions_template = 'ultimatum_final/Instructions.html'

    endowment = c(50)
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

        new_structure = [[21,  3], [17, 27], [ 1, 19], [25,  7], [13, 11], [ 5, 23], [ 9, 15], [14, 16], [26, 28], [22, 12], [ 2, 20], [18,  8], [10, 24], [ 6,  4]]

        self.set_group_matrix(new_structure)
        print(self.get_group_matrix())



def make_field(amount):
    return models.BooleanField(
        widget=widgets.RadioSelectHorizontal,
        label='Would you accept an offer of {}?'.format(c(amount)))


class Group(BaseGroup):
    use_strategy_method = models.BooleanField(initial=1,
        doc="""Whether this group uses strategy method"""
    )

    p1p2 = models.IntegerField()

    p2p1 = models.IntegerField( )

    def set_payoffs(self):

        if self.use_strategy_method:

            player1 = self.get_player_by_id(1)
            player2 = self.get_player_by_id(2)
            print(player1.sent)
            print(player2.sent)
            if player1.sent >= player2.reservation_price:
                    p1p2 = 1
                    print('we here?')
            else: p1p2 = 0

            if player2.sent >= player1.reservation_price:
                    p2p1 = 1
            else:
                p2p1 = 0
            print(p1p2,p2p1)


            if [p1p2,p2p1] == [1,1]:
                print('1,1')
                player1.payoff = Constants.endowment - player1.sent + player2.sent
                player2.payoff = Constants.endowment - player2.sent + player1.sent
                player1.participant.vars['ultimatum_round_1_payoff'] = player1.payoff
                player2.participant.vars['ultimatum_round_1_payoff'] = player2.payoff

            elif [p1p2,p2p1] == [1,0]:
                print('1,0')
                player1.payoff = Constants.endowment - player1.sent
                player2.payoff = player1.sent
                player1.participant.vars['ultimatum_round_1_payoff'] = player1.payoff
                player2.participant.vars['ultimatum_round_1_payoff'] = player2.payoff

            elif [p1p2,p2p1] == [0,1]:
                print('0,1')
                player1.payoff = player2.sent
                player2.payoff = Constants.endowment - player2.sent
                player1.participant.vars['ultimatum_round_1_payoff'] = player1.payoff
                player2.participant.vars['ultimatum_round_1_payoff'] = player2.payoff

            elif [p1p2,p2p1] == [0,0]:
                print('0,0')
                player1.payoff = c(0)
                player2.payoff = c(0)
                player1.participant.vars['ultimatum_round_1_payoff'] = player1.payoff
                player2.participant.vars['ultimatum_round_1_payoff'] = player2.payoff



class Player(BasePlayer):
    sent = models.CurrencyField(min=0, max=Constants.endowment)

    offer_accepted = models.BooleanField(
        doc="if offered amount is accepted (direct response method)"
    )

    subject_id= models.IntegerField()

    reservation_price = models.CurrencyField(min=0,max=Constants.endowment)

    # for strategy method, see the make_field function above
    # response_0 = make_field(0)
    # response_10 = make_field(10)
    # response_20 = make_field(20)
    # response_30 = make_field(30)
    # response_40 = make_field(40)
    # response_50 = make_field(50)
    # # response_60 = make_field(60)
    # # response_70 = make_field(70)
    # # response_80 = make_field(80)
    # # response_90 = make_field(90)
    # # response_100 = make_field(100)

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




