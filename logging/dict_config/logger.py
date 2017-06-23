CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s - %(thread)d - %(name)s - %(levelname)s: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': 'ext://sys.stderr'
        }
    },
    'loggers': {
        'dict_config.app': {
            'level': 'DEBUG',
            'handlers': ['console']
        },
        'dict_config.module.library': {
            'level': 'DEBUG',
            'handlers': ['console']
        }
    }
}
