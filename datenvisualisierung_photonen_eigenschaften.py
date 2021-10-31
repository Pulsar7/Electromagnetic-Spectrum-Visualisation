# Autor: Benedikt Fichtner
# Github: https://github.com/Pulsar7/
# Python-Version: Python 3.8.10

import os,csv
import matplotlib.pyplot as plt

data = {
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
	}
}
dateipfad = "data/daten.csv"
calculated_data_dateipfad = "calculated/calculated.csv"

def write_data(rows):
	with open(calculated_data_dateipfad,'w') as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerows(rows)

def calculate(max_number):
	rows = [
		[
		'Name',
		'Wellenlänge in nm',
		'Energie in eV','Frequenz in THz'
		]
	]
	with open(dateipfad, 'r') as r:
	    reader = csv.reader(r)
	    for row in reader:
	    	wellenlänge = float(row[1])
	    	frequenz = (c / (wellenlänge/(10**9)))
	    	energie = (h_evs * frequenz)
	    	data['wellenlänge']['elements'].append(wellenlänge)
	    	data['energie']['elements'].append(energie)
	    	data['frequenz']['elements'].append(frequenz)
	    	name = row[0]
	    	row = [
	    		name,
	    		'{:.2f}'.format(wellenlänge),
	    		'{:.2f}'.format(energie),
	    		'{:.2f}'.format(frequenz/(10**12)),
	    	]
	    	rows.append(row)
	write_data(rows)
	draw(data)

def draw(data):
	(fig, (ax1, ax2)) = plt.subplots(2, 1)	
	ax1.set(
		xlabel=data['wellenlänge']['text'],
		ylabel=data['energie']['text'],
		title='Untersuchung des elektromagnetischen Spektrums'
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
	data.clear()

h_js = (6.67408*10**-11) #Js
h_evs = (4.135667662*10**-15) #eV*s
c = 299792458 #m/s - Vakuum
max_number = 400
if (__name__ == '__main__'):
	os.system("clear") #Linux
	calculate(max_number)
