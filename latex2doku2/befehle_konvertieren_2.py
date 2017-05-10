# -*- coding: cp1252 -*-

# auswahl der zu bearbeitenden Datei
dateiname = raw_input("Bitte Dateinamen eingeben:   ")
file = open(dateiname,'r')

# definition der Variablen 
dok=''
index = 0
newline = ''
buh = ''
# deklaration der Latex-befehlslisten und deren ersetzung in Dokuwiki Syntax 
# Latex-befehl
befehl = ["\\verantwortlich{","\\ref{sec:",'\\URL{','\\url{','\\Url{','\\href{','\\isofuss{']
# er�ffnender Befehl dokuwiki Syntax 
befehlneu = ["**verantwortlich: //","[[",'[[','[[','[[','[[','Erstellt am ']
# Abschliessender Befehl dokuwiki Syntax
befehlneu2 = ["//**","]]",']]',']]',']]',']]',' ']

# �ffnen der Datei und Auslesen jeder zeile
file = open(dateiname,'r')
for line in file:
    
    index=0
    while index<len(befehl):
        if befehl[index] in line:
            
            newline = line				# Die aktuelle zeile wird in die Variable Newline gespeichert
            print(line)
            newline = newline.replace((befehl[index]),(befehlneu[index])) 	# in Newline wird der Latex Befehl durch den er�ffneden wiki Befehl ersetzt
            newline = newline.replace('}',(befehlneu2[index]))				# und die spitze Klammerzu wird durch den schliessenden wiki Befehl ersetzt
            print(newline)					# ausgabe der Zeile zur �berpr�fung 
			# Nachfrage ob die Zeile in Ordnung ist oder nicht 
            ok = raw_input('zeile OK? j zum best�tigen n um per hand zu korregieren  ') 
            if ok == 'j':
                line = newline 		# newline wird wieder nach line Gespeichert  und line wird �berpr�ft
            if ok =='n':
                line = raw_input('Bitte Zeile korekt eingeben:   ')		# wenn nein wird die neu eingabe der Zeile Verlangt
            else:
                line = line
        index = index + 1 # Index um die Befehle weiterzuz�hlen wird um 1 erh�ht 
    
    dok = dok + line  # Die zeile wird an die variable Dok angeh�ngt sodas sich das dokument langsam wieder zusammen setzt
        
print(dok) # Das gesamte Dokument wird zum Korrekturlesen nochmal angezeigt

# neue Datei unter dem Namen dateineu2.txt Absteichern 
file=open("dateineu2.txt",'w')
file.write(dok)
file.close
file=open("dateineu2.txt",'w')
file.write(dok)
file.close

    
