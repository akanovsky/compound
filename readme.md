# 1 **Instalace aplikace**

Stažení z Github
`git clone https://github.com/akanovsky/compounds.git`

Instalace balíčků Django,Django filters, rdkit.
V adresáři compounds spustit
`pip install -r requirements.txt`

Po instalaci je potřeba nastavit příkazovou řádku do adresáře compoundweb.
Ujistěte se, že v adresáři se nachází soubor manage.py

Následně naimportujte data ze vstupního csv souboru
`python manage.py load_data --path /cesta/k/vasemu/soboru.csv`

Následuje vytvoření schémat
`python manage.py create_images --path /cesta/k/vasemu/soboru.csv`

Aplikaci spustíme
`python manage.py runserver`

Ve webovém prohlížeči přejdeme na adresu
`http://127.0.0.1:8000/catalog`

Případně je třeba adresu upravit podle informace v řádku "Starting development server at" po spuštění serveru

# 2 **Použití aplikace**

Přihlášení do aplikace
- volba HOME --> Login HERE

  - Založen uživatel admin s heslem "heslo1234" (bez uvozovek)

Prohlížení látek
- volba Compound list
  - možnost filtrování dle názvu látky(Name) a knihovny(Library)
  - v případě, že látek je více než 20, je na konci stránky možnost přejít na další stranu
  

