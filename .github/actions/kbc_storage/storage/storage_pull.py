import json
import requests
import os

BASE = os.environ['KBC_STORAGE_API_HOST']
TOKEN = os.environ['KBC_STORAGE_API_TOKEN']
HEAD = {'X-StorageApi-Token': TOKEN}

output_storage_structure_file = 'storage.json'


def get_tables():
    tables = requests.get(url=''.join(['https://', BASE, '/v2/storage/tables']), headers=HEAD,
                          params={'include': 'buckets,columns,metadata,columnMetadata'})
    return tables.json()


with open(output_storage_structure_file, 'w') as f:
    json.dump(get_tables(), f, indent=4)

print(f'Storage structure saved to {output_storage_structure_file}')

# Udělej github akci co si stáhne storage.json z aktuální branch a z cílové (jak se bude vybírat?)
# vygeneruje seznam změn (akce jako v keboola.app-merge-branch-storage)
# následně asi nějaký skript co je bude umět zpracovat nebo vygeneruje komponentu keboola.app-merge-branch-storage!