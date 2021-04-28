from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class SubjectID(Page):
    form_model = 'player'
    form_fields = ['subject_id']

    def is_displayed(self):
        return self.subsession.round_number == 1

    def before_next_page(self):
        return self.player.set_type()

class Intro(Page):
    def is_displayed(self):
        return True

class PhotoWaitPage(WaitPage):
    wait_for_all_groups = False
    def after_all_players_arrive(self):
        pass


class Rank(Page):
    form_model = 'player'
    form_fields = ['rank1', 'rank2', 'rank3', 'rank4']

    timeout_submission = {'rank1': 1, 'rank2': 2, 'rank3': 3, 'rank4': 4}

    def vars_for_template(self):
        p1 = self.group.get_player_by_id(1)
        p2 = self.group.get_player_by_id(2)
        p3 = self.group.get_player_by_id(3)
        p4 = self.group.get_player_by_id(4)
        return {
            'image_path1': 'voting/B{}.jpg'.format(p1.subject_id),
            'image_path2': 'voting/B{}.jpg'.format(p2.subject_id),
            'image_path3': 'voting/B{}.jpg'.format(p3.subject_id),
            'image_path4': 'voting/B{}.jpg'.format(p4.subject_id),
            'player_type': self.player.participant.vars['type'],
        }

    def error_message(self, values):
        print('values is', values)
        if values["rank1"] == values["rank2"]:
            return 'You cannot give the same rank to more than 1 candidate'
        elif values["rank1"] == values["rank3"]:
            return 'You cannot give the same rank to more than 1 candidate'
        elif values["rank1"] == values["rank4"]:
            return 'You cannot give the same rank to more than 1 candidate'
        elif values["rank2"] == values["rank3"]:
            return 'You cannot give the same rank to more than 1 candidate'
        elif values["rank2"] == values["rank4"]:
            return 'You cannot give the same rank to more than 1 candidate'
        elif values["rank3"] == values["rank4"]:
            return 'You cannot give the same rank to more than 1 candidate'



class Rank1(Page):
    form_model = 'player'
    form_fields = [ 'rank2', 'rank3', 'rank4']

    timeout_submission = { 'rank2': 2, 'rank3': 3, 'rank4': 4}

    def is_displayed(self):
        return self.player.id_in_group == 1

    def vars_for_template(self):
        p1 = self.group.get_player_by_id(1)
        p2 = self.group.get_player_by_id(2)
        p3 = self.group.get_player_by_id(3)
        p4 = self.group.get_player_by_id(4)
        return {
            'image_path1': 'voting/B{}.jpg'.format(p1.subject_id),
            'image_path2': 'voting/B{}.jpg'.format(p2.subject_id),
            'image_path3': 'voting/B{}.jpg'.format(p3.subject_id),
            'image_path4': 'voting/B{}.jpg'.format(p4.subject_id),
            'player_type': self.player.participant.vars['type'],
        }

    def error_message(self, values):
        print('values is', values)
        if values["rank2"] == values["rank3"]:
            return 'You cannot give the same rank to more than 1 candidate'
        elif values["rank2"] == values["rank4"]:
            return 'You cannot give the same rank to more than 1 candidate'
        elif values["rank3"] == values["rank4"]:
            return 'You cannot give the same rank to more than 1 candidate'

class Rank2(Page):
    form_model = 'player'
    form_fields = ['rank1',  'rank3', 'rank4']

    timeout_submission = {'rank1': 1, 'rank3': 3, 'rank4': 4}

    def is_displayed(self):
        return self.player.id_in_group == 2

    def vars_for_template(self):
        p1 = self.group.get_player_by_id(1)
        p2 = self.group.get_player_by_id(2)
        p3 = self.group.get_player_by_id(3)
        p4 = self.group.get_player_by_id(4)
        return {
            'image_path1': 'voting/B{}.jpg'.format(p1.subject_id),
            'image_path2': 'voting/B{}.jpg'.format(p2.subject_id),
            'image_path3': 'voting/B{}.jpg'.format(p3.subject_id),
            'image_path4': 'voting/B{}.jpg'.format(p4.subject_id),
            'player_type': self.player.participant.vars['type'],
        }

    def error_message(self, values):
        print('values is', values)
        if values["rank1"] == values["rank3"]:
            return 'You cannot give the same rank to more than 1 candidate'
        elif values["rank1"] == values["rank4"]:
            return 'You cannot give the same rank to more than 1 candidate'
        elif values["rank3"] == values["rank4"]:
            return 'You cannot give the same rank to more than 1 candidate'

class Rank3(Page):
    form_model = 'player'
    form_fields = ['rank1', 'rank2', 'rank4']

    timeout_submission = {'rank1': 1, 'rank2': 2, 'rank4': 4}

    def is_displayed(self):
        return self.player.id_in_group == 3

    def vars_for_template(self):
        p1 = self.group.get_player_by_id(1)
        p2 = self.group.get_player_by_id(2)
        p3 = self.group.get_player_by_id(3)
        p4 = self.group.get_player_by_id(4)
        return {
            'image_path1': 'voting/B{}.jpg'.format(p1.subject_id),
            'image_path2': 'voting/B{}.jpg'.format(p2.subject_id),
            'image_path3': 'voting/B{}.jpg'.format(p3.subject_id),
            'image_path4': 'voting/B{}.jpg'.format(p4.subject_id),
            'player_type': self.player.participant.vars['type'],
        }

    def error_message(self, values):
        print('values is', values)
        if values["rank1"] == values["rank2"]:
            return 'You cannot give the same rank to more than 1 candidate'
        elif values["rank1"] == values["rank4"]:
            return 'You cannot give the same rank to more than 1 candidate'
        elif values["rank2"] == values["rank4"]:
            return 'You cannot give the same rank to more than 1 candidate'

class Rank4(Page):
    form_model = 'player'
    form_fields = ['rank1', 'rank2', 'rank3']

    timeout_submission = {'rank1': 1, 'rank2': 2, 'rank3': 3}

    def is_displayed(self):
        return self.player.id_in_group == 4

    def vars_for_template(self):
        p1 = self.group.get_player_by_id(1)
        p2 = self.group.get_player_by_id(2)
        p3 = self.group.get_player_by_id(3)
        p4 = self.group.get_player_by_id(4)
        return {
            'image_path1': 'voting/B{}.jpg'.format(p1.subject_id),
            'image_path2': 'voting/B{}.jpg'.format(p2.subject_id),
            'image_path3': 'voting/B{}.jpg'.format(p3.subject_id),
            'image_path4': 'voting/B{}.jpg'.format(p4.subject_id),
            'player_type': self.player.participant.vars['type'],
        }

    def error_message(self, values):
        print('values is', values)
        if values["rank1"] == values["rank2"]:
            return 'You cannot give the same rank to more than 1 candidate'
        elif values["rank1"] == values["rank3"]:
            return 'You cannot give the same rank to more than 1 candidate'
        elif values["rank2"] == values["rank3"]:
            return 'You cannot give the same rank to more than 1 candidate'


class RankWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_winner()


class RankResult(Page):
    def is_displayed(self):
        return True



class Allocation(Page):

    form_model = 'player'
    form_fields = ['allocation1','allocation2', 'allocation3', 'allocation4']

    timeout_submission = {'allocation1': 50 ,'allocation2': 150, 'allocation3': 100, 'allocation4': 100}

    def vars_for_template(self):
        p1 = self.group.get_player_by_id(1)
        p2 = self.group.get_player_by_id(2)
        p3 = self.group.get_player_by_id(3)
        p4 = self.group.get_player_by_id(4)
        return {
            'image_path1': 'voting/B{}.jpg'.format(p1.subject_id),
            'image_path2': 'voting/B{}.jpg'.format(p2.subject_id),
            'image_path3': 'voting/B{}.jpg'.format(p3.subject_id),
            'image_path4': 'voting/B{}.jpg'.format(p4.subject_id)
        }

    def error_message(self, values):
        print('values is', values)
        if values["allocation1"] + values["allocation2"] + values["allocation3"] + values["allocation4"] != 400:
            return 'The total amount must add up to 400'

class AllocationWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoff()

class AllocationResult(Page):
    def is_displayed(self):
        return True
    def before_next_page(self):
        self.participant.vars['election_payoff'] = self.player.payoff


page_sequence = [
    SubjectID,
    Intro,
    PhotoWaitPage,
    Rank1,
    Rank2,
    Rank3,
    Rank4,
    RankWaitPage,
    RankResult,
    Allocation,
    AllocationWaitPage,
    AllocationResult,
]
