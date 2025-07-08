## Tydzień 15: Paginacja i filtrowanie danych

✅ **Zadanie**: Zaimplementuj paginację i filtrowanie zamówień i użytkowników w API.

### Kroki:

1. Dodaj parametry `limit`, `offset`, `filter` do odpowiednich endpointów.
2. W SQLAlchemy przygotuj zapytania obsługujące paginację i filtrowanie po np. dacie lub statusie.
3. Ustandaryzuj odpowiedź API, aby zawierała informacje o stronicowaniu (`total`, `page`, `pagesize`).
4. Przetestuj odpowiedzi z różnymi filtrami i paginacją.

### 🎯 Rezultat:
Wydajne pobieranie dużych zbiorów danych z kontrolą liczby wyników.
