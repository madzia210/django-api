\# Sklep fullstack



Projekt sklepu internetowego składający się z backendu Django oraz frontendu React.



\## Wymagania



\- Python

\- Node.js i npm



\## Backend – Django



\### Konfiguracja



W głównym katalogu projektu skopiuj `.env.example` do `.env` i uzupełnij własny klucz `SECRET\_KEY`.



\### Uruchomienie



W terminalu przejdź do katalogu `backend`:



```powershell

cd backend

python -m venv venv

.\\venv\\Scripts\\python.exe -m pip install -r requirements.txt

.\\venv\\Scripts\\python.exe manage.py migrate

.\\venv\\Scripts\\python.exe manage.py runserver

```



Backend działa pod adresem `http://127.0.0.1:8000/`.



\## Frontend – React



\### Konfiguracja



W katalogu `frontend` skopiuj `.env.example` do `.env`.



\### Uruchomienie



W drugim terminalu, z gł

