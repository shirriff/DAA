# Investigation of DAA

The DAA instruction is documented in the [Intel manuals](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html) but the description doesn't make much sense. I ran extensive tests on a real processor to determine exactly how the operation behaves. This repository has files and test output from my investigation. It's here for reference, but it unlikely to be useful to anyone.

### test.asm
This is my test program in assembler. It runs through the DAA input values 0-255 four times. First with CF=0,AF=0; then CF=1,AF=0; then CF=0,AF=1; then CF=1,AF=1.

### out.txt
This is the output from the test program.
A line in this file has the input value, the DAA output value, and the FLAGS, all in hex.

### sim.py
This simulates the pseudocode for DAA, producing an output file that should match out.txt. With the flag `--intel`, it uses the algorithm in the Intel documentation. With no flag, it uses a simplified algorithm.

### analyze.py
This program processes `out.txt`, showing the flag values visually as well as the adjustment value.


