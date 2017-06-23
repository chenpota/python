# logging library

[PEP 282](https://www.python.org/dev/peps/pep-0282/)

[PEP 337](https://www.python.org/dev/peps/pep-0337/)

[PEP 391](https://www.python.org/dev/peps/pep-0391/)

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

[logging.config](https://docs.python.org/3.5/library/logging.config.html)

# Handlers

[Useful handlers](https://docs.python.org/3.5/howto/logging.html#useful-handlers)

# Filters

# Formatters

[logging Formatter](https://docs.python.org/3.5/library/logging.html#logrecord-attributes)

# Reference

1. https://docs.python.org/3.5/howto/logging.html

2. https://docs.python.org/3.5/howto/logging-cookbook.html#logging-cookbook
