import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Kevin London', 'kevinlondon@gmail.com'),
)

MANAGERS = ADMINS
TIME_ZONE = 'America/Los_Angeles'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, MEDIA_URL.strip("/"))

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, STATIC_URL.strip("/"))

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.expanduser('~/Dropbox/programming/webdev/FontAwesome'),
    os.path.expanduser('~/Dropbox/programming/webdev/twitter-bootstrap'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'j(2mk1cvkhur6#y1(w$0dvltt*5(ept^djeq5x*3@&amp;xyq3iarm'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'kevinlondon.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'kevinlondon.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, "templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'south',
    'taggit',
    'imagekit',
    'disqus',
    'tinymce',
    'blog',
    'about',
)

DISQUS_API_KEY = 'jTtJ8wb56nB04VTC3bQDYLrw0l8A66oBQdR36T7Oj7aTDmArFnDlRYQDSR8Tcywq'
DISQUS_WEBSITE_SHORTNAME = 'klondonblog'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

try:
    from local_settings import *
except ImportError:
    pass

# TinyMCE settings
TINYMCE_COMPRESSOR = True
TINYMCE_DEFAULT_CONFIG = {
    'width': '760',
    'height': '480',
    'plugins': 'fullscreen,media,preview',
    'theme': 'advanced',
    'relative_urls': False,
    'theme_advanced_toolbar_location': 'top',
    'theme_advanced_toolbar_align': 'left',
    'theme_advanced_buttons1': 'bold,italic,underline,strikethrough,|,' \
        'justifyleft,justifycenter,justifyright,justifyfull,|,forecolor,' \
        'formatselect,|,bullist,numlist,|,' \
        'indent,outdent,|,link,unlink,anchor,image,media,|,visualaid,code,' \
        'preview,fullscreen',
    'theme_advanced_buttons2': 'undo,redo,|,cut,copy,paste,pasteword,' \
        'pastetext,selectall,|,cleanup,help,|,hr',
    'theme_advanced_buttons3': '',
    'theme_advanced_blockformats': 'p,pre,address,blockquote,h1,h2,h3,h4,' \
        'h5,h6',
    'plugin_preview_width' : '800',
    'plugin_preview_height' : '600',
    'paste_auto_cleanup_on_paste': 'true',
    }

