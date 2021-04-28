from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Prime(Page):
    pass

class Introduction(Page):
    def is_displayed(self):
       return self.round_number == 1


class MakingGroups(WaitPage):
    wait_for_all_groups = True
    def after_all_players_arrive(self):
        self.subsession.do_my_shuffle()

class TrialQuestion(Page):
    def is_displayed(self):
        return self.round_number == 1

    form_model = 'player'
    form_fields = ['question1','question2','question3']

    def question1_error_message(self, question1):
        print('just checking', question1)
        if question1 != 4:
            return '''Wrong answer. Please try again! Make sure you've paid close attention to the table!'''

    def question2_error_message(self, question2):
        print('just checking', question2)
        if question2 != 3:
            return '''Wrong answer. Please try again! Make sure you've paid close attention to the table!'''

    def question3_error_message(self, question3):
        print('just checking', question3)
        if question3 != 4:
            return '''Wrong answer. Please try again! Make sure you've paid close attention to the table!'''



class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']
    timeout_submission = {'decision': 'Cooperate'}

    def vars_for_template(self):

        return{
            'partner_age': self.player.get_partner().participant.vars['age'],
            'partner_city': self.player.get_partner().participant.vars['city'],
            'partner_senior': self.player.get_partner().participant.vars['senior'],
            'partner_income': self.player.get_partner().participant.vars['income'],
            'partner_college': self.player.get_partner().participant.vars['college'],
            'partner_study_year': self.player.get_partner().participant.vars['study_year'],
            'partner_religion': self.player.get_partner().participant.vars['religion'],

            'player_age': self.player.participant.vars['age'],
            'player_city': self.player.participant.vars['city'],
            'player_senior': self.player.participant.vars['senior'],
            'player_income': self.player.participant.vars['income'],
            'player_college': self.player.participant.vars['college'],
            'player_study_year': self.player.participant.vars['study_year'],
            'player_religion': self.player.participant.vars['religion'],

        }

    def before_next_page(self):
        self.player.session_vars_dump = str(self.session.vars)


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()


class Results(Page):
    def is_displayed(self):
        return True

    def vars_for_template(self):
        me = self.player
        opponent = me.other_player()
        return {
            'my_decision': me.decision,
            'opponent_decision': opponent.decision,
            'same_choice': me.decision == opponent.decision,
        }


class PrimeRefresh(Page):
    form_model = 'player'
    form_fields = [ 'q5']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [
    Introduction,
    TrialQuestion,
    MakingGroups,
    Decision,
    ResultsWaitPage,
    Results
]
