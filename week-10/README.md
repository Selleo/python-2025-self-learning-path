## Tydzień 10: Transakcje i zarządzanie błędami

✅ **Zadanie**: Wprowadź obsługę transakcji i poprawne zarządzanie błędami w operacjach na bazie.

### Kroki:

1. Stosuj sesje SQLAlchemy w kontekście transakcji (`session.begin()`).
2. Obsłuż typowe wyjątki, np. `IntegrityError`, `NoResultFound`.
3. Dodaj globalny handler błędów w FastAPI dla zwracania czytelnych komunikatów.
4. Przetestuj scenariusze błędne: nieistniejący użytkownik, podwójna rejestracja.

### 🎯 Rezultat:
Bezpieczne i przewidywalne operacje CRUD z pełnym zarządzaniem wyjątkami.
