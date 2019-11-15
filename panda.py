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

	df = readcsv("data/nb.csv")
	print (df)


if __name__ == '__main__':
	main()