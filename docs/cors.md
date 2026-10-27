\# Diagnoza CORS



\## Wynik testu



W konsoli przeglądarki wykonano zapytanie `fetch` do `http://localhost:8000/api/products/` ze strony `http://localhost:5173/`.



Przeglądarka zwróciła błąd `net::ERR\_CONNECTION\_REFUSED` oraz `TypeError: Failed to fetch`.



\## Status odpowiedzi



Nie otrzymano statusu HTTP, ponieważ połączenie z serwerem zostało odrzucone. W zakładce Network żądanie miało status `(failed)`.



\## Dlaczego dane nie dotarły do skryptu?



Przeglądarka nie mogła nawiązać połączenia z serwerem, dlatego skrypt nie otrzymał odpowiedzi z danymi. Ten wynik sam w sobie nie potwierdza błędu CORS.





\## Zadanie 3 – test dozwolonego i niedozwolonego Origin



\### Dozwolony Origin



Polecenie:



```powershell

curl.exe -s -D - -o NUL -H "Origin: http://localhost:5173" http://127.0.0.1:8000/api/products/

```



Najważniejsza część odpowiedzi:



```text

HTTP/1.1 200 OK

Content-Type: application/json

Vary: origin

access-control-allow-origin: http://localhost:5173

```



Serwer zwrócił status `200 OK` i nagłówek `access-control-allow-origin` z adresem dozwolonego frontendu.



\### Niedozwolony Origin



Polecenie:



```powershell

curl.exe -s -D - -o NUL -H "Origin: http://example.com" http://127.0.0.1:8000/api/products/

```



Najważniejsza część odpowiedzi:



```text

HTTP/1.1 200 OK

Content-Type: application/json

Vary: origin

```



W odpowiedzi nie ma nagłówka `access-control-allow-origin`, ponieważ `http://example.com` nie znajduje się na liście dozwolonych adresów.



\### Wniosek



Oba żądania otrzymały status `200 OK`, ale tylko odpowiedź dla dozwolonego Origin zawiera nagłówek CORS pozwalający przeglądarce udostępnić dane skryptowi.



CORS nie chroni danych przed bezpośrednim odczytem, ponieważ jest mechanizmem egzekwowanym przez przeglądarkę, a nie blokadą żądań wysyłanych przez narzędzia takie jak `curl`.





\## Zadanie 4 – ręczne sprawdzenie preflight



Wykonano zapytanie `OPTIONS` z nagłówkami `Origin: http://localhost:5173` oraz `Access-Control-Request-Method: POST`.



Najważniejsze nagłówki odpowiedzi:



```text

HTTP/1.1 200 OK

content-length: 0

access-control-allow-origin: http://localhost:5173

access-control-allow-headers: accept, authorization, content-type, user-agent, x-csrftoken, x-requested-with

access-control-allow-methods: DELETE, GET, OPTIONS, PATCH, POST, PUT

access-control-max-age: 86400

```



Serwer zaakceptował zapytanie kontrolne. Nagłówek `access-control-allow-origin` wskazuje dozwolone źródło, `access-control-allow-methods` wymienia dozwolone metody HTTP, a `access-control-allow-headers` określa nagłówki, których może używać żądanie. `access-control-max-age: 86400` oznacza, że przeglądarka może przechowywać wynik preflight przez maksymalnie 86400 sekund.



Przeglądarka odczytuje te nagłówki, aby zdecydować, czy może wysłać właściwe żądanie i udostępnić jego odpowiedź skryptowi.



\## Zadanie 6 – sprawdzenie braku SECRET\_KEY



Tymczasowo zmieniono nazwę pliku `.env` na `.env.tmp` i uruchomiono `python manage.py check`.



Django odmówiło uruchomienia i wyświetliło komunikat:



`SECRET\_KEY musi być ustawiony w pliku .env`



Po teście przywrócono nazwę `.env`.



Takie rozwiązanie jest bezpieczniejsze niż użycie domyślnego klucza, ponieważ aplikacja nie uruchomi się przypadkowo z publicznym lub nieprawidłowym kluczem.



\## Zadanie 7 – zmienne środowiskowe frontendu



Utworzono pliki `frontend/.env` oraz `frontend/.env.example` ze zmienną `VITE\_API\_URL=http://127.0.0.1:8000/api`.



W `App.jsx` użyto `console.log(import.meta.env.VITE\_API\_URL)`. W konsoli przeglądarki wyświetlił się adres API.



Zmienne dostępne we frontendzie Vite muszą mieć prefiks `VITE\_`. Bez niego zmienna nie będzie dostępna przez `import.meta.env`.



\## Zadanie 8 – zmienna VITE\_ nie jest sekretem



Dodano `VITE\_TAJNE=abc123` do `frontend/.env` i odczytano zmienną w `App.jsx`. Po wykonaniu `npm run build` wyszukanie `abc123` w plikach JavaScript w katalogu `dist` zwróciło `True`.



Zmienne z prefiksem `VITE\_` nie nadają się do przechowywania sekretów, ponieważ ich wartości są widoczne w zbudowanej aplikacji.



\## Zadanie 10 – test czystego klonu



Sklonowano repozytorium z gałęzi `naprawione` do nowego katalogu `django-api-test`.



Podczas testu wykryto brak pakietu `python-dotenv` w pliku `backend/requirements.txt`. Dodano pakiet do zależności, wykonano commit i wysłano poprawkę na GitHuba. Po aktualizacji klonu instalacja zależności i polecenie `python manage.py check` zakończyły się poprawnie.



Migracje bazy danych wykonano poprawnie. Zależności frontendu zainstalowano przez `npm install`, a `npm run build` zakończyło się powodzeniem.



Test pokazał, że czysty klon wymaga kompletnego pliku `requirements.txt`. Instrukcja w README pozwala odtworzyć konfigurację projektu.



