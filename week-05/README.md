# Etap 2: Praca z bazą danych — Service Booking API

## Tydzień 5: Inicjalizacja projektu i struktura katalogów

✅ **Zadanie**: Przygotuj projekt Service Booking API do pracy: opisz cel projektu, zainicjalizuj repozytorium i uporządkuj strukturę katalogów.

### Kroki:

1. **Opis projektu**  
   Celem aplikacji jest umożliwienie użytkownikom rezerwacji usług, takich jak spotkania czy konsultacje.  
   Każdy użytkownik może mieć wiele zamówień (rezerwacji).  
   Aplikacja będzie oferować API RESTful, przechowywać dane w PostgreSQL oraz umożliwiać pełne zarządzanie użytkownikami i rezerwacjami.

2. **Inicjalizacja repozytorium**  
   - Utwórz nowe repozytorium Git.
   - Dodaj plik `.gitignore` (ignoruj: `.venv/`, `__pycache__/`, `.env`, `alembic/versions/`).
   - Utwórz plik `README.md` z krótkim opisem projektu, jego celem i technologiami.

3. **Przykładowa Struktura katalogów projektu**  
   - `app/`
     - `api/` — endpointy FastAPI
     - `core/` — konfiguracje (np. ustawienia bazy danych, inicjalizacja aplikacji)
     - `models/` — modele danych SQLAlchemy
     - `crud/` — funkcje operujące na bazie danych (Create, Read, Update, Delete)
     - `schemas/` — schematy Pydantic do walidacji danych wejściowych i wyjściowych
     - `tests/` — testy jednostkowe dla poszczególnych warstw
     - `main.py` — główny punkt wejścia aplikacji FastAPI
   - `alembic/`
     - `versions/` — katalog na pliki migracji bazy danych
   - `.env` — plik na zmienne środowiskowe (np. URL bazy danych)
   - `requirements.txt` — lista wszystkich zależności Pythona

4. **Biblioteki** 
   - FastAPI
   - Uvicorn
   - SQLAlchemy
   - Alembic
   - Pydantic
   - psycopg2-binary (lub asyncpg, jeśli planujesz zapytania asynchroniczne)

### 🎯 Rezultat:

- Gotowe repozytorium Git
- README.md z opisem projektu
- Struktura katalogów zgodna ze standardami
- Przygotowane środowisko deweloperskie z zainstalowanymi bibliotekami
