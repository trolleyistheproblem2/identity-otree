import os
from os import environ

import dj_database_url

import otree.settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# the environment variable OTREE_PRODUCTION controls whether Django runs in
# DEBUG mode. If OTREE_PRODUCTION==1, then DEBUG=False
if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
else:
    DEBUG = True

ADMIN_USERNAME = 'admin'

# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

# don't share this with anybody.
SECRET_KEY = 'ww=aou-+#*wmi*-0tenz5j*%4)%0c9$y%(vp0$k69vunf@!8kx'

DATABASES = {
    'default': dj_database_url.config(
        # Rather than hardcoding the DB parameters here,
        # it's recommended to set the DATABASE_URL environment variable.
        # This will allow you to use SQLite locally, and postgres/mysql
        # on the server
        # Examples:
        # export DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
        # export DATABASE_URL=mysql://USER:PASSWORD@HOST:PORT/NAME

        # fall back to SQLite if the DATABASE_URL env var is missing
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}

# AUTH_LEVEL:
# If you are launching a study and want visitors to only be able to
# play your app if you provided them with a start link, set the
# environment variable OTREE_AUTH_LEVEL to STUDY.
# If you would like to put your site online in public demo mode where
# anybody can play a demo version of your game, set OTREE_AUTH_LEVEL
# to DEMO. This will allow people to play in demo mode, but not access
# the full admin interface.

AUTH_LEVEL = environ.get('DEMO')

# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')


# e.g. EUR, CAD, GBP, CHF, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'INR'
USE_POINTS = False


# e.g. en, de, fr, it, ja, zh-hans
# see: https://docs.djangoproject.com/en/1.9/topics/i18n/#term-language-code
LANGUAGE_CODE = 'en'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

# SENTRY_DSN = ''

DEMO_PAGE_INTRO_TEXT = """
oTree games
"""

mturk_hit_settings = {
    'keywords': ['easy', 'bonus', 'choice', 'study'],
    'title': 'Title for your experiment',
    'description': 'Description for your experiment',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7*24,  # 7 days
    # 'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    # to use qualification requirements, you need to uncomment the 'qualification' import
    # at the top of this file.
    'qualification_requirements': [],
}

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.000,
    'participation_fee': 0.00,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
}



SESSION_CONFIGS = [
    {
        'name': 'dictator_scribble',
        'display_name': "dictator_scribble",
        'num_demo_participants': 4,
        'app_sequence': ['dictator_v21'],
    },

    {
        'name': 'ultimatum_v31',
        'display_name': "ultimatum_v31",
        'num_demo_participants': 4,
        'treatment': 'use_strategy_method',
        'app_sequence': [ 'ultimatum_v31'],
    },
    {
        'name': 'full',
        'display_name': "full_final",
        'num_demo_participants': 4,
        'treatment': 'use_strategy_method',
        'app_sequence': ['voting','survey_v3','essay', 'dictator_test','ultimatum_final'],
    },
    {
        'name': 'voting',
        'display_name': "voting",
        'num_demo_participants': 4,

        'app_sequence': ['voting'],
    },
    {
        'name': 'essay',
        'display_name': "essay",
        'num_demo_participants': 4,
        'app_sequence': ['survey_v3','essay','dictator_test','ultimatum_final'],
    },
    {
        'name': 'behavioral',
        'display_name': "behavioral",
        'num_demo_participants': 28,
        'app_sequence': ['voting','survey_v3','essay','dictator_v21', 'ultimatum_v31', 'dictator_v22','ultimatum_v32', 'dictator_v23','ultimatum_v33','payment'],
    },



    ]

SENTRY_DSN = 'http://0638ebe73b304148a286dbff5ad15e6a:fe63057203584bb58346673319400f0e@sentry.otree.org/250'

# anything you put after the below line will override
# oTree's default settings. Use with caution.
otree.settings.augment_settings(globals())
