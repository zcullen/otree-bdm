import os
from os import environ

import dj_database_url
from boto.mturk import qualification

import otree.settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'static'),
#)

# the environment variable OTREE_PRODUCTION controls whether Django runs in
# DEBUG mode. If OTREE_PRODUCTION==1, then DEBUG=False
if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
else:
    DEBUG = True

if environ.get('SPLIT_CHATS') not in {True, '1'}:
    SPLIT = False
else:
    SPLIT = True



# don't share this with anybody.
SECRET_KEY = '62qe!ca719!_t#xhlo-^)x%o^748x5o^zub@7+znt)7ivpfp7k'


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
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')
CHANNEL_ROUTING = 'transcription.routing.channel_routing'

# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')


# e.g. EUR, CAD, GBP, CHF, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False



# e.g. en, de, fr, it, ja, zh-hans
# see: https://docs.djangoproject.com/en/1.9/topics/i18n/#term-language-code
LANGUAGE_CODE = 'en'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

# SENTRY_DSN = ''

DEMO_PAGE_INTRO_TEXT = """
<p>
    This is the control panel for all of the oTree games issued by Zoe and Bobby.
</p>
"""

ROOMS = [
    {
        'name': 'transcription_room',
        'display_name': 'Transcription Room',
        'participant_label_file': '_rooms/trans.txt',
    }
]


# from here on are qualifications requirements for workers
# see description for requirements on Amazon Mechanical Turk website:
# http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_QualificationRequirementDataStructureArticle.html
# and also in docs for boto:
# https://boto.readthedocs.org/en/latest/ref/mturk.html?highlight=mturk#module-boto.mturk.qualification

mturk_hit_settings = {
    'keywords': ['transcription', 'bonus', 'negotiation', 'study'],
    'title': 'Management and Transcription',
    'description': 'You will be assigned to either manage or directly carry out transcription',
    'frame_height': 600,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 48*60,
    'expiration_hours': 7*24, # 7 days
#   'grant_qualification_id': '3NF07PFA1K2EGWJFNBQ4JN81TXKETV',# to prevent retakes FOR REAL
#    'grant_qualification_id': '3VFIQRXYYK60OWH5USLZQ69Z1BU2ZB', ## sandbox
#    'qualification_requirements': [
#         qualification.LocaleRequirement("EqualTo", "US"),
#         qualification.PercentAssignmentsApprovedRequirement("GreaterThanOrEqualTo", 50),
        # qualification.NumberHitsApprovedRequirement("GreaterThanOrEqualTo", 5),
#        qualification.Requirement('2F1QJWKUDD8XADTFD2Q0G6UTO95ALH', 'Exists'),   # MASTER
#        qualification.Requirement('3B9KD9M9B0GOWZ0N4GFJ74F19NXNJR', 'Exists') # Follow up survey qual
#        qualification.Requirement('3NF07PFA1K2EGWJFNBQ4JN81TXKETV', 'DoesNotExist') # UNCOMMENT FOR REAL
#        qualification.Requirement('3VFIQRXYYK60OWH5USLZQ69Z1BU2ZB', 'DoesNotExist')  # SANDBOX
#    ]
}


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.00,
    'participation_fee': 1.00,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
}

SESSION_CONFIGS = [
    {
        'name': 'transcription_survey',
        'display_name': "Transcription Survey",
        'num_demo_participants': 8,
#        'app_sequence': ['trx_survey','transcription','exit_survey'],
        'app_sequence': ['trx_survey','transcription'],
#        'use_browser_bots': True,
    },
    {
        'name': 'transcription',
        'display_name': "Transcription",
        'num_demo_participants': 4,
        'app_sequence': ['transcription','exit_survey'],
#        'use_browser_bots': True,
    },
    {
        'name': 'exit_survey',
        'display_name': "Transcription Exit Survey",
        'num_demo_participants': 1,
        'app_sequence': ['exit_survey'],
#        'use_browser_bots': True,
    },
{
        'name': 'traits',
        'display_name': "Traits",
        'num_demo_participants': 2,
        'app_sequence': ['traits'],
#        'use_browser_bots': True,
    },


]

SENTRY_DSN = 'http://52dc63bdd6d54a8f88a5cfa8466abab6:dc115bfc45e345089428f88fda13e2ae@sentry.otree.org/157'

# anything you put after the below line will override
# oTree's default settings. Use with caution.
otree.settings.augment_settings(globals())
