import os
import json

def load_translations(lang, base_path="."):
    """
    Scans entire project recursively
    and merges all *_LANG.json files.
    """
    lang = lang.upper()
    merged = {}

    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(f"_{lang}.json"):
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        merged.update(data)
                except Exception as e:
                    print(f"Error loading {path}: {e}")

    return merged
