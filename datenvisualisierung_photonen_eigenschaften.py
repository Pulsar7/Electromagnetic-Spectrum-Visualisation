# Autor: Benedikt Fichtner
# Github: https://github.com/Pulsar7/
# Python-Version: Python 3.8.10

import os,csv
import matplotlib.pyplot as plt

def calculate(max_number):
	data = {
		'dateipfad': "daten.csv",
		'wellenlänge': {
			'elements': [],
			'text': "Wellenlänge in nm"
		},
		'energie': {
			'elements': [],
			'text': "Energie in eV"
		},
		'frequenz': {
			'elements': [],
			'text': "Frequenz in Hz"
		},
	}
	with open(data['dateipfad'], 'r') as r:
	    reader = csv.reader(r)
	    for row in reader:
	    	wellenlänge = float(row[1])
	    	frequenz = (c / (wellenlänge/1000000000))
	    	energie = (h_evs * frequenz)
	    	print(f'{energie}')
	    	data['wellenlänge']['elements'].append(wellenlänge)
	    	data['energie']['elements'].append(energie)
	    	data['frequenz']['elements'].append(frequenz)
	draw(data)

def draw(data):
	(fig, (ax1, ax2)) = plt.subplots(2, 1)	
	ax1.set(
		xlabel=data['wellenlänge']['text'],
		ylabel=data['energie']['text']
		#title='Photonenenergien'
	)
	ax1.grid()
	ax1.plot(data['wellenlänge']['elements'], 
		data['energie']['elements'], 'o-', 
		color = "blue")

	#Zweites Koordinatensystem
	ax2.grid()
	ax2.plot(data['wellenlänge']['elements'], 
		data['frequenz']['elements'], 'o-', 
		color = "red")
	ax2.set(
		xlabel=data['wellenlänge']['text'],
		ylabel=data['frequenz']['text']
	)

	plt.show()

h_js = (6.67408*10**-11) #Js
h_evs = (4.135667662*10**-15) #eV*s
c = 299792458 #m/s
max_number = 400
if (__name__ == '__main__'):
	os.system("clear") #Linux
	calculate(max_number)
