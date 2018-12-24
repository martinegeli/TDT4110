def add_data(user):
	liste=user.split()
	liste[2]=int(liste[2])		
	return liste
	
print(add_data('Mark Zuckerberg 32 Male Married'))

def get_person(given_name, facebook):
	fjesboka=[]
	for i in range(len(facebook)):
		if facebook[i][0]==given_name:
			fjesboka.append(facebook[i])
	return fjesboka
		
#hvis given_name, da posisjon [0] i listen stemmer med [0] for hver liste som finner i listen facebook, så skal den printe ut hele listen. 
	
facebook = [["Mark", "Zuckerberg", 32, "Male", "Married"], 
		["Therese", "Johaug", 28, "Female", "Complicated"],
		["Mark", "Wahlberg", 45, "Male", "Married"],
		["Siv", "Jensen", 47, "Female", "Single"]]

print(get_person("Siv", facebook))

def main():
	
	
	
	