# Oblig3_SindreHalsebakk

Opprettet repository lokalt med relevante filer:
  *main.py med logikk
  *test_leap_year_checker.py med tester
  *requirements.txt med avhengigheter
  
Opprettet public remote repository på GitHub
  *README.md ble opprettet
  *Pushet nevnte filer til remote repository

Opprettet .github/workflows-mappe og skrev egen workflow
  *Oblig3_SindreHalsebakk.yml:
    *Definerer ny job og dens trigger 
    *Bygger nytt miljø med siste ubuntuversjon 
    *Sjekker ut koden fra filene
    *Setter opp valgt Pythonversjon
    *Installerer avhengigheter fra requirements.txt
    *Kjører pytest på logikk
    
Testing av workflow:
  * Kommenterte koden:
    * Committet og pushet til GitHub, workflow kjørte, alle tester passerte

  * Gjorde en endring i en test for å fremprovosere feil:
    * Committet og pushet til Github, workflow kjørte, en test feilet

  * Rettet opp endringen i testen: 
    * Committet og pushet endring til GitHub, workflow kjørte, alle tester passerte
 
