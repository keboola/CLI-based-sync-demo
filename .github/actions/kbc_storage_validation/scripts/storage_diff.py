import json

STORAGE_STRUCTURE_DIFF_FILE = 'storage_structure_diff.json'

table_relevant_keys = ['id', 'uri', 'idBranch', 'isTyped', 'name', 'definition', 'distributionType', 'distributionKey',
                       'indexType',
                       'indexKey', 'bucket', 'primaryKey', 'transactional', 'columns', 'syntheticPrimaryKeyEnabled',
                       'columnMetadata']
bucket_relevant_keys = ['id', 'uri', 'idBranch', 'name', 'stage', 'displayName', 'description', 'backend', 'sharing',
                        'sharingParameters']
column_relevant_keys = ['id', 'columnMetadata', 'primaryKey']


class StorageDiff:
    def __init__(self, source_storage_structure_file, dest_storage_structure_file,
                 storage_structure_diff_file=STORAGE_STRUCTURE_DIFF_FILE):
        self._storage_structure_diff_file = storage_structure_diff_file
        self._source_project = None
        self._dest_project = None
        self._source_storage_structure_file = source_storage_structure_file
        self._dest_storage_structure_file = dest_storage_structure_file

    def compare(self):
        diff = []
        src_json = self._read_file(self._source_storage_structure_file)
        dest_json = self._read_file(self._dest_storage_structure_file)
        self._source_project = src_json['project_id']
        self._dest_project = dest_json['project_id']
        diff.extend(self._compare_buckets(src_json, dest_json))
        diff.extend(self._compare_tables(src_json, dest_json))
        return self._write_file(diff)

    @staticmethod
    def _filter_keys(in_dict, relevant_keys):
        return {k: in_dict.get(k, None) for k in relevant_keys if k in in_dict}

    @staticmethod
    def _compare_object(obj1, obj2, ignore_keys=None):
        if ignore_keys is None:
            ignore_keys = []

        keys_to_compare = set(obj1.keys()).union(set(obj2.keys())) - set(ignore_keys)

        for key in keys_to_compare:
            if key in obj1 and key in obj2:
                if obj1[key] != obj2[key]:
                    return False
            else:
                return False

        return True

    @staticmethod
    def _compose_bucket(project, bucket, event):
        bucket_uri = bucket['uri']
        branch_id = bucket['idBranch']
        uri_parts = bucket_uri.split('/')
        stack = uri_parts[2]
        bucket_id = uri_parts[-1]
        link = f"https://{stack}/admin/projects/{project}/branch/{branch_id}/storage/{bucket_id}"

        return {"event": event,
                "bucket": bucket,
                "link": link}

    def _compare_buckets(self, src_structure, dest_structure):

        events = []

        src_buckets = {table['bucket']['id']: self._filter_keys(table['bucket'], bucket_relevant_keys) for table in
                       src_structure['tables']}

        dest_buckets = {table['bucket']['id']: self._filter_keys(table['bucket'], bucket_relevant_keys) for table in
                        dest_structure['tables']}

        # Detect added and changed buckets
        for bucket_id, src_bucket in src_buckets.items():
            if bucket_id not in dest_buckets:
                events.append(self._compose_bucket(self._source_project, src_bucket, "ADD_BUCKET"))
                if src_bucket['sharing']:
                    events.append(self._compose_bucket(self._source_project, src_bucket, "SHARE_BUCKET"))
            else:
                dest_bucket = dest_buckets[bucket_id]

                if src_bucket['sharing'] != dest_bucket['sharing']:
                    events.append(self._compose_bucket(self._source_project, src_bucket, "SHARE_BUCKET"))
                if self._compare_object(src_bucket, dest_bucket, ignore_keys=['sharing', 'idBranch']):
                    events.append(self._compose_bucket(self._source_project, src_bucket, "MODIFY_BUCKET"))

        # Detect removed buckets
        for bucket_id, dest_bucket in dest_buckets.items():
            if bucket_id not in src_buckets:
                events.append(self._compose_bucket(self._dest_project, dest_bucket, "DROP_BUCKET"))

        return events

    def _compare_tables(self, src_structure, dest_structure):
        events = []

        src_tables = {table['id']: self._filter_keys(table, table_relevant_keys) for table in src_structure['tables']}

        dest_tables = {table['id']: self._filter_keys(table, table_relevant_keys) for table in dest_structure['tables']}

        # Detect added and changed tables
        for table_id, src_table in src_tables.items():

            if table_id not in dest_tables:
                src_table['bucket'] = self._filter_keys(src_table['bucket'], bucket_relevant_keys)
                events.append(
                    {"event": "ADD_TABLE", "table": src_table})
            else:
                dest_table = dest_tables[table_id]
                events.extend(self._compare_table_details(src_table, dest_table))

        # Detect removed tables
        for table_id, dest_table in dest_tables.items():
            if table_id not in src_tables:
                events.append({"event": "DROP_TABLE", "table": dest_table})

        return events

    def _compare_table_details(self, dev_table, prod_table):
        events = []

        # Compare columns
        dev_columns = set(self._filter_keys(dev_table['columns'], column_relevant_keys))
        prod_columns = set(self._filter_keys(prod_table['columns'], column_relevant_keys))

        added_columns = dev_columns - prod_columns
        removed_columns = prod_columns - dev_columns

        for column in added_columns:
            events.append({"event": "ADD_COLUMN", "table_id": dev_table['id'], "column": column})
        for column in removed_columns:
            events.append({"event": "DROP_COLUMN", "table_id": dev_table['id'], "column": column})

        # Compare primary keys
        if dev_table['primaryKey'] != prod_table['primaryKey']:
            if not prod_table['primaryKey']:
                events.append(
                    {"event": "ADD_PRIMARY_KEY", "table_id": dev_table['id'], "primary_key": dev_table['primaryKey']})
            elif not dev_table['primaryKey']:
                events.append({"event": "DROP_PRIMARY_KEY", "table_id": dev_table['id']})

        # Compare column metadata
        if dev_table['columnMetadata'] != prod_table['columnMetadata']:
            events.append({"event": "EDIT_COLUMNS_METADATA", "table_id": dev_table['id'],
                           "dev_metadata": dev_table['columnMetadata'], "prod_metadata": prod_table['columnMetadata']})

        return events

    def _write_file(self, data):
        with open(self._storage_structure_diff_file, 'w') as f:
            json.dump(data, f, indent=4)
        return self._storage_structure_diff_file

    @staticmethod
    def _read_file(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
