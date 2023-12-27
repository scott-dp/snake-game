#Oppgave 6c
'''
#Passer på at inputet programmet får er et heltall
gyldig = False

while not gyldig:
    poeng = input("Skriv inn poengsummen din: ")


    try:#prøver å gjøre om til int
        poeng = int(poeng)
        gyldig = True
    except ValueError:#Hvis den får feilmeldingen ValueError så må brukeren prøve på nytt
        print("Du må skrive inn et heltall.")


if poeng>=0 and poeng<50:#Passer på at den ikke gir 'ikke bestått' til verdier under 0
    print("ikke bestått")
elif poeng>=50 and poeng<=69:#resten av valgene får med de riktige resultatene for grenseverdiene
    print("bestått")
elif poeng>=70 and poeng<=89:
    print("godt bestått")
elif poeng>=90 and poeng<=100:
    print("meget godt bestått")
else:
    print("Ikke gyldig poengsum!")
'''
#Oppgave 9a
#aller først må jeg fjerne feilen i datasettet
import json

with open("googleplaystore.json",encoding="utf-8-sig") as fil:#åpner json filen med innholdet
    innhold=json.load(fil)#laster json data

    #fjerner ordboken som har feil i json filen
    for i in innhold:
        if i["App"]=='Life Made WI-Fi Touchscreen Photo Frame':#sjekker hvert element om det stemmer
            innhold.remove(i)#fjerner elementet der feilen ligger

#lager ordbøker for hver kategori med antall og rating
kategorierAntall={}
kategorierSumRating={}
kategorierSumInstallasjoner={}

#ordbok som legger inn antall apper i tilhørende ordbok
def finnKategorier(data,ordbok):
    for i in data:
        if i["Category"] in ordbok:#Hvis kategorien allerede fins i ordbok
            ordbok[i["Category"]]+=1#legger den til 1
        elif i["Category"] not in ordbok:#hvis den ikke finnes
            ordbok[i["Category"]]=1#setter verdien lik 1


#ordbok som legger inn antall apper i tilhørende ordbok
def finnRating(data,ordbok):
    for i in data:
        if i["Category"] in ordbok and i["Rating"]!="NaN":#sjekker om den finnes i ordboken fra før og at rating ikke er NaN
            ordbok[i["Category"]]+=float(i["Rating"])#legger den til ratingen i summen
        elif i["Category"] not in ordbok and i["Rating"]!="NaN":#samme her men bare hvis det ikke finnes fra før i ordboken
            ordbok[i["Category"]]=float(i["Rating"])

        ordbok[i["Category"]]=round(ordbok[i["Category"]],2)#slik at det ikke blir så mange desimaler

def finnInstallasjoner(data,ordbok):#finner summen av installasjoner
    for i in innhold:
        if i["Installs"]!='0':#passer på at det ikke er 0 installasjoner
            temp=i["Installs"][:-1]#tar bare med tallet og fjerner '+'
            tilInt=int(temp.replace(",",""))#fjerner komma
            i["Installs"]=tilInt#endrer på antall installasjoner slik at det blir lettere videre
            if i["Category"] in ordbok:
                ordbok[i["Category"]]+=tilInt#legger til i sum installasjoner ordboken
            elif i["Category"] not in ordbok:
                ordbok[i["Category"]]=tilInt

#kaller opp funksjonene
finnInstallasjoner(innhold,kategorierSumInstallasjoner)#kaller opp funksjonen
finnKategorier(innhold,kategorierAntall)
finnRating(innhold,kategorierSumRating)

gjennomsnittRating={}#ny ordbok som skal inneholde gjennomsnittrating til hver kategori
gjennomsnittInstallasjoner={}

#funksjon som regner ut gjennomsitt rating
def regnUtGjennomsnittRatingOgInstallasjoner(antallOrdbok,sumratingOrdbok,sumInstallasjoner,nyOrdbok1,nyOrdbok2):
    for i in antallOrdbok:
        nyOrdbok1[i]=round(sumratingOrdbok[i]/antallOrdbok[i],2)#deler summen av rating på antall apper for å finne gjennomsitt og runder av
        nyOrdbok2[i]=round(sumInstallasjoner[i]/antallOrdbok[i],0)#deler summen av installsjoner på antall apper for å finne gjennomsitt og runder av


regnUtGjennomsnittRatingOgInstallasjoner(kategorierAntall,kategorierSumRating,kategorierSumInstallasjoner,gjennomsnittRating,gjennomsnittInstallasjoner)#kaller opp funksjonen


sortertAntall = sorted(kategorierAntall.items(), key=lambda x: x[1], reverse=True)#gir en liste med tupler sortert etter flest apper i kategorien

print("De 3 største kategoriene målt i antall apper:")
#skriver ut de 3 største appene
for i in range(3):
    print(f'{sortertAntall[i][0]} med {sortertAntall[i][1]} apper, gjennomsnittsrating er {gjennomsnittRating[sortertAntall[i][0]]}, gjennomsnitt installsjoner er {gjennomsnittInstallasjoner[sortertAntall[i][0]]}')

#oppgave 9b

#ordbøker som lagrer spill og antall installasjoner
apperIFAMILY={}
apperIGAME={}
apperITOOLS={}

#funksjon som legger til info i de ordbøkene
def finnMestPopulareApper(data,family,game,tools):
    for i in data:
        if i["Category"]=="FAMILY":
            family[i["App"]]=int(i["Installs"])
        elif i["Category"]=="GAME":
            game[i["App"]]=int(i["Installs"])
        elif i["Category"]=="TOOLS":
            tools[i["App"]]=int(i["Installs"])

finnMestPopulareApper(innhold,apperIFAMILY,apperIGAME,apperITOOLS)#kaller opp funksjon

#sorterer ordbøkene
familySortert=sorted(apperIFAMILY.items(), key=lambda x: x[1], reverse=True)
gameSortert=sorted(apperIGAME.items(), key=lambda x: x[1], reverse=True)
toolsSortert=sorted(apperITOOLS.items(), key=lambda x: x[1], reverse=True)

print("De mest populære appene i FAMILY, GAME OG TOOLS i antall installasjoner:")

for i in range(3):
    print(f'de {i+1}. mest populære: ')
    print(f'family: {familySortert[i][0]}, installasjoner: {familySortert[i][1]}, game: {gameSortert[i][0]}, installasjoner: {gameSortert[i][1]}, tools: {toolsSortert[i][0]}, installasjoner: {toolsSortert[i][1]}')
