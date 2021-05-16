"""
A package contains all the files you need for a module.
Modules are Python code libraries you can include in your project.

1. If you do not have PIP installed, you can download and install it from this page: https://pypi.org/project/pip/
2. Downloading a package
3. Python\Python36-32\Scripts under this pip install <packageName> [pip install camelcase]

"""

# First product method.

import camelcase

c = camelcase.CamelCase()

txt = 'hello world'

print(c.hump(txt))