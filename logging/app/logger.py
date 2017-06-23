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
            #'address': ('localhost', 514)
            'address': '/dev/log'
        }
    },
    'loggers': {
        #'external_module': {
        #    'level': 'DEBUG',
        #    'handlers': ['stderr', 'syslog']
        #},
        '__main__': {
            'level': 'DEBUG',
            'handlers': ['stderr', 'syslog']
        },
        'app.library': {
            'level': 'DEBUG',
            'handlers': ['stderr', 'syslog']
        }
    }
}
