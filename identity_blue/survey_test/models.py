from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import itertools
from statistics import median


class Subsession(BaseSubsession):


    def creating_session(self):
        assert len(self.get_players()) % 2 == 0, 'The number of players should be even'



class Constants(BaseConstants):
    name_in_url = 'survey_test'
    players_per_group = None
    num_rounds = 1
    type_a1 = [15, 16, 17, 18, 19, 20, 21]
    type_a2 = [22, 23, 24, 25, 26, 27, 28]
    type_b = [1, 3, 5, 7, 9, 11, 13]
    type_c = [2, 4, 6, 8, 10, 12, 14]

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    subject_id = models.IntegerField(
        min=1,max=30,
        label='Subject ID'
    )

    gender = models.StringField(
        choices=['Male', 'Female'],
        label='What is your gender?',
        widget=widgets.RadioSelect)

    age = models.IntegerField(min=0,max=100,label='What is your age?', choices=range(18,100))

    city = models.StringField(choices=['Pune', 'Mumbai', 'Delhi', 'Chennai', 'Kolkata', 'Other'],
                              widget=widgets.RadioSelect,
                              label= 'What city are you residing in right now?')

    college = models.StringField(choices=['Poona College', 'Fergusson College', 'Bharti Vidyapeeth', 'Other'],
                                 widget=widgets.RadioSelect,
                                 label='What college are you studying in?')

    major = models.StringField(choices=['Economics', 'MBA', 'Other'],
                               widget=widgets.RadioSelect,
                               label='What is your major of study in college?')

    study_year = models.StringField(choices=['UG 1', 'UG 2', 'UG 3', 'UG 4', 'PG 1', 'PG 2', 'Other'],
                                    widget=widgets.RadioSelect,
                                    label='What year of your study are you in?')
    religion = models.StringField(choices=['Hindu', 'Muslim', 'Christian', 'Other'],
                                  widget=widgets.RadioSelect,
                                  label='What religion have you been brought up with?')

    income = models.IntegerField(min=0, max=100000000, label='''What is your family's monthly income?''')

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

    def set_all_in_vars(self):

        self.participant.vars['age'] = self.age
        self.participant.vars['city'] = self.city
        self.participant.vars['college'] = self.college
        self.participant.vars['major'] = self.major
        self.participant.vars['study_year'] = self.study_year
        self.participant.vars['religion'] = self.religion
        self.participant.vars['income'] = self.income








