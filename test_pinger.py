import pytest

from pinger import process_ping_line

def test_pinger():
    line = '[1512530077.291093] 64 bytes from lga25s55-in-f14.1e100.net (172.217.6.238): icmp_seq=1 ttl=53 time=26.6 ms'
    process_ping_line(bytearray(line, encoding='utf-8'))

