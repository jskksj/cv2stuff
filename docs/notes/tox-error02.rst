.. _tox-error02:

Now I am getting a new error:
-----------------------------

I was able to fix this by manualy soft linking cv2.so into the .tox site-packages, but then it did not find numpy.

.. code-block:: guess


         tox
        GLOB sdist-make: /home/jsk/GitHub/cv2stuff/setup.py
        system create: /home/jsk/GitHub/cv2stuff/.tox/system
        system installdeps: -r/home/jsk/GitHub/cv2stuff/requirements.txt
        system inst: /home/jsk/GitHub/cv2stuff/.tox/dist/cv2stuff-0.1.0.zip
        system installed: alabaster==0.7.8,argh==0.26.1,Babel==2.3.4,bumpversion==0.5.3,click==6.6,coverage==4.0.3,cv2stuff==0.1.0,docutils==0.12,flake8==2.5.4,imagesize==0.7.1,Jinja2==2.8,MarkupSafe==0.23,mccabe==0.4.0,pathtools==0.1.2,pep8==1.7.0,pluggy==0.3.1,py==1.4.31,pyflakes==1.0.0,Pygments==2.1.3,pytest==2.9.1,pytz==2016.4,PyYAML==3.11,six==1.10.0,snowballstemmer==1.2.1,Sphinx==1.4.1,sphinxcontrib-programoutput==0.8,tox==2.3.1,virtualenv==15.0.1,watchdog==0.8.3
        system runtests: PYTHONHASHSEED='439870164'
        system runtests: commands[0] | py.test
        ==================================================================== test session starts =====================================================================
        platform linux -- Python 3.5.1, pytest-2.9.1, py-1.4.31, pluggy-0.3.1
        rootdir: /home/jsk/GitHub/cv2stuff, inifile: 
        collected 2 items / 1 errors 

        cv2stuff/tests/test_exception.py ..

        =========================================================================== ERRORS ===========================================================================
        ______________________________________________________ ERROR collecting cv2stuff/tests/test_cv2stuff.py ______________________________________________________
        cv2stuff/tests/test_cv2stuff.py:5: in <module>
            import cv2
        E   ImportError: No module named 'cv2'
        ============================================================= 2 passed, 1 error in 0.09 seconds ==============================================================
        ERROR: InvocationError: '/home/jsk/GitHub/cv2stuff/.tox/system/bin/py.test'
