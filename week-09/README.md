## Tydzień 9: Relacje między tabelami

✅ **Zadanie**: Zdefiniuj i wykorzystaj relacje między `users` a `orders`.

### Kroki:

1. W modelu `User` dodaj relację do wielu `Order` (`relationship` w SQLAlchemy).
2. W modelu `Order` dodaj klucz obcy (`ForeignKey`) do `User`.
3. Umożliw w API tworzenie zamówień przypisanych do konkretnego użytkownika.
4. Dodaj endpointy zwracające zamówienia danego użytkownika.

### 🎯 Rezultat:
Pełne powiązanie użytkowników z ich rezerwacjami (1:N).
