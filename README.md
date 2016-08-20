# Indexerator
# A quick and dirty tool to generate an index for studying for/taking SANS certs. A "reverse index" of a specific format is taken as input to generate the output file.

Usage:
    "python Indexerator.py"
    
    -Prompts for an input file, which should be a file with the format shown below.
    
    -Prompts for an output file, which does not have to exist.

# Required format example:

Book[SPACE][SPACE]1

15[SPACE][SPACE]dns,bind

Book[SPACE][SPACE]2

32[SPACE][SPACE]pcap,flow,wireshark

33[SPACE][SPACE]wireshark,tshark
 
 TODOs:
 - Improved documentation
