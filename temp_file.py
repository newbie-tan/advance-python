import json
from pprint import pprint

if __name__ == '__main__':
    with open("base_menu.json", "r", encoding="utf-8") as f:
        r = json.load(f)
        pprint(r)
