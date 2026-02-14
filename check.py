import json
f = open('website/data/symbols.json', 'r', encoding='utf-8')
try:
    data = json.load(f)
    print('Valid JSON')
    print('Categories:', len(data['categories']))
    for c in data['categories']:
        print(f"  {c['id']}: {len(c['symbols'])} symbols")
    print('Total:', sum(len(c['symbols']) for c in data['categories']))
except json.JSONDecodeError as e:
    print(f'JSON ERROR: {e}')
finally:
    f.close()
