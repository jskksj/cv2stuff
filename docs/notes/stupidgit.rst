Stupid Git
==========

Actually this problem may not have been git's fault.  git status kept reporting that the docs/_build folder needed to be added to a commit.  
I could not get rid it of and it was in the ignore file.  I think adding the ignore file in PyCharm had something to do with the problem.
Finally I just merged the branch with master an deleted the _build folder.  After checking out the branch I mkdired the folder and remade the 
html files.  Now we are good to go.

The problem came back the next day, it looked like this:

Untracked files:  (use "git add <file>..." to include in what will be 
committed)  _build/

It turns out I had build/ in .gitignore rather than _build/ like it needed.

Using sphinx-git...

.. git_changelog::

.. git_changelog::
    :rev-list: v3..v4
