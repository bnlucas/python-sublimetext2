#!/usr/bin/env python
import argparse
import os
import re
import shutil
import sys
import textwrap

from threading import Thread
from subprocess import PIPE, Popen


VIRTUALENV  = 'C:\\Python27\\Scripts\\virtualenv.exe'
SUBLIMETEXT = 'subl'


VCMD = '{venv} {dest}'
SCMD = '{subl} --project {project}'


description = '''
Create a Python project with Sublime Text 2.
--------------------------------------------
  - Creates a Python project with virtualenv.
  - Creates a Sublime Text 2 project file.
'''


project = '''
{
	"build_systems": [
		{
			"name": "Python-{app}",
			"cmd": ["${project_path}/Scripts/python", "-u", "$file"],
			"working_dir": "${project_path:${folder}}/src",
			"selector": "source.python",
			"env": {
				"PYTHONPATH": "."
			}
		}
	],
	"settings": {
		"tab_size": 4,
		"rulers": [80, 100]
	},
	"folders": [
		{
			"path": "{spp}",
			"folder_exclude_patterns": [".svn", ".git", ".hg", "CVS"],
			"file_exclude_patterns": ["*.pyc", "*.pyo", "*.exe", "*.dll",
				"*.obj", "*.o", "*.a", "*.lib", "*.so", "*.dylib", "*.ncb",
				"*.sdf", "*.suo", "*.pdb", "*.idb", ".DS_Store", "*.class",
				"*.psd", "*.db", "*.sublime-workspace"],
			"binary_file_patterns": ["*.jpg", "*.jpeg", "*.png", "*.gif",
				"*.ttf", "*.tga", "*.dds", "*.ico", "*.eot", "*.pdf", "*.swf",
				"*.jar", "*.zip"]
		}
	]
}
'''


parser = argparse.ArgumentParser(
	formatter_class=argparse.RawDescriptionHelpFormatter,
	description=textwrap.dedent(description)
)

parser.add_argument('-n', '--name', type=str, dest='name',
	help='project name (required)', required=True)
parser.add_argument('-p', '--path', type=str, dest='path',
	help='project path, default .', default='.')
parser.add_argument('--no-sb2', dest='sublime', action='store_true',
	help='do not open Sublime Text 2', default=False)
parser.add_argument('-v', '--verbose', dest='verbose', action='store_true')

args = parser.parse_args(sys.argv[1:])


def validate_name(name):
	exp = re.compile(r'^(?i)[a-z0-9][a-z0-9\-\_]+[a-z0-9]$')
	if re.match(exp, name):
		return True
	return False


def format_path(path):
	path = path.replace('\\', '/')
	exp = re.compile(r'^(?i)([a-z])\:([a-z0-9\/]+)$')
	r = re.search(exp, path)
	if r:
		return '/'.join(['', ''.join(r.groups())])
	return path


def sublime_project(project_path):
	src_path = os.path.join(project_path, args.name)
	st_project = '.'.join([args.name.lower(), 'sublime-project'])
	st_project_file = os.path.join(src_path, st_project)

	p = project.replace('{app}', args.name)
	p = p.replace('{spp}', format_path(src_path))

	if args.verbose: print 'Creating', src_path
	os.makedirs(src_path)

	with open(st_project_file, 'wb') as f:
		if args.verbose: print 'Writing', st_project_file
		f.write(p)

	init_file = os.path.join(src_path, '__init__.py')
	with open(init_file, 'wb') as f:
		if args.verbose: print 'Writing', init_file
		f.write('')

	return st_project_file


def open_sublime_text(project_file):
	cmd = SCMD.format(subl=SUBLIMETEXT, project=project_file)
	proc = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
	out, err = proc.communicate()
	if err:
		print err


def main():
	if not validate_name(args.name):
		print 'You have specified an improper project name.'
		exit()

	project_path = os.path.join(os.path.abspath(args.path), args.name)

	if os.path.exists(project_path):
		overwrite = raw_input('Project path exists. Overwrite? Y/N: ')
		if overwrite.lower() == 'n':
			exit()
		elif overwrite.lower() == 'y':
			shutil.rmtree(project_path)
		else:
			print overwrite, 'is an unknown command.'
			exit()
	
	cmd = VCMD.format(venv=VIRTUALENV, dest=project_path)
	cmd = ' '.join([cmd, '--quiet'])
	if args.verbose:
		cmd = ' '.join([cmd, '--verbose'])
	venv = Thread(target=os.system, args=[cmd])
	venv.start()
	venv.join()

	project_file = sublime_project(project_path)

	if not args.sublime:
		subl = Thread(target=open_sublime_text, args=[project_file]).start()

	print args.name, 'has been created.'
	print 'To activate the virtualenv, use the following:'
	print

	if 'win' in sys.platform:
		print '> cd', args.name
		print '> .\\Scripts\\activate'
	else:
		print '$ cd', args.name
		print '$ source bin/activate'


if __name__ == '__main__':
	main()