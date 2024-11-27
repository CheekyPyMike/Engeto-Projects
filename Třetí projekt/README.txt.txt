Projekt 3: Scraper volebních dat

Tento projekt je součástí Engeto Online Python Akademie. Skript `projekt_3.py` stahuje a zpracovává data z volebních výsledků a ukládá je do souboru CSV.

Autor
Mykola Tichonov
Email: mykola.tikhonov@seznam.cz
Discord: phranschyze

Popis funkcionality
Skript načte HTML obsah ze zadané URL adresy, zpracuje tabulky dat a dynamicky získává další informace z propojených stránek. Výsledná data se ukládají do CSV souboru.

Použité knihovny
Skript používá následující knihovny:
- argparse: Pro zpracování argumentů příkazové řádky.
- BeautifulSoup (z balíčku `bs4`): Pro analýzu a zpracování HTML dokumentů.
- pandas: Pro manipulaci s tabulkovými daty a export do CSV.
- requests: Pro odesílání HTTP požadavků a získávání obsahu stránek.
- urllib.parse: Pro manipulaci s URL adresami.

Instalace knihoven
Knihovny je možné nainstalovat pomocí `pip`. Spusťte následující příkaz v terminálu:

```bash
pip install argparse beautifulsoup4 pandas requests atd...
Ukázka projektu:
  argument1 - https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103
  argument2 - vysledky_prostejov.csv
Spuštění programu:
python scrape_volby.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" "vysledky_prostejov.csv"

Částečný výstup:

code	location	registered	envelopes	valid	Občanská demokratická strana	Řád národa - Vlastenecká unie	CESTA ODPOVĚDNÉ SPOLEČNOSTI	Česká str.sociálně demokrat.	Radostné Česko
506761	Alojzov	205	145	144	29	0	0	9	0
589268	Bedihošť	834	527	524	51	0	0	28	1
589276	Bílovice-Lutotín	431	279	275	13	0	0	32	0
589284	Biskupice	238	132	131	14	0	0	9	0
589292	Bohuslavice	376	236	236	20	0	0	23	0
589306	Bousín	107	67	67	5	0	0	4	0




