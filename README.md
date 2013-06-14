Python scripts for working in Sublime Text 2
============================================


project.py
----------
This script sets up a [virtual environment][virtualenv] and a .sublime-project
file for a Python project. There are two variables in `project.py` that need to
be set depending on platform and setup.

```python
VIRTUALENV  = 'C:\\Python27\\Scripts\\virtualenv.exe'
SUBLIMETEXT = 'subl'
```

While writing this script, I am on a Windows 7 system with the my PATH system
variable pointing to the Sublime Text 2 installation directory and have changed
the default `sublime_text.exe` to `subl.exe`. These variables must be adjusted
in order for it to work properly on your setup.

Running `project.py`:

<pre class="console">
  C:\>python project.py --help

  usage: project.py [-h] -n NAME [-p PATH] [--no-sb2] [-v]

  Create a Python project with Sublime Text 2.
  --------------------------------------------
    - Creates a Python project with virtualenv.
    - Creates a Sublime Text 2 project file.

  optional arguments:
    -h, --help            show this help message and exit
    -n NAME, --name NAME  project name (required)
    -p PATH, --path PATH  project path, default .
    --no-sb2              do not open Sublime Text 2
    -v, --verbose
</pre>

After the project has been setup, you will see the following output:

Windows:

<pre class="console">
  {PROJECT} has been created.
  To activate the virtualenv, use the following:

  > cd {PROJECT}
  > .\Scripts\activate
</pre>

*Nix:

<pre class="console">
  {PROJECT} has been created.
  To activate the virtualenv, use the following:

  > cd {PROJECT}
  > source bin/activate
</pre>

Upon completion of creating the virtual environment and the .sublime-project
file, Sublime Text 2 will open a new window with the project only showing the
`src` folder, which contains the `{PROJECT}.sublime-project

Project structure on Windows:

<pre class="console">
  {PROJECT}/
  |-- Include/ (set by virutalenv.exe)
  |-- Lib/ (set by virtualenv.exe)
  |-- Scripts/ (set by virtualenv.exe)
  |-- {PROJECT}/
  |   |-- __init__.py
  |   |-- {PROJECT}.sublime-project
  |   `-- {PROJECT}.sublime-workspace (hidden by .sublime-project)
</pre>

[virtualenv]: http://www.virtualenv.org/en/latest/