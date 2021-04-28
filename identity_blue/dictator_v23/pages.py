from ._builtin import Page, WaitPage
from .models import Constants
import random


class Introduction(Page):

    # form_model = 'player'
    # form_fields = ['subject_id']
    #
    # def before_next_page(self):
    #     self.player.set_type()

    def is_displayed(self):
        return self.subsession.round_number == 1
    #def before_next_page(self):


class MakingGroups2(WaitPage):
    wait_for_all_groups = True
    pass




class Offer(Page):
    form_model = 'player'
    form_fields = ['sent']
    timeout_submission = {'sent': 32}

    def before_next_page(self):
        self.player.participant_vars_dump = str(self.participant.vars)
        self.player.kept = Constants.endowment - self.player.sent

    #def is_displayed(self):
       # return self.player.id_in_group == 1

    def vars_for_template(self):
        return {

            'partner_type': self.player.get_partner().participant.vars['type'],


            'player_type': self.player.participant.vars['type'],

        }

    #def before_next_page(self):
     #   self.player.participant_vars_dump = str(self.participant.vars)

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        group = self.group
        player1 = group.get_player_by_id(1)
        player2 = group.get_player_by_id(2)

        player1.payoff = Constants.endowment - player2.kept + player1.kept
        player2.payoff = Constants.endowment - player1.kept + player2.kept
        player1.participant.vars['payoff_dictator'] = player1.payoff
        player2.participant.vars['payoff_dictator'] = player2.payoff

class Results(Page):
    def is_displayed(self):
        return True

    def before_next_page(self):
        self.participant.vars['dictator_round_3_payoff']= self.player.payoff

page_sequence = [
    Introduction,
    MakingGroups2,
    Offer,
    ResultsWaitPage,
    Results,

]
