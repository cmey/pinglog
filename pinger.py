import argparse
import re
import subprocess

from db.db import DB


parser = argparse.ArgumentParser(description='Ping a remote server and log the stats.')
parser.add_argument('--dest', default="google.com", help='ping destination address (remote server)')
parser.add_argument('--src', default="eth0", help='ping source address (local interface)')
args = parser.parse_args()


def run_command(command):
    p = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')

command = 'ping -I {src} -D {dest}'.format(src=args.src, dest=args.dest).split()

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
            db.insert(date, args.dest, ping)

if __name__ == '__main__':

    with DB() as db:
        for line in run_command(command):
            process_ping_line(line, db=db)

