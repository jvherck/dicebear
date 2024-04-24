---
description: Statistic functions for the usage of Dicebear.
---

# 📊 Statistics

To improve Dicebear's Python package you can set the environment variable `ENABLE_PYTHON_DICEBEAR_USAGE_STATS` to true. This will ping an API for almost every function you use to gather anonymous usage analytics. This anonymous data will be used to determine which functions can be removed, improved or added.

You can put the following lines of code in your project before calling any Dicebear function:

```python
import os

# Enable anonymous usage statistics
os.environ['ENABLE_PYTHON_DICEBEAR_USAGE_STATS'] = 'true'
```

Enabling usage stats will cost performance because it will ping an API for most Dicebear functions you use, but this performance cost should be very minimal.

You can also open a [discussion](https://github.com/jvherck/dicebear/discussions) or [issue](https://github.com/jvherck/dicebear/issues) on the [GitHub repo](https://github.com/jvherck/dicebear) to express your thoughts or ideas.
