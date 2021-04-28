from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    # form_model = 'player'
    # form_fields = ['subject_id']
    #
    # def before_next_page(self):
    #     self.player.set_type()

    def is_displayed(self):
        return self.subsession.round_number == 1

class MakingGroups2(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.subsession.do_my_shuffle()


class Offer(Page):
    form_model = 'player'
    form_fields = ['amount_offered']

    def is_displayed(self):
        return True

    def vars_for_template(self):
        return {


            'partner_type': self.player.get_partner().participant.vars['type'],


            'player_type': self.player.participant.vars['type'],

        }


class WaitForProposer(WaitPage):
    pass


class AcceptStrategy(Page):
    form_model = 'player'
    form_fields = ['response_{}'.format(int(i)) for i in
                   Constants.offer_choices]

    def is_displayed(self):
        return True

    def vars_for_template(self):
        return {


            'partner_type': self.player.get_partner().participant.vars['type'],


            'player_type': self.player.participant.vars['type'],

        }


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass

class Process(Page):
    def before_next_page(self):
        return self.player.set_payoffs()


class Results(Page):
    pass


page_sequence = [Introduction,
                 MakingGroups2,
                 Offer,
                 WaitForProposer,
                 AcceptStrategy,
                 ResultsWaitPage,
                 Process,
                 Results]
