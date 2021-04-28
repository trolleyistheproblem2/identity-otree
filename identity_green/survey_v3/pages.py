from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Welcome(Page):
    pass

    # form_model = 'player'
    # form_fields = ['subject_id']
    # def before_next_page(self):
    #     self.player.set_type()


class PreIntro(Page):
    pass

class Info(Page):
    form_model = 'player'
    form_fields = ['age','gender', 'religion', 'income']

    def before_next_page(self):
        self.player.set_all_in_vars()


class Others1(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1

    form_model = 'player'
    form_fields = ['age1_2', 'gender1_2', 'religion1_2', 'income1_2',
                   'age1_3', 'gender1_3', 'religion1_3', 'income1_3',
                   'age1_4', 'gender1_4', 'religion1_4', 'income1_4',
                   ]

    def vars_for_template(self):
        p1 = self.group.get_player_by_id(1)
        p2 = self.group.get_player_by_id(2)
        p3 = self.group.get_player_by_id(3)
        p4 = self.group.get_player_by_id(4)
        return {
            'image_path1': 'voting/G{}.jpg'.format(p1.participant.vars['subject_id']),
            'image_path2': 'voting/G{}.jpg'.format(p2.participant.vars['subject_id']),
            'image_path3': 'voting/G{}.jpg'.format(p3.participant.vars['subject_id']),
            'image_path4': 'voting/G{}.jpg'.format(p4.participant.vars['subject_id'])
        }

class Others2(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2

    form_model = 'player'
    form_fields = ['age2_3', 'gender2_3', 'religion2_3', 'income2_3',
                   'age2_1', 'gender2_1',  'religion2_1', 'income2_1',
                   'age2_4', 'gender2_4',  'religion2_4', 'income2_4',
                   ]

    def vars_for_template(self):
        p1 = self.group.get_player_by_id(1)
        p2 = self.group.get_player_by_id(2)
        p3 = self.group.get_player_by_id(3)
        p4 = self.group.get_player_by_id(4)
        return {
            'image_path1': 'voting/G{}.jpg'.format(p1.participant.vars['subject_id']),
            'image_path2': 'voting/G{}.jpg'.format(p2.participant.vars['subject_id']),
            'image_path3': 'voting/G{}.jpg'.format(p3.participant.vars['subject_id']),
            'image_path4': 'voting/G{}.jpg'.format(p4.participant.vars['subject_id'])
        }

class Others3(Page):
    def is_displayed(self):
        return self.player.id_in_group == 3

    form_model = 'player'
    form_fields = ['age3_2', 'gender3_2',  'religion3_2', 'income3_2',
                   'age3_1', 'gender3_1', 'religion3_1', 'income3_1',
                   'age3_4', 'gender3_4', 'religion3_4', 'income3_4',
                   ]

    def vars_for_template(self):
        p1 = self.group.get_player_by_id(1)
        p2 = self.group.get_player_by_id(2)
        p3 = self.group.get_player_by_id(3)
        p4 = self.group.get_player_by_id(4)
        return {
            'image_path1': 'voting/G{}.jpg'.format(p1.participant.vars['subject_id']),
            'image_path2': 'voting/G{}.jpg'.format(p2.participant.vars['subject_id']),
            'image_path3': 'voting/G{}.jpg'.format(p3.participant.vars['subject_id']),
            'image_path4': 'voting/G{}.jpg'.format(p4.participant.vars['subject_id'])
        }

class Others4(Page):
    def is_displayed(self):
        return self.player.id_in_group == 4

    form_model = 'player'
    form_fields = ['age4_2', 'gender4_2', 'religion4_2', 'income4_2',
                   'age4_3', 'gender4_3', 'religion4_3', 'income4_3',
                   'age4_1', 'gender4_1', 'religion4_1', 'income4_1',
                   ]

    def vars_for_template(self):
        p1 = self.group.get_player_by_id(1)
        p2 = self.group.get_player_by_id(2)
        p3 = self.group.get_player_by_id(3)
        p4 = self.group.get_player_by_id(4)
        return {
            'image_path1': 'voting/G{}.jpg'.format(p1.participant.vars['subject_id']),
            'image_path2': 'voting/G{}.jpg'.format(p2.participant.vars['subject_id']),
            'image_path3': 'voting/G{}.jpg'.format(p3.participant.vars['subject_id']),
            'image_path4': 'voting/G{}.jpg'.format(p4.participant.vars['subject_id'])
        }



class Result(Page):
    def vars_for_template(self):
        return {
            'player_age': self.player.participant.vars['age'],
            'player_type': self.player.participant.vars['type'],
            'player_religion': self.player.participant.vars['religion'],
        }


page_sequence = [
    Welcome,
    #PreIntro,
    Others1,
    Others2,
    Others3,
    Others4,
    Info,
     # Result
]
