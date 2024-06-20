import json
import requests


class StoragePull:
    def __init__(self, host, token, destination_file):
        self._base = self._base_uni(host)
        self._token = token
        self._head = {'X-StorageApi-Token': self._token}
        self._destination_file = destination_file

    @staticmethod
    def _base_uni(host):
        if not host.startswith('https://'):
            return ''.join(['https://', host])
        return host

    def _get_tables(self):
        tables = requests.get(url=''.join([self._base, '/v2/storage/tables']), headers=self._head,
                              params={'include': 'buckets,columns,metadata,columnMetadata'})
        return tables.json()

    def _save_storage_structure(self, structure):
        with open(self._destination_file, 'w') as f:
            json.dump(structure, f, indent=4)

        print(f'Storage structure saved to {self._destination_file}')
        return self._destination_file

    def pull(self):
        return self._save_storage_structure(self._get_tables())
