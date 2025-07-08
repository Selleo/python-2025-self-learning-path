## Tydzień 14: Obsługa plików i integracja z AWS S3

✅ **Zadanie**: Dodaj możliwość przesyłania i pobierania plików (np. potwierdzenia rezerwacji) na AWS S3.

### Kroki:

1. Skonfiguruj klienta AWS S3 (np. boto3) w projekcie.
2. Utwórz endpoint API do przesyłania pliku dla zamówienia (`POST /upload`).
3. Dodaj endpoint API do pobierania pliku z S3 (`GET /download/{order_id}`).
4. Przechowuj URL pliku w bazie danych powiązany z zamówieniem.

### 🎯 Rezultat:
Umożliwienie przesyłania i pobierania plików powiązanych z zamówieniami.
