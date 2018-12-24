def is_leap_year (year):
	if year % 400 == 0:
		return True
	elif year % 100 == 0:
		return False
	elif year % 4 == 0:
		return True
	return False
	
	
def weekday_newyear(year):
	weekday=0 #mandag
	for i in range(1900, year):
		days_in_year = is_leap_year(i) and 366 or 365
		weekday = (weekday + days_in_year)%7
	return weekday
		
ukedager = [" man", "tir", "ons", "tor", "fre", "lør", "søn "]	
		
for i in range(1900, 1920):
	print(i, ukedager[weekday_newyear(i)])
	
def is_workday ( weekday ):
	return 0 <= weekday < 5
	
def workdays_in_year ( year ):
	weekday = weekday_newyear ( year ) #Setter ukedagen til å starte på den dagen året har sin første dag. Dette er viktig for å skille årene med antall dager
	days_in_year = is_leap_year ( year ) and 366 or 365 #er en dag mer i året om the er skuddår
	workdays = 0
	for i in range ( days_in_year ):
		if is_workday ( weekday ): 
			workdays += 1 #is_workday fra forrige funksjon som viser om det er en arbeidsdag eller ikke, og det er om den ligger i intervallet 0 <= i < 5. Kjører bare så lenge den er true
		weekday = ( weekday + 1) % 7 #når det ikke lenger er en arbeidsdag så legger weekday til en, og den går ikke over 6 fordi vi bruker modulo 7.
	return workdays
	 
for i in range (1900 , 1920 ):
	print (i, " har", workdays_in_year (i), " arbeidsdager ")