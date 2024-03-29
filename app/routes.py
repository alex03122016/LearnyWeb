from flask import request, render_template, redirect, url_for, flash
from app import app
#from flask_caching import Cache
#cache = Cache(app,config={'CACHE_TYPE': 'simple'})

import os
import sys
from flask import send_file
from learny import learny, clozetest, colorsyllables, infinitive, PresentOrPast, specialwords, wordsearch
from learny import shufflesyl
from app.forms import LearnyWebForm
from app.help import Help

@app.route('/')
@app.route('/index')
def index():
	form = LearnyWebForm()
	help = Help().helpMessage
	return render_template('index.html', title ='learnY', form=form, help=help)

@app.route('/', methods=['GET', 'POST'])
def my_form_post():
	#cache = Cache()
	#with app.app_context():
	#	cache.clear()
	language = "Sprache: Deutsch"
	form = LearnyWebForm()
	text = form.textinput.data

	# clozetest_btn
	if form.clozetest_btn.data == True:
		print("You want a clozetest")
		clozetest.cloze_test(text, language)
		download = 'return_clozetest'
	#button syllables_btn
	if form.syllables_btn.data == True:
		print("You want syllables")
		colorsyllables.color_syllables(text)
		#someNouns, noun_list = clozetest.cloze_test(text, language)
		#shufflesyl.syl_shuffle(noun_list)
		download = 'return_syllables'

	#wordsearch_btn
	if form.wordsearch_btn.data == True:
		print("You want a wordsearch")
		words = specialwords.nouns(text, language)
		wordsearch.wordsearch(words)
		download = 'return_wordsearch'

	#infinitive_btn
	if form.infinitive_btn.data == True:
		print("You want infinitive")
		infinitive.infinitive(text, language)
		download = 'return_infinitive'

	#pastOrPresent_btn
	if form.presentOrPast_btn.data == True:
		print("You want pastOrPrest")
		PresentOrPast.present_or_past(text, language)
		download = 'return_presentOrPast'

	return redirect(url_for(download))

@app.route('/return-clozetest/')
def return_clozetest():
	try:
		return send_file(   os.path.join(os.path.expanduser('~'),
                            'clozeTestfileTitle.docx'),
                             attachment_filename='clozeTestfileTitle.docx',
                             as_attachment=True)
	except Exception as e:
		return str(e)

#return syllables_btn
@app.route('/return-syllables/')
def return_syllables():
	try:
		return send_file(   os.path.join(os.path.expanduser('~'),
                            'colorsyllablesfileTitle.docx'),
                            attachment_filename='colorsyllablesfileTitle.docx',
                            as_attachment=True)
	except Exception as e:
		return str(e)

#return wordsearch_btn
@app.route('/return-wordsearch/')
def return_wordsearch():
	try:
		return send_file(   os.path.join(os.path.expanduser('~'),
                            'wordsearchfileTitle.docx'),
                            attachment_filename='wordsearchfileTitle.docx',
                            as_attachment=True)
	except Exception as e:
		return str(e)

#return infinitive_btn
@app.route('/return-infinitive/')
def return_infinitive():
	try:
		return send_file(   os.path.join(os.path.expanduser('~'),
                            'infinitivefileTitle.docx'),
                            attachment_filename='infinitivefileTitle.docx',
                            as_attachment=True)
	except Exception as e:
		return str(e)

#return pastOrPresent_btn
@app.route('/return-pastOrPresent/')
def return_presentOrPast():
	try:
		return send_file(os.path.join(  os.path.expanduser('~'),
                                        'presentorpastfileTitle.docx'),
                                        attachment_filename='pastOrPresentfileTitle.docx',
                                        as_attachment=True)
	except Exception as e:
		return str(e)
