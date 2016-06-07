Create a Project with cookiecutter
==================================

.. code-block:: console

    cookiecutter ~/GitHub/cookiecutter-pypackage

This command will ask a bunch of questions and then create a new folder with a given name, {Project Name}.
Inside that folder will be a python package with the same name plus a lot of configuration folders.  Do not use **hyphens** (-) in {Project Name}.

Create a virtualenv
-------------------

.. code-block:: console

    pyenv virtualenv 3.5.1 {Project Name}
    cd ~/GitHub/{Project Name}
    pyenv local {Project Name} system

As you might expect it creates a virtualenv for the above project with Python3.5.1 as default.  The second command ensures that the project will auto activate and adds the system python to the venv.


.. code-block:: console

        cp ~/GitHub/requirements_dev.txt .
        pip install -r requirements_dev.txt

These two commands will then add the normal packages to the new project.

.. todo::

    For my own cookiecutter that has my choice of requirements-dev.txt and tox.ini

make docs
=========

The makefile uses sphinx-apidocs which automagically generates an rst file for both the project and module.
