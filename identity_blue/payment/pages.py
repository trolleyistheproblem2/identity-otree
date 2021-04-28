from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Calculate(Page):

    def before_next_page(self):
        return self.player.random_payments()



class Thanks(Page):

    form_model = ['player']
    form_fields = ['family_income','outfit','mother_tongue','english_fluency','hindi_fluency']

    # def before_next_page(self):
    #     return self.player.random_payments()


class Payment(Page):

    def vars_for_template(self):
        return {

            'election_winner': self.participant.vars['election_winner_id'],

            'election_payoff' : self.participant.vars['election_payoff'],

            'dictator_payoff': self.participant.vars['dictator_final_payoff'],
            'ultimatum_payoff': self.participant.vars['ultimatum_final_payoff'],
            'player_type': self.player.participant.vars['type'],

        }





page_sequence = [
    Calculate,
    Thanks,
    Payment
]
