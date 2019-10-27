# Here you can add custom options
# DEBUG = False

# ADMINS = (
#     ('Your Name', 'your_email@example.com'),
# )

# This is the contact email that will be shown in various places all over
# the site.
# CONTACT_EMAIL = 'mail@email.com'

# Whether to run setup even in production mode.
# AUTO_SETUP = True

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

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# A list of allowed hostnames of this Fidus Writer installation
# ALLOWED_HOSTS = [
#    'localhost',
# ]

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
# STATIC_URL = '/static/'

# To enable other plugins than the default ones, specify the plugins below
INSTALLED_APPS = [
    'book',
    'citation_api_import',
    'languagetool',
    #'ojs',
    #'phplist',
]

# Languatool settings. If LT_PORT isn't a valid port number, the languagetool
# daemon will not run.
LT_PORT = 4387
LT_URL = 'http://localhost:' + str(LT_PORT)

# 2FA settings
# INSTALLED_APPS += [
    #'django_otp',
    #'django_otp.plugins.otp_totp',
    #'two_factor_authentication.FidusConfig',
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
# PHPLIST_SECRET (optional) # If you have set an obligatory secret within the PHPLIst REST API, set it here as well.
# PHPLIST_LIST_ID # The email list id found in step 2.