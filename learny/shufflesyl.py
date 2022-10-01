#! python3
# -*- coding: utf-8 -*-

import random
#import docx
#from . import docxprint
#code: pip install PyHyphen
from hyphen import Hyphenator
de_DE = Hyphenator('de_DE')

def syl_shuffle(some_nouns):
	try:
		import docxprint
	except ImportError:
		from learny import docxprint
	#python-docx module code: pip install python-docx
	import docx
	Aufgabe = {
		"Kopfzeile": "Name: 				Klasse: 				Datum:  \n ",
		"Titel": "",
		"1. Aufgabe": "Finde die Wörter aus den Lücken!\n",
		"Hinweise": "Hier sind die Wörter aus den Lücken: \n",
		"Rätselwörter": "Hier ein paar Rätselwörter aus dem Text: \n",
	}
	doc = docx.Document()# initializing python-docx
	save_path = docxprint.docx_print(Doc= doc, save= 'sylshuffle')
	print("some_nouns", some_nouns)

	some_nouns = list(set(some_nouns))
	#list(dict.fromkeys(some_nouns)) #erase duplicates
	random.shuffle(some_nouns) #shuffle für Rätselwörter
	docxprint.docx_print(printText=Aufgabe["Rätselwörter"], Bold=True, Doc=doc)
	print("some_nouns", some_nouns)


	for word in some_nouns:
		hyph = de_DE.syllables(word.text)
		random.shuffle(hyph)
		if hyph != []:
			shuffled = ' '.join(hyph)
			print(hyph)
		if word == some_nouns[-1]:
			break
		word = str(word)
		#shuffled = list(word)
		#random.shuffle(shuffled)
		shuffled = ''.join(shuffled)
		docxprint.docx_print(printText=shuffled + ' ______________________________', Doc=doc)
		print(shuffled)

	doc.save(save_path)

if __name__ == "__main__":
	import clozetest
	language = "Sprache: Deutsch"

	input= """
	In vielen Getränken in Deutschland ist zu viel Zucker. Das hat die Organisation „Foodwatch“ festgestellt. Wenn man zu viel Zucker isst, kann man zu dick und krank werden.

	Die Organisation „Foodwatch“ hat 463 Limonaden, Energy Drinks, Saft-Schorlen und Eis-Tees untersucht. „Foodwatch“ ist ein englisches Wort und heißt Lebens-Mittel-Überwachung. Nur sechs Getränke waren nicht gezuckert. Das süßeste Getränk – ein Energy-Drink – hatte in einer halben Liter Dose 78 Gramm Zucker. Das sind 26 Stück Würfel-Zucker.
	Die Welt-Gesundheits-Organisation hat empfohlen: Ein Mensch sollte nicht mehr als sechs Tee-Löffel Zucker am Tag essen. Wenn man mehr Zucker isst, können die Zähne krank werden oder man wird zu dick. Eine große Gefahr ist auch die Zucker-Krankheit. Sie wird Diabetes genannt. Daran kann der Mensch sterben.
	In dem Land Groß-Britannien soll es deshalb ab 2018 eine Zucker-Steuer geben, damit die Hersteller weniger süße Getränke verkaufen.
	„Foodwatch“ fordert: Auch in Deutschland soll es eine Zucker-Steuer geben. Die Bundes-Regierung lehnt das ab. Der Minister für Ernährung, Christian Schmidt, sagt: Straf-Steuern auf Lebens-Mittel sind der falsche Weg. Die Menschen sollen besser über gesunde Lebens-Mittel informiert werden. Am besten schon in der Schule.

	"""
	someNouns, noun_list = clozetest.cloze_test(input, language)
	syl_shuffle(some_nouns= noun_list)
