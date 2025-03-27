# Here you can add custom options
# DEBUG = False

# ADMINS = (
#     ('Your Name', 'your_email@example.com'),
# )

# This is the contact email that will be shown in various places all over
# the site.
# CONTACT_EMAIL = 'mail@email.com'

# The port to run on.
# PORT = 4386

# Whether anyone surfing to the site can open an account.
# REGISTRATION_OPEN = True

# This determines whether there is a star labeled "Free" on the login page
# IS_FREE = True

# Local time zone for this installation. Keep UTC here, the frontend will
# translate this to the correct local time.
# TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
# LANGUAGE_CODE = 'en-us'

ACCOUNT_EMAIL_VERIFICATION = "optional"

# Send emails using an SMTP server
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'localhost'
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_PORT = 25
# EMAIL_SUBJECT_PREFIX = '[Fidus Writer]'
# EMAIL_USE_TLS = True # Port 587
# EMAIL_USE_SSL = True # Port 465
# DEFAULT_FROM_EMAIL = 'system@email.com'
# SERVER_EMAIL = 'system@email.com'


# A list of allowed hostnames of this Fidus Writer installation
# ALLOWED_HOSTS = [
#    'localhost',
# ]

# CSRF_TRUSTED_ORIGINS = []

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
# STATIC_URL = '/static/'

# To enable other plugins than the default ones, specify the plugins below
INSTALLED_APPS = [
    "user_template_manager",
    "book",
    "citation_api_import",
    "languagetool",
    "pandoc",
    # "ojs",
    # "phplist",
    # "gitrepo_export",
    # "website",
]

# Languatool settings. If LT_PORT isn't a valid port number, the languagetool
# daemon will not run.
LT_PORT = 4385
LT_URL = "http://localhost:" + str(LT_PORT)

# Gitrepo export settings
#
# GitHub
#
# Set up GitHub as one of the connected login options. See instructions here:
# https://django-allauth.readthedocs.io/en/latest/providers.html#github
# Then enable the below options for the github connector.
#
# SOCIALACCOUNT_PROVIDERS = {
#    'github': {
#        'SCOPE': [
#            'repo',
#            'user:emai',
#        ],
#    }
# }
#
# GitLab
#
# Set up GitLab as one of the connected login options. See instructions here:
# https://django-allauth.readthedocs.io/en/latest/providers.html#gitlab
# Then enable the below options for the gitlab connector.
#
# SOCIALACCOUNT_PROVIDERS = {
#    'gitlab': {
#        'SCOPE': [
#            'api',
#        ],
#    }
# }
#
# 2FA settings
# INSTALLED_APPS += [
#    'django_otp',
#    'django_otp.plugins.otp_totp',
#    'two_factor_authentication.FidusConfig',
# ]
# MIDDLEWARE = [
#   'django.contrib.auth.middleware.AuthenticationMiddleware',
#   'django_otp.middleware.OTPMiddleware'
# ]
# OTP_TOTP_ISSUER = 'Fidus Writer' # Add your own organization here
# REMOVED_APPS = ['django.contrib.admin']

# PHPList settings
# PHPLIST_BASE_URL # The URL of your PHPList installation
# PHPLIST_LOGIN # The PHPList user's username created in step 4
# PHPLIST_PASSWORD # The PHPList user's password created in step 4
# PHPLIST_SECRET (optional) # If you have set an obligatory secret within
# the PHPList REST API, set it here as well.
# PHPLIST_LIST_ID # The email list id found in step 2.

# FOOTER_LINKS = [
#     {
#         "text": "Terms and Conditions",
#         "link": "/pages/terms/"
#     },
#     {
#         "text": "Privacy policy",
#         "link": "/pages/privacy/"
#     },
#     {
#         "text": "Equations and Math with MathLive",
#         "link": "https://github.com/arnog/mathlive#readme",
#         "external": True
#     },
#     {
#         "text": "Citations with Citation Style Language",
#         "link": "https://citationstyles.org/",
#         "external": True
#     },
#     {
#         "text": "Editing with ProseMirror",
#         "link": "https://prosemirror.net/",
#         "external": True
#     }
# ]

# Add branding logo inside of "static-libs" folder. For example: static-libs/svg/logo.svg
# BRANDING_LOGO = "svg/logo.svg"
