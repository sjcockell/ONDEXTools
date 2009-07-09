#! /usr/bin/env python
import sys

def main(file):
	"Will convert Affy CSV array annotation into list of UniProt identifiers and ProbeIDs"
	fh = open(file, 'r')
	lines = fh.readlines()
	fh.close()
	for line in lines:
		if not line.startswith('#'):
			pass
		else:
			print line.rstrip()

if __name__ == '__main__':
	f = sys.argv[1]
	main(f)
