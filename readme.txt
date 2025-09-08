----- virtual env ----------
A virtual environment is an isolated space where you can install packages specific to a project
without affecting your global Python setup or other projects.

Avoid conflicts - Different projects may need different versions of the same library. A virtual environment keeps them separate.

----- source command ------
Executes the commands in the current shell.
Does not start a new process.
Can modify environment variables, functions, or aliases persistently in your session.

What Happens Without source?
If you just run: ./script.sh
It runs in a new subshell.
Any environment changes (like export VAR=VALUE) won't persist in your current session.

--------- commands ----------
run python app - python3 app.py
open python shell - python3
check current directory - pwd
list contents inside a directory - ls -l instance
