RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'

#esittely variable joka kutsutaan joka kerta kun lennnetään
lentokoneet_esittely_stripped = ("Sähkölentokone", "Hybridi Helikopteri", "Sähköliitokone", "Biodiesel Jet", "Sähköhelikopteri", "Aurinkoivoima Raketti")

#intro teksti esittely
lentokone_esittely = (f'''
{BLUE}1. Sähkölentokone{RESET}

{GREEN}CO2 Päästöt: 0.25 kg/km
Hinta: 6000€{RESET}
Kuvaus: Huipputeknologian nollapäästöinen lentokone, joka tarjoaa vertaansa vailla olevaa tehokkuutta ja ympäristöystävällisyyttä premium-hinnalla
 ''',f''' 
{BLUE}Hybridi Helikopteri{RESET}

{GREEN}CO2 Päästöt: 0.30 kg/km
Hinta: 5000€{RESET}
Kuvaus: Sähkömoottoreiden ja perinteisen polttoaineen yhdistelmä tarjoaa tasapainon vähentyneiden päästöjen ja luotettavan suorituskyvyn välillä.
 ''', f'''
{BLUE}Sähköliitokone{RESET}

{GREEN}CO2 Päästöt: 0.35 kg/km
Hinta: 4000€{RESET}
Kuvaus: Edistyneellä akkuteknologialla varustettu sähköliitokone on suunniteltu tehokkuutta ja mahdollisimman pientä ympäristövaikutusta silmällä pitäen, ihanteellinen keskitason budjeteille.
 ''',f'''
{BLUE}Biodiesel Jet{RESET}

{GREEN}CO2 Päästöt: 0.40 kg/km
Hinta: 3000€{RESET}
Kuvaus: Kestävillä biopolttoaineilla toimiva jet asettaa uuden standardin ympäristöystävälliselle nopealle matkustamiselle saavutettavaan hintaan.
 ''',f'''
{BLUE}Sähköhelikopteri{RESET}

{GREEN}CO2 Päästöt: 0.45 kg/km
Hinta: 2000€{RESET}
Kuvaus: Kompakti ja monipuolinen sähköhelikopteri, joka tarjoaa pienemmät päästöt lyhyen matkan tehtäviin ja budjettitietoisille pelaajille.
 ''',f'''
{BLUE} Aurinkovoima Raketti{RESET}
 
{GREEN}CO2 Päästöt: 0.50 kg/km
Hinta: 1000€{RESET}
Kuvaus: Innovaatiivinen konsepti, joka yhdistää aurinkoenergian ja raketin teknologian, tarjoten ainutlaatuisen, mutta vähemmän tehokkaan matkustustavan alhaisimmalla hinnalla.
 ''')

#Laskennaliset arvot
lentokoneet = [[6000, 0.25], [5000, 0.30], [4000, 0.35], [3000, 0.40], [2000, 0.45], [1000, 0.50]]

