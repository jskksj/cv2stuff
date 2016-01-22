PyTest Imports
==============

When I started with py.test I kept getting an ImportError from the test code.  py.test was not finding my cv package. I
finally found this `discussion`_ which told me what to do.  I quote: ``My own favourite hack, abuse how py.test loads conftest
files: put an empty conftest.py in the project's top-level directory.``  Now py.test finds everything.

.. _discussion: http://stackoverflow.com/questions/20971619/ensuring-py-test-includes-the-application-directory-in-sys-path