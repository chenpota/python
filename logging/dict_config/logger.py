CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'stderr': {
            'format': '%(asctime)s - %(thread)d - %(name)s - %(levelname)s: %(message)s'
        },
        'syslog': {
            'format': '%(thread)d - %(name)s - %(levelname)s: %(message)s'
        }
    },
    'handlers': {
        'stderr': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'stderr'
        },
        'syslog': {
            'level': 'DEBUG',
            'class': 'logging.handlers.SysLogHandler',
            'formatter': 'syslog',
            'address': ('localhost', 514)
            #'address': '/dev/log'
        }
    },
    'loggers': {
        'dict_config.app': {
            'level': 'DEBUG',
            'handlers': ['stderr', 'syslog']
        },
        'dict_config.module.library': {
            'level': 'DEBUG',
            'handlers': ['stderr', 'syslog']
        }
    }
}
