PyEnv
=====

I think it might be best to create a virtualenv this way:

.. code-block:: console

        pyenv virtualenv pyversion venvname
        pyenv virtualenv 2.7.6 cv2stuff

When that is done the venvname will be in the envs folder of the chosen pyversion python interpreter.

--------

I got cv2 to import by softlinking to the system cv2 source object file.

..

        ln -s /usr/local/lib/python3.4/site-packages/cv2.cpython-34m.so ~/.pyenv/versions/cv2stuff/lib/python3.5/site-packages/cv2.so

--------

I thought pyenv was making it hard to use wxpython but it turns out it is hard to use wxpython with any virtualenv.

--------

To upgrade pyenv:

..

        cd /home/jsk/.pyenv/plugins/python-build/../.. && git pull && cd -
