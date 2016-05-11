tox setup
=========


:ref:`tox-error01`

:ref:`tox-error02`

.. code-block:: guess

        E   ImportError: No module named 'cv2'

I get this error because tox creates a virtualenv for each version of python being tested and it cannot include the local cv2.so file.

I deleted all of the softlinks to cv2.cpython-34m.so in ~/.pyenv/ and .tox/

Then I made a softlike to /usr/local/lib/python3.4/site-packages/cv2.cpython-34m.so cv2.so in the main site-packages folder. Finally I added '/usr/local/lib/python3.4/site-packages/cv2.cpython-34m.so' to /etc/ld.so.conf and ran sudo ldconfig.

ldconfig -p still does not show the cv2.so source object file.  Even if it did would having it available in the python3.4 packages really do any good?

I just ran python3.4 and it does not have site-packages in the path, just variations on '/usr/local/lib/python3.4/dist-packages'

I linked cv2.so into '/usr/local/lib/python3.4/dist-packages' but now when I 'import cv2' I get:

.. code-block:: guess

        ImportError: numpy.core.multiarray failed to import
        Traceback (most recent call last):
        File "<string>", line 1, in <module>
        ImportError: numpy.core.multiarray failed to import

I suppose if numpy were pip installed globaly that would not be a problem.
