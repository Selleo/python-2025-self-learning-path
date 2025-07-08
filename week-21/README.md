## Tydzień 21: Dokumentacja projektu i podsumowanie architektury

✅ **Zadanie**: Udokumentuj API za pomocą narzędzi takich jak **Swagger** (integracja z FastAPI), dodając szczegóły dotyczące endpointów, parametrów i przykładów odpowiedzi.

---

### 📂 Przykładowa struktura katalogów projektu po Etapie 3 (Service Booking API)

- `service_booking_api/`  
  - `app/` — główna aplikacja
    - `__init__.py` — plik inicjalizacyjny
    - `main.py` — punkt wejścia aplikacji FastAPI (start + rejestracja routerów)
    - `core/` — podstawowe funkcje aplikacji
      - `config.py` — konfiguracje aplikacji (np. baza danych, S3, secret keys)
      - `security.py` — funkcje autoryzacji (np. JWT)
    - `db/` — inicjalizacja bazy danych
      - `__init__.py` — plik inicjalizacyjny
      - `database.py` — inicjalizacja bazy (SQLAlchemy + Async)
      - `models/` — modele bazy danych
        - `__init__.py` — plik inicjalizacyjny
        - `user.py` — model użytkownika
        - `order.py` — model zamówienia
      - `schemas/` — schematy Pydantic do walidacji danych wejściowych i wyjściowych
        - `__init__.py` — plik inicjalizacyjny
        - `user.py` — schemat użytkownika
        - `order.py` — schemat zamówienia
      - `crud/` — operacje CRUD (Create, Read, Update, Delete)
        - `__init__.py` — plik inicjalizacyjny
        - `user.py` — operacje CRUD użytkownika
        - `order.py` — operacje CRUD zamówienia
    - `routers/` — endpointy FastAPI
      - `__init__.py` — plik inicjalizacyjny
      - `user.py` — endpointy użytkowników
      - `order.py` — endpointy zamówień
      - `upload.py` — endpointy uploadu plików
    - `services/` — usługi pomocnicze
      - `__init__.py` — plik inicjalizacyjny
      - `s3_service.py` — obsługa AWS S3
      - `cache.py` — cache danych
    - `middlewares/` — middleware (np. autoryzacja, logowanie)
      - `__init__.py` — plik inicjalizacyjny
      - `auth_middleware.py` — middleware autoryzacji
      - `logging_middleware.py` — middleware logowania
    - `exceptions/` — wyjątki
      - `__init__.py` — plik inicjalizacyjny
      - `custom_exceptions.py` — własne wyjątki domenowe
    - `utils/` — funkcje pomocnicze
      - `__init__.py` — plik inicjalizacyjny
      - `validators.py` — własne walidatory Pydantic
      - `helpers.py` — funkcje pomocnicze
  - `tests/` — testy
    - `__init__.py` — plik inicjalizacyjny
    - `conftest.py` — setup testów
    - `unit/` — testy jednostkowe
      - `test_users.py` — testy dla użytkowników
      - `test_orders.py` — testy dla zamówień
    - `integration/` — testy integracyjne
      - `test_endpoints.py` — testy endpointów
      - `test_upload.py` — testy uploadu plików
  - `alembic/` — migracje bazy danych
    - `versions/` — katalog na pliki migracji bazy danych
  - `alembic.ini` — plik konfiguracyjny Alembic
  - `requirements.txt` — lista zależności Pythona
  - `README.md` — plik README z opisem projektu
  - `.env` — zmienne środowiskowe (np. URL bazy danych, klucze API)
  - `pytest.ini` — konfiguracja Pytest

### 🔄 Diagram — przepływ danych w Service Booking API (uproszczony)

- Klient (np. Frontend lub Postman)
    ↓
- FastAPI Router
    ↓
- Pydantic Schema (walidacja danych)
    ↓
- CRUD (SQLAlchemy)
    ↓
- PostgreSQL (DB)
    ↓
- ⤴️ (jeśli upload) -> AWS S3 (boto3)
    ↓
- Response JSON

- **Klient** wysyła zapytanie HTTP do API (np. `POST /orders`, `GET /users`).
- **FastAPI** obsługuje zapytanie, sprawdza autoryzację i waliduje dane.
- **Middleware** zajmuje się logowaniem i autoryzacją użytkownika.
- **API** komunikuje się z bazą danych przez **SQLAlchemy**, wykonując odpowiednie operacje CRUD.
- W przypadku potrzeby, API może wysłać dane na **AWS S3** (np. pliki związane z zamówieniem).
- **Serwis Cache** może zostać użyty do przechowywania danych do późniejszego użycia, aby zredukować obciążenie bazy danych.
- API zwraca odpowiedź do klienta w formacie JSON.
