# logging library

* Loggers
* Handlers
* Filters
* Formatters

# Loggers

A good convention to use when naming loggers is to use a module-level logger, in each module which uses logging, named as follows:

```python
logger = logging.getLogger(__name__)
```
It could add/remove Handler or Filter.

[logging flow](https://docs.python.org/3.5/_images/logging_flow.png)

[logging Formatter](https://docs.python.org/3.5/library/logging.html#logrecord-attributes)

[logging.config](https://docs.python.org/3.5/library/logging.config.html)

# Handlers

[Useful handlers](https://docs.python.org/3.5/howto/logging.html#useful-handlers)

# Reference

1. https://docs.python.org/3.5/howto/logging.html
