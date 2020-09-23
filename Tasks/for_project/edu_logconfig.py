import logging
import locale


def set_log_level(log_level):
    log_levels = ['NOTSET', 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    i = log_levels.index(log_level)
    if i > 0:  # Log level cannot be lower than 'NOTSET'
        i -= 1
    logging.disable(logging._levelNames[log_levels[i]])


LOGCONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s - %(levelname)s - %(name)s: %(message)s'
        },
        'verbose': {
            'format': '%(asctime)s - %(levelname)s - %(name)s[LINE:%(lineno)d]: %(message)s'
        },
    },
    'handlers': {
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'edu.log',
            'formatter': 'default',
            'level': 'DEBUG',
            'maxBytes': 102400,
            'backupCount': 5,
            'encoding': locale.getpreferredencoding()
        },
    },
    'loggers': {
        '__main__': {
            'handlers':['file'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'edu_dbclient': {
            'handlers':['file'],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
}