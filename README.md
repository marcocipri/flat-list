FlattenList
==========================

This project is generated using the `python_boilerplate` paster template. It provides simple starting points for using some of the popular best-practices:

  * Proper [setuptools](https://pypi.python.org/pypi/setuptools)-compatible package layout.
  * [py.test](http://pytest.org/)-based tests.
  * [buildout](http://www.buildout.org/) for managing development tools or developing multiple-package projects
  * Usage of the [Travis-CI](https://travis-ci.org/) continuous integration service.


Notes
==========================
 1. solving this problem I've began with a tail recursive approach but, at least in case of Python,
I switched to this 'no recursive' solution because poor performance
 2. Travis integration : https://travis-ci.org/marcocipri/flat-list

Preparation
-----------

The next thing to do after having created the project layout is to add the code to a version control repository. There are two common options for you to choose from:

  1. For smaller single-package projects you might want to keep only the Python's package code (i.e. `src/flatten_list`) under version control, and consider the rest (the `buildout.cfg` and all that comes with it) to be your local development environment.
  2. For larger projects you should consider keeping the whole development environment (including `buildout.cfg`, perhaps several eggs under `src`, docs in `doc`, etc) under version control.



Common development tasks
------------------------

       
  * **Running tests**  
    Tests are kept in the `tests` directory and are run using

        > py.test
        > integrated on Trevis : https://travis-ci.org/marcocipri/flat-list
    
  * **Creating Sphinx documentation**
  
        sphinx-quickstart
        (Fill in the values, edit documentation, add it to version control)
        (Generate documentation by something like "cd docs; make html")
        
    (See [this guide](http://sphinx-doc.org/tutorial.html) for more details)
    
  * **Specifying dependencies for your package**  
    Edit the `install_requires` line in `src/flatten_list/setup.py` by listing all the dependent packages.
    
  * **Publishing the package on Pypi**
  
         > cd src/flatten_list
         > python setup.py register sdist upload


Copyright & License
-------------------

  * Copyright 2018, Marco Cipri
  * License: MIT

