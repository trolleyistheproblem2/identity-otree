from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'voting'
    players_per_group = 4
    num_others_per_group = players_per_group - 1
    num_rounds = 1
    type_a1 = [1,5,9,13,17,21,25]  # ph1
    type_a2 = [23,27,3,7,11,15,19]  # ph2
    type_b = [26,2,6,10,14,18,22]  # pm
    type_c = [20,24,28,4,8,12,16]  # rh


class Subsession(BaseSubsession):
    def creating_session(self):

        new_structure = [
                            [1, 23, 26, 20],
                            [5, 27, 2, 24],
                            [9, 3, 6, 28],
                            [13, 7, 10, 4],
                            [17, 11, 14, 8],
                            [21, 15, 18, 12],
                            [25, 19, 22, 16],
                         ]
        self.set_group_matrix(new_structure)
        print(self.get_group_matrix())


class Group(BaseGroup):
    winner_rank = models.IntegerField()

    sum_rank1 = models.IntegerField()
    sum_rank2 = models.IntegerField()
    sum_rank3 = models.IntegerField()
    sum_rank4 = models.IntegerField()

    winner_id = models.IntegerField()



    def set_winner(self):

        self.sum_rank1 = sum(p.rank1 for p in self.get_players())
        self.sum_rank2 = sum(p.rank2 for p in self.get_players())
        self.sum_rank3 = sum(p.rank3 for p in self.get_players())
        self.sum_rank4 = sum(p.rank4 for p in self.get_players())

        ranks = [self.sum_rank1, self.sum_rank2, self.sum_rank3, self.sum_rank4]
        sorted_ranks = sorted(ranks)
        print('votes are', sorted_ranks)
        self.winner_rank = sorted_ranks[0]
        if self.winner_rank == self.sum_rank1:
            self.winner_id = 1
        elif self.winner_rank == self.sum_rank2:
            self.winner_id = 2
        elif self.winner_rank == self.sum_rank3:
            self.winner_id = 3
        elif self.winner_rank == self.sum_rank4:
            self.winner_id = 4

        print('winner got votes:', self.winner_rank)
        print('Winner is', self.winner_id)



    def set_payoff(self):

        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p3 = self.get_player_by_id(3)
        p4 = self.get_player_by_id(4)



        if self.winner_id == 1:

            p1.payoff = p1.allocation1
            p2.payoff = p1.allocation2
            p3.payoff = p1.allocation3
            p4.payoff = p1.allocation4
            p1.participant.vars['election_winner_id'] = self.winner_id
            p2.participant.vars['election_winner_id'] = self.winner_id
            p3.participant.vars['election_winner_id'] = self.winner_id
            p4.participant.vars['election_winner_id'] = self.winner_id

            p1.participant.vars['election_p1_payoff'] = p1.payoff
            p2.participant.vars['election_p2_payoff'] = p2.payoff
            p3.participant.vars['election_p3_payoff'] = p3.payoff
            p4.participant.vars['election_p4_payoff'] = p4.payoff
            print(p1.participant.vars)
            print(p2.participant.vars)
            print(p3.participant.vars)
            print(p4.participant.vars)

        elif self.winner_id == 2:
            p1.payoff = p2.allocation1
            p2.payoff = p2.allocation2
            p3.payoff = p2.allocation3
            p4.payoff = p2.allocation4
            p1.participant.vars['election_winner_id'] = self.winner_id
            p2.participant.vars['election_winner_id'] = self.winner_id
            p3.participant.vars['election_winner_id'] = self.winner_id
            p4.participant.vars['election_winner_id'] = self.winner_id

            p1.participant.vars['election_p1_payoff'] = p1.payoff
            p2.participant.vars['election_p2_payoff'] = p2.payoff
            p3.participant.vars['election_p3_payoff'] = p3.payoff
            p4.participant.vars['election_p4_payoff'] = p4.payoff
            print(p1.participant.vars)
            print(p2.participant.vars)
            print(p3.participant.vars)
            print(p4.participant.vars)

        elif self.winner_id == 3:
            p1.payoff = p3.allocation1
            p2.payoff = p3.allocation2
            p3.payoff = p3.allocation3
            p4.payoff = p3.allocation4
            p1.participant.vars['election_winner_id'] = self.winner_id
            p2.participant.vars['election_winner_id'] = self.winner_id
            p3.participant.vars['election_winner_id'] = self.winner_id
            p4.participant.vars['election_winner_id'] = self.winner_id

            p1.participant.vars['election_p1_payoff'] = p1.payoff
            p2.participant.vars['election_p2_payoff'] = p2.payoff
            p3.participant.vars['election_p3_payoff'] = p3.payoff
            p4.participant.vars['election_p4_payoff'] = p4.payoff
            print(p1.participant.vars)
            print(p2.participant.vars)
            print(p3.participant.vars)
            print(p4.participant.vars)

        elif self.winner_id == 4:
            p1.payoff = p4.allocation1
            p2.payoff = p4.allocation2
            p3.payoff = p4.allocation3
            p4.payoff = p4.allocation4
            p1.participant.vars['election_winner_id'] = self.winner_id
            p2.participant.vars['election_winner_id'] = self.winner_id
            p3.participant.vars['election_winner_id'] = self.winner_id
            p4.participant.vars['election_winner_id'] = self.winner_id

            p1.participant.vars['election_p1_payoff'] = p1.payoff
            p2.participant.vars['election_p2_payoff'] = p2.payoff
            p3.participant.vars['election_p3_payoff'] = p3.payoff
            p4.participant.vars['election_p4_payoff'] = p4.payoff
            print(p1.participant.vars)
            print(p2.participant.vars)
            print(p3.participant.vars)
            print(p4.participant.vars)




class Player(BasePlayer):
    rank1 = models.IntegerField(min=1, max=3, label='Give a rank to Candidate 1', initial=0)

    rank2 = models.IntegerField(min=1, max=3, label='Give a rank to Candidate 2', initial=0)

    rank3 = models.IntegerField(min=1, max=3, label='Give a rank to Candidate 3', initial=0)

    rank4 = models.IntegerField(min=1, max=3, label='Give a rank to Candidate 4', initial=0)

    # rank1 = models.IntegerField(min=0, max=3, label='Give a rank to Candidate 1', widget=widgets.RadioSelectHorizontal,
    #                             choices=[[1, '1'], [2, '2'], [3, '3']], initial=3, blank=True)
    #
    # rank2 = models.IntegerField(min=0, max=3, label='Give a rank to Candidate 2', widget=widgets.RadioSelectHorizontal,
    #                             choices=[[1, '1'], [2, '2'], [3, '3']], initial=3, blank=True)
    #
    # rank3 = models.IntegerField(min=0, max=3, label='Give a rank to Candidate 3', widget=widgets.RadioSelectHorizontal,
    #                             choices=[[1, '1'], [2, '2'], [3, '3']], initial=3, blank=True)
    #
    # rank4 = models.IntegerField(min=0, max=3, label='Give a rank to Candidate 4', widget=widgets.RadioSelectHorizontal,
    #                             choices=[[1, '1'], [2, '2'], [3, '3']], initial=3, blank=True)

    allocation1 = models.IntegerField(min=0, max=400, label='Give an amount to Table Member 1')
    allocation2 = models.IntegerField(min=0, max=400, label='Give an amount to Table Member 2')
    allocation3 = models.IntegerField(min=0, max=400, label='Give an amount to Table Member 3')
    allocation4 = models.IntegerField(min=0, max=400, label='Give an amount to Table Member 4')

    subject_id = models.IntegerField(min=0,max=28, label='Subject ID')

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

    # def set_winner_in_vars(self):


