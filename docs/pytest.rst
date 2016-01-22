Using pytest with tox in cookie
===============================

tox failure due to lack of 'deps=pytest' in tox.ini
---------------------------------------------------

.. code-block:: bash

   (cookietox) jsk@jsk-VirtualBox:~/GitHub/cookietox/cookietox$ tox
   GLOB sdist-make: /home/jsk/GitHub/cookietox/cookietox/setup.py
   py351 inst-nodeps: /home/jsk/GitHub/cookietox/cookietox/.tox/dist/cookietox-0.1.0.zip
   py351 installed: cookietox==0.1.0,wheel==0.24.0
   py351 runtests: PYTHONHASHSEED='1128723482'
   py351 runtests: commands[0] | python setup.py test
   running test
   running egg_info
   writing dependency_links to cookietox.egg-info/dependency_links.txt
   writing top-level names to cookietox.egg-info/top_level.txt
   writing cookietox.egg-info/PKG-INFO
   reading manifest file 'cookietox.egg-info/SOURCES.txt'
   reading manifest template 'MANIFEST.in'
   warning: no previously-included files matching '__pycache__' found under directory '*'
   writing manifest file 'cookietox.egg-info/SOURCES.txt'
   running build_ext
   Traceback (most recent call last):
          File "setup.py", line 57, in <module>
            tests_require=test_requirements
          File "/usr/lib/python3.4/distutils/core.py", line 148, in setup
            dist.run_commands()
          File "/usr/lib/python3.4/distutils/dist.py", line 955, in run_commands
            self.run_command(cmd)
          File "/usr/lib/python3.4/distutils/dist.py", line 974, in run_command
            cmd_obj.run()
          File "/home/jsk/GitHub/cookietox/cookietox/.tox/py351/lib/python3.4/site-packages/setuptools/command/test.py", line 142, in run
            self.with_project_on_sys_path(self.run_tests)
          File "/home/jsk/GitHub/cookietox/cookietox/.tox/py351/lib/python3.4/site-packages/setuptools/command/test.py", line 122, in with_project_on_sys_path
            func()
          File "/home/jsk/GitHub/cookietox/cookietox/.tox/py351/lib/python3.4/site-packages/setuptools/command/test.py", line 163, in run_tests
            testRunner=self._resolve_as_ep(self.test_runner),
          File "/usr/lib/python3.4/unittest/main.py", line 92, in __init__
            self.parseArgs(argv)
          File "/usr/lib/python3.4/unittest/main.py", line 139, in parseArgs
            self.createTests()
          File "/usr/lib/python3.4/unittest/main.py", line 146, in createTests
            self.module)
          File "/usr/lib/python3.4/unittest/loader.py", line 146, in loadTestsFromNames
            suites = [self.loadTestsFromName(name, module) for name in names]
          File "/usr/lib/python3.4/unittest/loader.py", line 146, in <listcomp>
            suites = [self.loadTestsFromName(name, module) for name in names]
          File "/usr/lib/python3.4/unittest/loader.py", line 117, in loadTestsFromName
            return self.loadTestsFromModule(obj)
          File "/home/jsk/GitHub/cookietox/cookietox/.tox/py351/lib/python3.4/site-packages/setuptools/command/test.py", line 37, in loadTestsFromModule
            tests.append(self.loadTestsFromName(submodule))
          File "/usr/lib/python3.4/unittest/loader.py", line 114, in loadTestsFromName
            parent, obj = obj, getattr(obj, part)
    AttributeError: 'module' object has no attribute 'test_arg_parse'
        ERROR: InvocationError: '/home/jsk/GitHub/cookietox/cookietox/.tox/py351/bin/python setup.py test'


avoid __init__.py files in your test directories. This way your tests can run easily against an installed version of mypkg, independently from if the installed package contains the tests or not.

As that's the recommended workflow of working with py.test: install the package under development with pip install -e, then test it.

Because of this, I myself opt for unique test names, in the convention over configuration manner. It also ensures that you don't get ambiguous test names in the various test run output.

If you need to keep the test names and don't care about the above mentioned functionality, you should be ok with putting an __init__.py.

----------------------
                
I don't get the use case: "This way your tests can run easily against an installed version of mypkg". I run my tests against my development version of mypkg. This way the tests exist. I create __init__.py files to avoid this "unique basename" error message. – guettli Jun 18 '14 at 9:46 
                
I created a feature request to change the docs: bitbucket.org/hpk42/pytest/issue/529/… – guettli Jun 18 '14 at 10:21
                
@guettli The use case is when you want to test your package as installed via setup.py. This can be used to ensure you're including all required files in the install, like bundled data and that all dependencies are handled correctly. It can also be used to install on environments where the target system does not have a compiler and you're going to use a binary egg or wheel for the installation. – Mark Evans Apr 26 '15 at 18:56

