import pandas as pd

def readcsv(putanja):
	'''
	Funkcija prima putanju do csv filea. Cita file i vraca dataframe. 
	Vraca error ako nije dobra putanja
	'''
	try:
		d = pd.read_csv(putanja)
	except FileNotFoundError as e:
		print(str(e))
		return ""

	return d



def main():

	df = readcsv("data/nba.csv")
	print (df.iloc[:3]) #print prva tri reda
	print (df.at[2,"Name"]) #print po labelama
	print (df.axes) # ispise koliko ima redova i sve labele/stupce
	print (df.columns) # ispise nazive svih stupaca
	print (df.dtypes) #ispise tipove svih stupaca
	print (df.empty) # if empty True, else False
	print (df.iat[3,4]) #print po poziciji
	print (df.index) # ispise broj redova
	print (df.loc[:4,:'Number']) # kao i iloc samo koristi labele umisto indexa
	print (df.ndim,"broj dimenzija")
	print (df.shape) #ispise velicinu dataframea npr. 6x8
	print (df.size) #ispise velicinu dataframea npr. 48
	#print (df.style) tribalo bi instalirat neki styler i jinja2 pa nista
	print (df.to_numpy()) # prepise df u listu lista. i brze je
 


if __name__ == '__main__':
	main()