# Big Data und Infrastruktur

## HINWEIS
**Alle Folien zu Cloud werden in der Klausur wichtig**

## Was ist Big Data?

### Definition / Einführung

- Keine Standarddefinition
  - Erstmalig GARTNER Group (2012): High volume, high velocity, high variety => require new forms of processing
- Kein Unterschied zu Business Intelligence
- Treffender: Highest Volume (unbeherrschbar)
- 3 (4, 5) V's (Klausur)
  - Volume, Scale of Data
  - Velocity, Analysis of Streaming Data
  - Variety, Different Forms of Data
  - (Veracity, Uncertainty of Data)
  - (Value)
- Volume
  - Most Companies have 100TB each
  - 2.3 Billionen GB every day
  - 6 Mrd. have a cellphone
  - 40 Zettabytes created 2020
- Velocity
  - Modern Cars 100 Sensors
  - 1TB NYSE Data every day
  - 19 Mrd. Network Connections each day
- Variety
  - 150 Exabytes in Healthcare
  - 30 Mrd. Posts auf Facebook jeden Monat
  - 400 Mio Tweets jeden Tag (200 Mio aktive User pro Monat)
  - 420 Mio Wearables (Smartwatch etc.)
  - 4+ Mrd. Videos jeden Monat auf Youtube geschaut
- Veracity
  - 1/3 Business Leaders don't trust information for decision making
  - 27% of Respondents in one survey where unsure how much of their data was inaccurate
  - Poor Data Quality costs the U.S. 3.1 Billionen Dollar / Jahr

### Big Data aus Sicht der Softwarehersteller

- Big Data = Transactions + Interactions + Observations

### Datenmengen (Klausur)

- Size stored:
  - Google: 15.000 Petabytes
  - NSA: 10.000 Petabytes
  - Facebook: 300 Petabytes
  - eBay: 90 Petabytes
- Data processed per Day
  - Google: 100 PB
  - eBay: 100 PB
  - NSA: 28 PB
  - Facebook: 0,6 PB
  
 ## Landscape
 4 Kategorien von Daten
 - Infrastruktur
    - Prozess und Speicherung, ggf. auch Analyse von Daten
 - Integration
    - Analyse auf mehreren Ebenen
 - Engineering
    - Monetarisierung 
 - MISSING
 
## Typen der Datenanalyse
- Kundenprobleme
    - Business Sense of Data
    - Real Time oder Batch Analyse für Prediktionen
        - Real Time Probleme sind Probleme die keine Latenz erlauben (COVID-19, Fraud Detection)
        - Batch erlaubt es zu klären, warum etwas passiert ist und wie sich daraus zukünftige Ereignisse ableiten lassen (Amazon & eBay Kaufempfehlung)
 
### Definitionen
- alle nicht einheitlich
- KLAUSUR: Definitionen und Gemeinsamkeiten & Unterscheide BD & BI **VERSTEHEN** und **EIGENE RECHERCHEN** | Eigene Beispiel und aktuelle Entwicklung (weniger BI mehr BD Jobs)
### Big Data
- BITKOM: Datenmenge (Volume), Datenvielfalt (Variety), Datengeschwindigkeit (Velocity), Erkennen von Zusammenhängen (Analytics)
    - 3 V's + Analytics
- Größtenteils Auswertungen auf unstrukturierten Daten
    
### Business Intelligence
- Sammelbegriff für den IT-gestützten Zugriff auf Daten
- Aus diesem Wissen soll Handlungsentscheidungen des Managements ermöglichen
- Unterschied zu BD --> strukturierte Daten werden verdichtet für "einfache Antworten"

### Data Science
- Mischung aus BD & BI
- Sinnvolle Informationen aus strukturierten Daten aus der BI und den unstrukturierten Daten der BD ziehen
- Dient ebenfalls der Entscheidungsfindung
- Zusammenhang BI --> Überschneidungen
- DS dient eher der Prediktion

## Cloud Computing
- Def (BSI): Dynamisches Anbieten, Nutzen und Abrechnen von IT-Dienstleistungen

## Unterschiedliche Ansätze der IT
### Traditionelle IT
- Sicherheit
- Effizienz
- Ruhe & Genauigkeit

### Non-lineare IT
- Nicht sequentiell
- Agil, z.T. vieles im Beta-Stadium
- Hoher Innovationsgrad
- Unruhe im Sinne von kont. Weiterentwicklung

## Handlungsfelder der Cloud
- Strategie
    - Roadmap von OnPrem zu Cloud
- Architektur & Technologie
    - Sichere Infrastruktur
    - u.a. SaaS
- Migration
    - Methoden
    - Vertragsauswahl
- Datenschutz
    - Compliance
    - Anonymisierung
    - Pers.bezo und F&E-Daten
- Datensicherheit
    - Verschlüsselung
    - Schutz vor Zugriff Dritter
- Governance
    - Mitarbeiter & Skills
    - Motivation / Mindset
    
## 4 Säulen der Digitalisierung
- Zukunftsorientierte Mensch-Maschine Interaktion
- Ganzheitliche Integrationsarchitekturen
- Effektive Analytics & Business Insights
- Reaktionsfähige hybride Infrastrukturen

## Cloud Modelle
### IaaS
_Infrastructure as a Service_
- Rechner und Speicherkapzitäten werden gemietet
- Zielgruppe: Kunden die Hardwarekosten sparen wollen

### PaaS
_Platform as a Service_
- Laufzeitumgebung für Webanwendungen, Test- oder Entwicklungsumgebungen
- Zielgruppe: Kunden, die schnell Umgebungen benötigen, diese aber nicht vorhalten wollen

### SaaS
_Software as a Service_
- Software on Demand, pay as you use
- standardisierte Software (Dropbox, Office365)
- Kunden die Software nur nutzen möchten und keine Verantwortung über SLA oä. haben möchten

### Grad der Integration
IaaS --> PaaS --> SaaS



## Cloud-Typen (KLAUSUR)
### Private Cloud
- Kunde betreibt die Cloud
- Services werden nur für die interne Nutzung bereitgestellt
- hohe Investitionkosten
- **Interne-IT mit Cloud-Mechanismen**

### Public Cloud
- nicht öffentlich für alle, sondern von jedem "mietbar"
- Zahlung nach Nutzung, sehr geringe Investitionskosten
- **komplett ausgelagerte IT**

### Hybrid Cloud
- Mischform
- meist auf das wesentliche konzentriert

## Virtualisierung in der Cloud
- ermöglicht maßgeschneiderte Server
- Linux das meist-virtualisierte System in der Azure Cloud

## Faktoren für die Entscheidung für eine Cloud
- Ausfallsicherheit
- Produktivität
- Flexibilität
- Datenschutz und -sicherheit
- Kosten
- Externe Abhängigkeit  

## Self-Managed vs. Provider Managed (KLAUSUR)
4 Bereiche zu vergleichen
- Betrieb
- Security
- Kontrolle
- Hochverfügbarkeit