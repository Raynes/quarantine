# quarantine

Quarantine is a tool for installing Python packages (programs, in particular) in
isolated virtual environments while allowing easy access to the programs.

First of all, add `~/.quarantine/bin` to your PATH. This is where all
executables will be linked. Next, fire off an install:

```
$ quarantine install awscli
Creating environment /Users/Anthony/.quarantine/envs/awscli...

pip install awscli --install-option --install-scripts=/Users/Anthony/.quarantine/envs/awscli/quarantine-bin

Downloading/unpacking awscli
  Downloading awscli-1.5.1.tar.gz (249kB): 249kB downloaded
  Running setup.py (path:/Users/Anthony/.quarantine/envs/awscli/build/awscli/setup.py) egg_info for package awscli

Downloading/unpacking botocore>=0.65.0,<0.66.0 (from awscli)
  Downloading botocore-0.65.0.tar.gz (1.0MB): 1.0MB downloaded
  Running setup.py (path:/Users/Anthony/.quarantine/envs/awscli/build/botocore/setup.py) egg_info for package botocore

Downloading/unpacking bcdoc>=0.12.0,<0.13.0 (from awscli)
  Downloading bcdoc-0.12.2.tar.gz
  Running setup.py (path:/Users/Anthony/.quarantine/envs/awscli/build/bcdoc/setup.py) egg_info for package bcdoc

    warning: no files found matching 'README.md'
Downloading/unpacking six>=1.1.0 (from awscli)
  Downloading six-1.8.0-py2.py3-none-any.whl
Downloading/unpacking colorama==0.2.5 (from awscli)
  Downloading colorama-0.2.5.tar.gz
  Running setup.py (path:/Users/Anthony/.quarantine/envs/awscli/build/colorama/setup.py) egg_info for package colorama

Downloading/unpacking docutils>=0.10 (from awscli)
  Downloading docutils-0.12.tar.gz (1.6MB): 1.6MB downloaded
  Running setup.py (path:/Users/Anthony/.quarantine/envs/awscli/build/docutils/setup.py) egg_info for package docutils

    warning: no files found matching 'MANIFEST'
    warning: no files found matching '*' under directory 'extras'
    warning: no previously-included files matching '.cvsignore' found under directory '*'
    warning: no previously-included files matching '*.pyc' found under directory '*'
    warning: no previously-included files matching '*~' found under directory '*'
    warning: no previously-included files matching '.DS_Store' found under directory '*'
Downloading/unpacking rsa==3.1.2 (from awscli)
  Downloading rsa-3.1.2.tar.gz
  Running setup.py (path:/Users/Anthony/.quarantine/envs/awscli/build/rsa/setup.py) egg_info for package rsa

    warning: no files found matching 'README'
Downloading/unpacking jmespath==0.4.1 (from botocore>=0.65.0,<0.66.0->awscli)
  Downloading jmespath-0.4.1.tar.gz
  Running setup.py (path:/Users/Anthony/.quarantine/envs/awscli/build/jmespath/setup.py) egg_info for package jmespath

Downloading/unpacking python-dateutil>=2.1 (from botocore>=0.65.0,<0.66.0->awscli)
  Downloading python-dateutil-2.2.tar.gz (259kB): 259kB downloaded
  Running setup.py (path:/Users/Anthony/.quarantine/envs/awscli/build/python-dateutil/setup.py) egg_info for package python-dateutil

Downloading/unpacking pyasn1>=0.1.3 (from rsa==3.1.2->awscli)
  Downloading pyasn1-0.1.7.tar.gz (68kB): 68kB downloaded
  Running setup.py (path:/Users/Anthony/.quarantine/envs/awscli/build/pyasn1/setup.py) egg_info for package pyasn1

Installing collected packages: awscli, botocore, bcdoc, six, colorama, docutils, rsa, jmespath, python-dateutil, pyasn1
  Running setup.py install for awscli
    changing mode of build/scripts-2.7/aws from 644 to 755
    changing mode of build/scripts-2.7/aws.cmd from 644 to 755
    changing mode of build/scripts-2.7/aws_completer from 644 to 755
    changing mode of build/scripts-2.7/aws_zsh_completer.sh from 644 to 755

    changing mode of /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/aws to 755
    changing mode of /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/aws.cmd to 755
    changing mode of /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/aws_completer to 755
    changing mode of /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/aws_zsh_completer.sh to 755
  Running setup.py install for botocore

  Running setup.py install for bcdoc

    warning: no files found matching 'README.md'
  Running setup.py install for colorama

  Running setup.py install for docutils
    changing mode of build/scripts-2.7/rst2html.py from 644 to 755
    changing mode of build/scripts-2.7/rst2s5.py from 644 to 755
    changing mode of build/scripts-2.7/rst2latex.py from 644 to 755
    changing mode of build/scripts-2.7/rst2xetex.py from 644 to 755
    changing mode of build/scripts-2.7/rst2man.py from 644 to 755
    changing mode of build/scripts-2.7/rst2xml.py from 644 to 755
    changing mode of build/scripts-2.7/rst2pseudoxml.py from 644 to 755
    changing mode of build/scripts-2.7/rstpep2html.py from 644 to 755
    changing mode of build/scripts-2.7/rst2odt.py from 644 to 755
    changing mode of build/scripts-2.7/rst2odt_prepstyles.py from 644 to 755

    warning: no files found matching 'MANIFEST'
    warning: no files found matching '*' under directory 'extras'
    warning: no previously-included files matching '.cvsignore' found under directory '*'
    warning: no previously-included files matching '*.pyc' found under directory '*'
    warning: no previously-included files matching '*~' found under directory '*'
    warning: no previously-included files matching '.DS_Store' found under directory '*'
    changing mode of /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/rst2html.py to 755
    changing mode of /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/rst2latex.py to 755
    changing mode of /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/rst2man.py to 755
    changing mode of /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/rst2odt.py to 755
    changing mode of /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/rst2odt_prepstyles.py to 755
    changing mode of /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/rst2pseudoxml.py to 755
    changing mode of /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/rst2s5.py to 755
    changing mode of /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/rst2xetex.py to 755
    changing mode of /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/rst2xml.py to 755
    changing mode of /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/rstpep2html.py to 755
  Running setup.py install for rsa

    warning: no files found matching 'README'
    Installing pyrsa-encrypt-bigfile script to /Users/Anthony/.quarantine/envs/awscli/quarantine-bin
    Installing pyrsa-encrypt script to /Users/Anthony/.quarantine/envs/awscli/quarantine-bin
    Installing pyrsa-verify script to /Users/Anthony/.quarantine/envs/awscli/quarantine-bin
    Installing pyrsa-sign script to /Users/Anthony/.quarantine/envs/awscli/quarantine-bin
    Installing pyrsa-priv2pub script to /Users/Anthony/.quarantine/envs/awscli/quarantine-bin
    Installing pyrsa-decrypt script to /Users/Anthony/.quarantine/envs/awscli/quarantine-bin
    Installing pyrsa-keygen script to /Users/Anthony/.quarantine/envs/awscli/quarantine-bin
    Installing pyrsa-decrypt-bigfile script to /Users/Anthony/.quarantine/envs/awscli/quarantine-bin
  Running setup.py install for jmespath
    changing mode of build/scripts-2.7/jp from 644 to 755

    changing mode of /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/jp to 755
  Running setup.py install for python-dateutil

  Running setup.py install for pyasn1

Successfully installed awscli botocore bcdoc six colorama docutils rsa jmespath python-dateutil pyasn1
Cleaning up...

Creating link for /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/aws...
Creating link for /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/aws.cmd...
Creating link for /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/aws_completer...
Creating link for /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/aws_zsh_completer.sh...
Creating link for /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/jp...
Creating link for /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/pyrsa-decrypt...
Creating link for /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/pyrsa-decrypt-bigfile...
Creating link for /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/pyrsa-encrypt...
Creating link for /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/pyrsa-encrypt-bigfile...
Creating link for /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/pyrsa-keygen...
Creating link for /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/pyrsa-priv2pub...
Creating link for /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/pyrsa-sign...
Creating link for /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/pyrsa-verify...
Creating link for /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/rst2html.py...
Creating link for /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/rst2latex.py...
Creating link for /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/rst2man.py...
Creating link for /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/rst2odt.py...
Creating link for /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/rst2odt_prepstyles.py...
Creating link for /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/rst2pseudoxml.py...
Creating link for /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/rst2s5.py...
Creating link for /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/rst2xetex.py...
Creating link for /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/rst2xml.py...
Creating link for /Users/Anthony/.quarantine/envs/awscli/quarantine-bin/rstpep2html.py...
```

Quarantine simply creates a virtualenv under the hood and symlinks all the
scripts to `~/.quarantine/bin`. As you can see, it uses `pip` for doing the
actual installing. You can pass extra arguments to `pip` like so:

```
$ quarantine install foo -- -i http://my.package-index.io/
```

Finally, you can uninstall things by doing this:

```
$ quarantine install
```

## Why?

Because unless you have a virtualenv for every Python program you use, you're
going to eventually end up with transitive dependency issues.

## License

© 2014 Anthony Grimes. Distributed under the Apache 2.0 license, of which a copy
can be found in the `LICENSE` file at the root of this project.
