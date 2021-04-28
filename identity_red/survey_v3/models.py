from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import itertools
from statistics import median


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



class Constants(BaseConstants):
    name_in_url = 'survey_v3'
    players_per_group = None
    num_rounds = 1
    type_a1 = [1, 5, 9, 13, 17, 21, 25]  # ph1
    type_a2 = [23, 27, 3, 7, 11, 25, 19]  # ph2
    type_b = [26, 2, 6, 10, 14, 18, 22]  # pm
    type_c = [20, 24, 28, 4, 8, 12, 16]  # rh

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    gender = models.StringField(
        choices=['Male', 'Female', 'Other'],
        label='What is your gender?',
        widget=widgets.RadioSelectHorizontal)

    age = models.IntegerField(min=0,max=100,label='What is your age?', choices=range(18,100))

    religion = models.StringField(choices=['Hindu', 'Muslim', 'Christian', 'Parsi', 'Jain', 'Sikh', 'Others'],
                                  widget=widgets.RadioSelectHorizontal,
                                  label='What religion have you been brought up with?')

    income = models.StringField(choices=['High Income', 'Low Income'],
                                widget=widgets.RadioSelectHorizontal,
                                label='''What is your family's income level?''')

    # tuition = models.IntegerField(choices=[500,1000,2000],
    #                               widget=widgets.RadioSelectHorizontal,
    #                                 label='''What is your college's monthly tuition fee. Enter the number closest to your knowledge.''')

    # languages = models.StringField(choices=['English', 'Hindi', 'Marathi'],
    #                            widget=widgets.RadioSelectHorizontal,
    #                            label='What languages do you speak?')

    def set_all_in_vars(self):
        self.participant.vars['gender'] = self.gender
        self.participant.vars['age'] = self.age
        self.participant.vars['religion'] = self.religion
        self.participant.vars['income'] = self.income
        print(self.participant.vars)

    subject_id = models.IntegerField(min=0, max=28, label='Subject ID')

    def set_type(self):
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

    # def set_payoffs(self):
    #     group_members = self.get_others_in_group()

    age1_1 = models.IntegerField(label='''Please enter your guess for this table member's age''')
    age1_2 = models.IntegerField(label='''Please enter your guess for this table member's age''')
    age1_3 = models.IntegerField(label='''Please enter your guess for this table member's age''')
    age1_4 = models.IntegerField(label='''Please enter your guess for this table member's age''')
    age2_1 = models.IntegerField(label='''Please enter your guess for this table member's age''')
    age2_2 = models.IntegerField(label='''Please enter your guess for this table member's age''')
    age2_3 = models.IntegerField(label='''Please enter your guess for this table member's age''')
    age2_4 = models.IntegerField(label='''Please enter your guess for this table member's age''')
    age3_1 = models.IntegerField(label='''Please enter your guess for this table member's age''')
    age3_2 = models.IntegerField(label='''Please enter your guess for this table member's age''')
    age3_3 = models.IntegerField(label='''Please enter your guess for this table member's age''')
    age3_4 = models.IntegerField(label='''Please enter your guess for this table member's age''')
    age4_1 = models.IntegerField(label='''Please enter your guess for this table member's age''')
    age4_2 = models.IntegerField(label='''Please enter your guess for this table member's age''')
    age4_3 = models.IntegerField(label='''Please enter your guess for this table member's age''')
    age4_4 = models.IntegerField(label='''Please enter your guess for this table member's age''')

    gender1_1 = models.StringField(choices=['Male', 'Female', 'Other'],
                                   label='''Please enter your guess for this table member's gender''')
    gender1_2 = models.StringField(choices=['Male', 'Female', 'Other'],
                                   label='''Please enter your guess for this table member's gender''')
    gender1_3 = models.StringField(choices=['Male', 'Female', 'Other'],
                                   label='''Please enter your guess for this table member's gender''')
    gender1_4 = models.StringField(choices=['Male', 'Female', 'Other'],
                                   label='''Please enter your guess for this table member's gender''')
    gender2_1 = models.StringField(choices=['Male', 'Female', 'Other'],
                                   label='''Please enter your guess for this table member's gender''')
    gender2_2 = models.StringField(choices=['Male', 'Female', 'Other'],
                                   label='''Please enter your guess for this table member's gender''')
    gender2_3 = models.StringField(choices=['Male', 'Female', 'Other'],
                                   label='''Please enter your guess for this table member's gender''')
    gender2_4 = models.StringField(choices=['Male', 'Female', 'Other'],
                                   label='''Please enter your guess for this table member's gender''')
    gender3_1 = models.StringField(choices=['Male', 'Female', 'Other'],
                                   label='''Please enter your guess for this table member's gender''')
    gender3_2 = models.StringField(choices=['Male', 'Female', 'Other'],
                                   label='''Please enter your guess for this table member's gender''')
    gender3_3 = models.StringField(choices=['Male', 'Female', 'Other'],
                                   label='''Please enter your guess for this table member's gender''')
    gender3_4 = models.StringField(choices=['Male', 'Female', 'Other'],
                                   label='''Please enter your guess for this table member's gender''')
    gender4_1 = models.StringField(choices=['Male', 'Female', 'Other'],
                                   label='''Please enter your guess for this table member's gender''')
    gender4_2 = models.StringField(choices=['Male', 'Female', 'Other'],
                                   label='''Please enter your guess for this table member's gender''')
    gender4_3 = models.StringField(choices=['Male', 'Female', 'Other'],
                                   label='''Please enter your guess for this table member's gender''')
    gender4_4 = models.StringField(choices=['Male', 'Female', 'Other'],
                                   label='''Please enter your guess for this table member's gender''')

    religion1_1 = models.StringField(choices=['Hindu', 'Muslim', 'Christian', 'Parsi', 'Jain', 'Sikh', 'Others'],
                                     label='''Please enter your guess for this table member's religion''')
    religion1_2 = models.StringField(choices=['Hindu', 'Muslim', 'Christian', 'Parsi', 'Jain', 'Sikh', 'Others'],
                                     label='''Please enter your guess for this table member's religion''')
    religion1_3 = models.StringField(choices=['Hindu', 'Muslim', 'Christian', 'Parsi', 'Jain', 'Sikh', 'Others'],
                                     label='''Please enter your guess for this table member's religion''')
    religion1_4 = models.StringField(choices=['Hindu', 'Muslim', 'Christian', 'Parsi', 'Jain', 'Sikh', 'Others'],
                                     label='''Please enter your guess for this table member's religion''')
    religion2_1 = models.StringField(choices=['Hindu', 'Muslim', 'Christian', 'Parsi', 'Jain', 'Sikh', 'Others'],
                                     label='''Please enter your guess for this table member's religion''')
    religion2_2 = models.StringField(choices=['Hindu', 'Muslim', 'Christian', 'Parsi', 'Jain', 'Sikh', 'Others'],
                                     label='''Please enter your guess for this table member's religion''')
    religion2_3 = models.StringField(choices=['Hindu', 'Muslim', 'Christian', 'Parsi', 'Jain', 'Sikh', 'Others'],
                                     label='''Please enter your guess for this table member's religion''')
    religion2_4 = models.StringField(choices=['Hindu', 'Muslim', 'Christian', 'Parsi', 'Jain', 'Sikh', 'Others'],
                                     label='''Please enter your guess for this table member's religion''')
    religion3_1 = models.StringField(choices=['Hindu', 'Muslim', 'Christian', 'Parsi', 'Jain', 'Sikh', 'Others'],
                                     label='''Please enter your guess for this table member's religion''')
    religion3_2 = models.StringField(choices=['Hindu', 'Muslim', 'Christian', 'Parsi', 'Jain', 'Sikh', 'Others'],
                                     label='''Please enter your guess for this table member's religion''')
    religion3_3 = models.StringField(choices=['Hindu', 'Muslim', 'Christian', 'Parsi', 'Jain', 'Sikh', 'Others'],
                                     label='''Please enter your guess for this table member's religion''')
    religion3_4 = models.StringField(choices=['Hindu', 'Muslim', 'Christian', 'Parsi', 'Jain', 'Sikh', 'Others'],
                                     label='''Please enter your guess for this table member's religion''')
    religion4_1 = models.StringField(choices=['Hindu', 'Muslim', 'Christian', 'Parsi', 'Jain', 'Sikh', 'Others'],
                                     label='''Please enter your guess for this table member's religion''')
    religion4_2 = models.StringField(choices=['Hindu', 'Muslim', 'Christian', 'Parsi', 'Jain', 'Sikh', 'Others'],
                                     label='''Please enter your guess for this table member's religion''')
    religion4_3 = models.StringField(choices=['Hindu', 'Muslim', 'Christian', 'Parsi', 'Jain', 'Sikh', 'Others'],
                                     label='''Please enter your guess for this table member's religion''')
    religion4_4 = models.StringField(choices=['Hindu', 'Muslim', 'Christian', 'Parsi', 'Jain', 'Sikh', 'Others'],
                                     label='''Please enter your guess for this table member's religion''')

    income1_1 = models.StringField(choices=['High Income', 'Low Income'],
                                   label='''Please enter your guess for this table member's income''')
    income1_2 = models.StringField(choices=['High Income', 'Low Income'],
                                   label='''Please enter your guess for this table member's income''')
    income1_3 = models.StringField(choices=['High Income', 'Low Income'],
                                   label='''Please enter your guess for this table member's income''')
    income1_4 = models.StringField(choices=['High Income', 'Low Income'],
                                   label='''Please enter your guess for this table member's income''')
    income2_1 = models.StringField(choices=['High Income', 'Low Income'],
                                   label='''Please enter your guess for this table member's income''')
    income2_2 = models.StringField(choices=['High Income', 'Low Income'],
                                   label='''Please enter your guess for this table member's income''')
    income2_3 = models.StringField(choices=['High Income', 'Low Income'],
                                   label='''Please enter your guess for this table member's income''')
    income2_4 = models.StringField(choices=['High Income', 'Low Income'],
                                   label='''Please enter your guess for this table member's income''')
    income3_1 = models.StringField(choices=['High Income', 'Low Income'],
                                   label='''Please enter your guess for this table member's income''')
    income3_2 = models.StringField(choices=['High Income', 'Low Income'],
                                   label='''Please enter your guess for this table member's income''')
    income3_3 = models.StringField(choices=['High Income', 'Low Income'],
                                   label='''Please enter your guess for this table member's income''')
    income3_4 = models.StringField(choices=['High Income', 'Low Income'],
                                   label='''Please enter your guess for this table member's income''')
    income4_1 = models.StringField(choices=['High Income', 'Low Income'],
                                   label='''Please enter your guess for this table member's income''')
    income4_2 = models.StringField(choices=['High Income', 'Low Income'],
                                   label='''Please enter your guess for this table member's income''')
    income4_3 = models.StringField(choices=['High Income', 'Low Income'],
                                   label='''Please enter your guess for this table member's income''')
    income4_4 = models.StringField(choices=['High Income', 'Low Income'],
                                   label='''Please enter your guess for this table member's income''')









