Sphinx
======

To fix this error I ran:

..

        pip install -e .

        make docs

        rm -f docs/cv2stuff.rst
        rm -f docs/tests.rst
        rm -f docs/modules.rst
        sphinx-apidoc -o docs/ cv2stuff 
        Creating file docs/cv2stuff.rst.
        Creating file docs/modules.rst.
        make -C docs clean
        make[1]: Entering directory `/home/jsk/GitHub/cv2stuff/docs'
        rm -rf _build/*
        make[1]: Leaving directory `/home/jsk/GitHub/cv2stuff/docs'
        make -C docs html
        make[1]: Entering directory `/home/jsk/GitHub/cv2stuff/docs'
        sphinx-build -b html -d _build/doctrees   . _build/html
        Running Sphinx v1.3.6
        making output directory...

        Exception occurred:
          File "conf.py", line 18, in <module>
            import cv2stuff
        ImportError: No module named 'cv2stuff'
        The full traceback has been saved in /tmp/sphinx-err-42hwxuu8.log, if you want to report the issue to the developers.
        Please also report this if it was a user error, so that a better error message can be provided next time.
        A bug report can be filed in the tracker at <https://github.com/sphinx-doc/sphinx/issues>. Thanks!
        make[1]: *** [html] Error 1
        make[1]: Leaving directory `/home/jsk/GitHub/cv2stuff/docs'
        make: *** [docs] Error 2

