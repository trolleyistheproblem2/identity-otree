from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Enter(Page):
    def before_next_page(self):
        return self.player.set_essay_topic()
    # form_model = 'player'
    # form_fields = ['subject_id']

    # def before_next_page(self):
    #     self.player.set_type()

class Essay(Page):
    form_model = 'player'
    form_fields = ['essay_text']

    timeout_seconds = 300

    def vars_for_template(self):
        return {
            'essay_type': self.player.participant.vars['essay_topic']
        }

    # def error_message(self, values):
    #     print('values is', values)
    #     if len(values["essay_text"]) < 100 :
    #         return 'You must write more than a 100 characters.'

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Enter,
    Essay,
    Results
]
