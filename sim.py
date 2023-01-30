# This routine simulates a given DAA algorithm for comparison with the real data.

import sys

def parity(n):
  """ Compute parity of n. 1 = even parity."""
  p = 1
  while n:
    if n & 1:
      p = 1 - p
    n = n >> 1
  return p

def daa_intel(al, af, cf):
  """ The DAA algorithm as specified by Intel."""
  old_al = al
  old_cf = cf
  if al & 0xf > 9 or af:
    al += 0x06
    cf = old_cf or al >= 0x100
    af = 1
  else:
    af = 0
  al = al & 0xff
  if old_al > 0x99 or old_cf:
    al += 0x60
    cf = 1
  else:
    cf = 0
  al = al & 0xff
  return (al, af, cf)

def daa_simplified(al, af, cf):
  """ The DAA algorithm as specified by Intel, cleaned up."""
  old_al = al
  if al & 0xf > 9 or af:
    al += 0x06
    af = 1
  al = al & 0xff
  if old_al > 0x99 or cf:
    al += 0x60
    cf = 1
  al = al & 0xff
  return (al, af, cf)

def test(daa_routine):
  """ This runs through all the test cases using the specified routine."""
  for af in range(0, 2):
    for cf in range(0, 2):
      for i in range(0, 256):

        al, a, c = daa_routine(i, af, cf)

        # Compute flags for output

        flags = 0x202 # interrupt plus bit 1 always set
        if al & 0x80:
          flags |= 0x80 # sign
        if al == 0:
          flags |= 0x40 # zero
        if a:
          flags |= 0x10 # aux

        if parity(al):
          flags |= 0x04 # parity
        if c:
          flags |= 0x01 # carry

        print("%x, daa %x, flags %x" % (i, al, flags))


if __name__ == '__main__':
  if len(sys.argv) == 2 and sys.argv[1] == "--intel":
    print("Running Intel algorithm", file=sys.stderr)
    test(daa_intel)
  else:
    print("Running simplified algorithm", file=sys.stderr)
    test(daa_simplified)
