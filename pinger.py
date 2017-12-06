import subprocess

def run_command(command):
    p = subprocess.Popen(command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')

command = 'ping -D google.com'.split()

for line in run_command(command):
        print(line)
