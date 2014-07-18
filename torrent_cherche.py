#!/usr/bin/env python
from tpb import TPB
recherche = raw_input('Que voulez vous rechercher ? :')
t = TPB('https://thepiratebay.org')
results = t.search(recherche, category=0)

for r in results:
	print '*' * 50
	r.print_torrent()
	print '\n'


