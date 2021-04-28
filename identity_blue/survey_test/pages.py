from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Welcome(Page):
    form_model = 'player'
    form_fields = ['subject_id']
    def before_next_page(self):
        self.player.set_type()


class PreIntro(Page):
    pass

class Info(Page):
    form_model = 'player'
    form_fields = ['income']

    def before_next_page(self):
        self.player.set_all_in_vars()

class MedianCalc(WaitPage):
    wait_for_all_groups = True
    def after_all_players_arrive(self):
        self.subsession.split_on_income()



class Result(Page):
    pass


page_sequence = [
    Welcome,
    #PreIntro,
    #Info,
    #MedianCalc,
    Result
]
