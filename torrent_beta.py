#!/usr/bin/env python
#-*- coding: utf-8 -*-
#title :news_pb.py
#description :get last torrents from ThePirateBay or do a research.
#author :pirateboxge@gmail.com
#date :20130902
#version :0.1
#usage :python news_pb.py
#notes :I love Hyena...beautiful creature.

from tpb import TPB
#t = TPB()

# when using a proxy site
t = TPB('https://thepiratebay.org')

print '*' * 50
print '1) Voir les torrents récents'
print '2) Faire une recherche de torrent'
print '*' * 50
question_1 = raw_input('Taper le chiffre qui correspond (1 ou 2) : ')
print '*' * 50


if question_1 == '1':
	for tr in t.recent():
		print '*' * 50
		tr.print_torrent()
		print '\n'
else:
	recherche = raw_input('Que voulez vous rechercher ? :')
	results = t.search(recherche, category=0)
	for r in results:
		print '*' * 50
		r.print_torrent()
		print '\n'


