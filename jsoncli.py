#!/usr/bin/env python3
import json
import argparse
import sys

def pretty_print(json_data):
    print(json.dumps(json_data, indent=4, ensure_ascii=False))

def get_value(json_data, path):
    keys = path.split('.')
    current = json_data
    try:
        for key in keys:
            if isinstance(current, list):
                key = int(key)  # jeśli indeks listy
            current = current[key]
        print(json.dumps(current, indent=4, ensure_ascii=False))
    except (KeyError, IndexError, ValueError, TypeError):
        print(f"Error: ścieżka '{path}' nie istnieje w JSON", file=sys.stderr)
        sys.exit(1)

def validate_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json.load(f)
        print("JSON jest poprawny")
    except json.JSONDecodeError as e:
        print(f"Błąd JSON: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="JsonCLI - narzędzie do pracy z JSON w terminalu")
    parser.add_argument("file", help="Plik JSON do przetworzenia")
    parser.add_argument("--pretty", action="store_true", help="Wyświetl ładnie sformatowany JSON")
    parser.add_argument("--get", metavar="PATH", help="Pobierz wartość pod ścieżką np. user.name lub items.0.id")
    parser.add_argument("--validate", action="store_true", help="Sprawdź poprawność JSON")

    args = parser.parse_args()

    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Błąd podczas wczytywania JSON: {e}", file=sys.stderr)
        sys.exit(1)

    if args.validate:
        print("JSON jest poprawny")
        sys.exit(0)

    if args.get:
        get_value(data, args.get)
        sys.exit(0)

    if args.pretty:
        pretty_print(data)
        sys.exit(0)

    # Jeśli żadna flaga nie została podana, wyświetl podstawowy JSON
    print(json.dumps(data))

if __name__ == "__main__":
    main()