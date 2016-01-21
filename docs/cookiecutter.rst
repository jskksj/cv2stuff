Create a Project with cookiecutter
==================================

.. code-block:: console

    cookiecutter ~/GitHub/cookiecutter-pypackage

This command will ask a bunch of questions and then create a new folder with a given name, {Project Name}.
Inside that folder will be a python package with the same name plus a lot of configuration folders.

Create a virtualenv
-------------------

.. code-block:: console

    pyenv virtualenv 3.5.1 {Project Name}
    pyenv local system

As you might expect it creates a virtualenv for the above project.  The second command creates local python versions.

.. todo::

    For my own cookiecutter that has my choice of requirements-dev.txt and tox.ini

make docs
=========

The makefile uses sphinx-apidocs which automagically generates an rst file for both the project and module.
