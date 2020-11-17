import os


def env_var(key, default=None, required=False):
    """ Parse environment variable accordingly. """
    if required:
        # Throw KeyError for missing requirements
        val = os.environ[key]
    else:
        # Use default or None
        val = os.environ.get(key, default)

    # Replace booleans
    if val == 'True':
        val = True
    elif val == 'False':
        val = False

    return val


class Config(object):
    SECRET_KEY = env_var('SECRET_KEY', required=True)

    SQLALCHEMY_DATABASE_URI = env_var('DATABASE_URI', required=True)
    SQLALCHEMY_TRACK_MODIFICATIONS = env_var('SQLALCHEMY_TRACK_MODIFICATIONS', default=False)
