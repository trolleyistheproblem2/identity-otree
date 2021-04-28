from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    timeout_seconds = 600


class Offer(Page):
    form_model = 'player'
    form_fields = ['amount_offered']

    def is_displayed(self):
        return True

    timeout_seconds = 600


class WaitForProposer(WaitPage):
    pass


class AcceptStrategy(Page):
    form_model = 'player'
    form_fields = ['response_{}'.format(int(i)) for i in
                   Constants.offer_choices]

    def is_displayed(self):
        return True


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass

class Process(Page):
    def before_next_page(self):
        return self.player.set_payoffs()


class Results(Page):
    pass


page_sequence = [Introduction,
                 Offer,
                 WaitForProposer,
                 AcceptStrategy,
                 ResultsWaitPage,
                 Process,
                 Results]
