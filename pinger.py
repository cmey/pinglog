import re
import subprocess

from db.db import DB

def run_command(command):
    p = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')

dest = 'google.com'
src = 'eth0'
command = 'ping -I {src} -D {dest}'.format(src=src, dest=dest).split()

matcher = re.compile(r'\[(.*)\].*time=(.*) ms')

def process_ping_line(line, db=None):
    line = line.decode('utf-8').strip()
    print(line)
    match = matcher.match(str(line))
    if match is not None:
        match_groups = match.groups()
        print("  ", match_groups)
        date, ping = match_groups
        if db is not None:
            db.insert(date, dest, ping)

if __name__ == '__main__':

    with DB() as db:
        for line in run_command(command):
            process_ping_line(line, db=db)

