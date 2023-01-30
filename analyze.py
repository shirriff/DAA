# Analyze the output from the DAA test

import re

def flagStr(flags):
  return '%c%c-%c-%c-%c' % (
    'S' if flags & 0x80 else '-', 
    'Z' if flags & 0x40 else '-', 
    'A' if flags & 0x10 else '-', 
    'P' if flags & 0x04 else '-', 
    'C' if flags & 0x01 else '-')

with open('out.txt') as f:
  for line in f.readlines():
    m = re.match('(\S+), daa (\S+), flags (\S+)', line.strip())
    val = int(m.group(1), 16)
    daa = int(m.group(2), 16)
    flags = int(m.group(3), 16)
    if val == 0:
      print('\n')
    if daa != val:
      print('%02x -> %02x, %s, adj %02x' % (val, daa, flagStr(flags), (daa - val) % 0x100))
    else:
      print('%02x -> %02x, %s' % (val, daa, flagStr(flags)))
