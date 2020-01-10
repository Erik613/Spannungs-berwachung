# Spannungsüberwachung 

| Projektbezeichnung | Projektgruppe | Bearbeitungszeitraum  |
| ------------- |:-------------:| -----:|
|Spannungsüberwachung| Patrick Matern, Monique Vanessa Ostermann, Erik Elges |  |

## Einleitung

### Ziel und Zweck des Dokuments

Dieses Pflichtenheft beschreibt die Umsetzung des Projektes der Firma MeViTo GmbH, bei dem Soft- und Hardware zur Spannungsüberwachung von Akkus entwickelt werden sollen.

### Ausgangssituation/Ist-Zustand

Das Projekt ist eine Forderung der Firma MeViTo GmbH. Für Testprozesse von neu entwickelten Akkuzellen wird ein System aus Soft- und Hardware benötigt, mit dem der Spannungsverlauf von Akkus über einen bestimmten Zeitraum überwacht werden kann. Zur Messung steht ein nodeMCU inklusive Steckbrett und verschiedener Widerstände zur Verfügung.

##	Ziel/Formulierung Auftrag

Es sollen funktionsfähige Software- und Hardware-Komponenten entwickelt werden, mit denen es möglich ist Akkus für eBikes und Pedelecs hinsichtlich ihres Spannungverlaufes zu überwachen. Das System soll plattformunabhängig laufen und die Hardware sollte mittels USB mit dem PC verbunden werden können.

## Technische Anforderungen

Die Anwendung soll den Spannungsverlauf eines 50V Akku über einen längeren Zeitraum überwachen. Dabei soll die Messung die Spannungswerte mit Zeitstempel in ein Dokument schreiben. Die Messung soll so lange laufen, bis ein festgelegter Schwellenwert unterschritten wird. Wird die Messung vorzeitig unterbrochen, indem beispielsweise die Hardware getrennt wird, soll eine entsprechende Fehlermeldung mit ausgegeben werden.
Das System basiert auf einer Hardware und einer Softwarekomponente. Die Hardware basiert auf dem nodeMCU. Hier ist zu beachten, dass dieser mit einer maximalen Spannung von 3V belastet werden kann. Aus diesem Grund muss die Spannung des Akkus von 50V mittels eines Spannungsteilers auf 3V heruntergeregelt werden. Dies wird über ein Steckbrett, Verbindungen und einem 15 kΩ und 1 kΩ Widerstand realisiert. (Siehe Entwurfsdokumentation).
Der Hardwareteil wird über USB an den PC verbunden. So bekommt die Software die Werte der Messung geliefert. Die Software wird in Python entwickelt, damit sie plattformunabhängig ist. Dort werden die Messwerte wieder auf ihre eigentliche Größe hochgerechnet und mit Zeitstempeln in ein Dokument geschrieben.
Wird ein Schwellenwert bei der Messung unterschritten, wird eine Abschlussmeldung in das Dokument geschrieben. Bei vorzeitigem Beenden wird eine Fehlermeldung dokumentiert.

###	Entwurfsdokumentation
![Schaltplan](https://github.com/Erik613/Spannungsueberwachung/blob/master/img/Schaltplan.png)
 
 
### Optionale Features

### Problemanalyse

Eine essentielle Schwierigkeit liegt darin, dass bei dem Akku Spannungen von 50V auftreten können. Die Ausgänge des nodeMCU können allerdings nur Spannungen von 3V aushalten. Deshalb muss die Spannung heruntergeregelt werden, damit die Bauteile nicht beschädigt werden. Dies wird über einen Spannungsteiler realisiert, der aus einem 15 kΩ und einen 3  kΩ Widerstand besteht.
Ein weiteres Problem könnte die Kommunikation zwischen dem Arduino und der PC-Software darstellen.

## Rahmenbedingungen

### Zeitplan

- 10.01.2020 fertiges Pflichtenheft mit Entwurfsdokumentation
- 17.01.2020 Programmablaufsplan
- 24.01.2020 lauffähige Programmteile (Arduino/Python) und             			     Zusammenschluss von Hardware und Software
- 31.01.2020 fertige Anwendung (vorzugsweise Ausreichend getestet)

## Glossar







