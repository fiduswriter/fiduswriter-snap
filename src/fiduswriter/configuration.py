# Debug or production mode
DEBUG = False

# Whether to run setup even in production mode.
AUTO_SETUP = True

# The port to run on.
PORT = 4386

# Whether anyone surfing to the site can open an account.
REGISTRATION_OPEN = True

# This determines whether there is a star labeled "Free" on the login page
IS_FREE = True

# Local time zone for this installation. Keep UTC here, the frontend will
# translate this to the correct local time.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# A list of allowed hostnames of this Fidus Writer installation
ALLOWED_HOSTS = [
    'localhost',
]

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

INSTALLED_APPS = []
