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
  C:\>python project.py -h

  usage: project.py [-h] -n NAME [-p PATH] [-v]

  Create a Python project with Sublime Text 2.
  --------------------------------------------
    - Creates a Python project with virtualenv.
    - Creates a Sublime Text 2 project file.

  optional arguments:
    -h, --help            show this help message and exit
    -n NAME, --name NAME  project name (required)
    -p PATH, --path PATH  project path, default .
    -v, --verbose
</pre>

Upon completion of creating the virtual environment and the .sublime-project
file, Sublime Text 2 will open a new window with the project only showing the
`src` folder, which contains the `{APPNAME}.sublime-project

Project structure on Windows:

<pre class="console">
  {APPNAME}/
  |-- Include/ (set by virutalenv.exe)
  |-- Lib/ (set by virtualenv.exe)
  |-- Scripts/ (set by virtualenv.exe)
  |-- src/
  |   |-- {APPNAME}.sublime-project
  |   `-- {APPNAME}.sublime-workspace (hidden by .sublime-project)
</pre>

[virtualenv]: http://www.virtualenv.org/en/latest/