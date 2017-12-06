import re
import subprocess

def run_command(command):
    p = subprocess.Popen(command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')

command = 'ping -D google.com'.split()

matcher = re.compile(r'\[(.*)\].*time=(.*) ms')

for line in run_command(command):
    line = line.decode("utf-8").strip()
    print(line)
    match = matcher.match(str(line))
    if match is not None:
        match_groups = match.groups()
        print(match_groups)

