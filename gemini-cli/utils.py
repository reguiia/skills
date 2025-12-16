import subprocess
import os
import shlex

def get_skill_path(skill_name):
    """Gets the absolute path to a skill directory."""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'skills', skill_name))

def run_command(command_string):
    """Runs a command and prints its output securely."""
    command = shlex.split(command_string)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    for line in iter(process.stdout.readline, ''):
        print(line, end='')
    process.stdout.close()
    return_code = process.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, command)
