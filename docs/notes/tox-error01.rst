.. _tox-error01:

I need to work on getting a good requirements setup.  
====================================================

I just spend a couple of hours wondering why I kept getting this error:

.. code-block:: guess

    ======================================================================
    ERROR: test_calibrate (unittest.loader._FailedTest)
    ----------------------------------------------------------------------
    ImportError: Failed to import test module: test_calibrate
    Traceback (most recent call last):
    File "/home/jsk/.pyenv/versions/3.5.1/lib/python3.5/unittest/loader.py", line 153, in loadTestsFromName
        module = __import__(module_name)
    File "/home/jsk/GitHub/opencv_stuff/tests/test_calibrate.py", line 4, in <module>
        from opencv_stuff.calibrate import calibrate
    File "/home/jsk/GitHub/opencv_stuff/opencv_stuff/calibrate.py", line 2, in <module>
        import click
    ImportError: No module named 'click'


    ----------------------------------------------------------------------
    Ran 2 tests in 0.002s

    FAILED (errors=1)
    ERROR: InvocationError: '/home/jsk/GitHub/opencv_stuff/.tox/py35/bin/python setup.py test'


The darn thing would pass pytest, and python setup.py test but not tox.  Finally I get the deps right in tox.ini:

.. code-block:: guess

    deps = -r{toxinidir}/requirements_dev.txt
