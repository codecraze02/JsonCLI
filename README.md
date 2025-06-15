# JsonCLI

Narzędzie CLI do pracy z plikami JSON.

## Funkcje

- Wyświetlanie ładnie sformatowanego JSON (`--pretty`)
- Pobieranie wartości pod ścieżką (`--get user.name`)
- Walidacja poprawności JSON (`--validate`)

## Instalacja

1. Sklonuj repozytorium:

```bash
git clone https://github.com/twojlogin/JsonCLI.git
cd JsonCLI
```

2. (Opcjonalnie) Dodaj uprawnienia do uruchomienia:

```bash
chmod +x jsoncli.py
```
## Użycie

```bash
./jsoncli.py data.json --pretty
./jsoncli.py data.json --get user.name
./jsoncli.py data.json --validate
```
## Przykład JSON

{
    "user": {
        "name": "Jan",
        "age": 30
    },
    "items": [
        {"id": 1, "name": "Miecz"},
        {"id": 2, "name": "Tarcza"}
    ]
}

## Przykładowe wywołania

Wyświetl ładnie cały JSON:

./jsoncli.py data.json --pretty

Pobierz nazwę użytkownika:

./jsoncli.py data.json --get user.name

Sprawdź, czy JSON jest poprawny:

./jsoncli.py data.json --validate

---
