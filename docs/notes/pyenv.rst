PyEnv
=====

I think it might be best to create a virtualenv this way:

..

        **pyenv virtualenv pyversion venvname**

When that is done the venvname will be in the envs folder of the chosen pyversion python interpreter.

--------

I got cv2 to import by softlinking to the cv2.so file in ~/.pyenv/versions/cv2stuff/lib/python3.5/site-packages/cv2.so

--------

I thought pyenv was making it hard to use wxpython but it turns out it is hard to use wxpython with any virtualenv.
