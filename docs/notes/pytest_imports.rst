PyTest Imports
==============

As you say yourself py.test basically assumes you have the PYTHONPATH setup up correctly. There are several ways of achieving this:

Give your project a setup.py and use pip install -e . in a virtualenv for this project. This is probably the standard method.

As a variation on this if you have a virtualenv but no setup.py use your venv's facility to add the projects directory on sys.path, e.g. pew add . if you use pew, or add2virtualenv . if you use virtualenv and the extensions of virtualenvwrapper.

If you always like the current working directory on sys.path you can simply always export PYTHONPATH='' in your shell. That is ensure the empty string on on sys.path which python will interpret as the current working direcotry. This is potentially a security hazard though.

My own favourite hack, abuse how py.test loads conftest files: put an empty conftest.py in the project's top-level directory.

The reason for py.test to behave this way is to make it easy to run the tests in a tests/ directory of a checkout against an installed package. If it would unconditionally add the project directory to the PYTHONPATH then this would not be possible anymore.

finally found this `discussion`_ which told me what to do.  I quote: ``My own favourite hack, abuse how py.test loads conftest
files: put an empty conftest.py in the project's top-level directory.``  Now py.test finds everything.

.. _discussion: http://stackoverflow.com/questions/20971619/ensuring-py-test-includes-the-application-directory-in-sys-path
