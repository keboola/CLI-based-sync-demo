# Storage comparison result 


## Comparison environments 'prod' vs 'dev' 


## Project 'L1' vs project 'L1'


### Storage structure is the same

No changes detected

## Project 'L0' vs project 'L0'


### Bucket modified

{'id': 'in.c-test', 'name': 'c-test', 'stage': 'in', 'displayName': 'test', 'description': '', 'backend': 'snowflake', 'sharing': 'specific-projects', 'sharingParameters': {'projects': [{'id': 9997, 'name': '[PROD] CLI stages L1'}]}}

### Bucket removed

{'id': 'out.c-create-table-test', 'name': 'c-create-table-test', 'stage': 'out', 'displayName': 'create-table-test', 'description': '', 'backend': 'snowflake', 'sharing': None}

### Bucket removed

{'id': 'in.c-keboola-ex-google-drive-1119451229', 'name': 'c-keboola-ex-google-drive-1119451229', 'stage': 'in', 'displayName': 'keboola-ex-google-drive-1119451229', 'description': '', 'backend': 'snowflake', 'sharing': None}

### Table added

{'id': 'in.c-test.testaccount', 'isTyped': False, 'name': 'testaccount', 'distributionType': None, 'distributionKey': [], 'indexType': None, 'indexKey': [], 'bucket': {'id': 'in.c-test', 'name': 'c-test', 'stage': 'in', 'displayName': 'test', 'description': '', 'backend': 'snowflake', 'sharing': 'specific-projects', 'sharingParameters': {'projects': [{'id': 9997, 'name': '[PROD] CLI stages L1'}]}}, 'primaryKey': [], 'transactional': False, 'columns': ['Name', 'SubAccount', 'FullyQualifiedName', 'Active', 'Classification', 'AccountType', 'AccountSubType', 'CurrentBalance', 'CurrentBalanceWithSubAccounts', 'Currency', 'TaxCode', 'ID'], 'syntheticPrimaryKeyEnabled': False, 'columnMetadata': {'Name': [{'id': '1718259536', 'key': 'KBC.datatype.basetype', 'value': 'STRING', 'provider': 'user', 'timestamp': '2024-05-15T15:18:45+0200'}, {'id': '1718259537', 'key': 'KBC.datatype.nullable', 'value': '1', 'provider': 'user', 'timestamp': '2024-05-15T15:18:45+0200'}, {'id': '1718259538', 'key': 'KBC.datatype.length', 'value': '255', 'provider': 'user', 'timestamp': '2024-05-15T15:18:45+0200'}]}}

### Table removed

{'id': 'out.c-create-table-test.out', 'isTyped': False, 'name': 'out', 'distributionType': None, 'distributionKey': [], 'indexType': None, 'indexKey': [], 'bucket': {'uri': 'https://connection.keboola.com/v2/storage/buckets/out.c-create-table-test', 'id': 'out.c-create-table-test', 'name': 'c-create-table-test', 'displayName': 'create-table-test', 'idBranch': 865218, 'stage': 'out', 'description': '', 'tables': 'https://connection.keboola.com/v2/storage/buckets/out.c-create-table-test', 'created': '2024-04-29T13:18:19+0200', 'lastChangeDate': '2024-05-15T15:51:30+0200', 'isReadOnly': False, 'dataSizeBytes': 1536, 'rowsCount': 2, 'isMaintenance': False, 'backend': 'snowflake', 'sharing': None, 'hasExternalSchema': False, 'databaseName': ''}, 'primaryKey': [], 'transactional': False, 'columns': ['NUM', 'STR', 'Text'], 'syntheticPrimaryKeyEnabled': False, 'columnMetadata': {'NUM': [{'id': '1718019337', 'key': 'KBC.datatype.type', 'value': 'NUMBER', 'provider': 'storage', 'timestamp': '2024-04-29T13:18:34+0200'}, {'id': '1718019338', 'key': 'KBC.datatype.nullable', 'value': '1', 'provider': 'storage', 'timestamp': '2024-04-29T13:18:34+0200'}, {'id': '1718019339', 'key': 'KBC.datatype.basetype', 'value': 'NUMERIC', 'provider': 'storage', 'timestamp': '2024-04-29T13:18:34+0200'}, {'id': '1718019340', 'key': 'KBC.datatype.length', 'value': '1,0', 'provider': 'storage', 'timestamp': '2024-04-29T13:18:34+0200'}, {'id': '1718019351', 'key': 'KBC.datatype.type', 'value': 'NUMBER', 'provider': 'keboola.snowflake-transformation', 'timestamp': '2024-04-29T13:18:35+0200'}, {'id': '1718019352', 'key': 'KBC.datatype.nullable', 'value': '1', 'provider': 'keboola.snowflake-transformation', 'timestamp': '2024-04-29T13:18:35+0200'}, {'id': '1718019353', 'key': 'KBC.datatype.basetype', 'value': 'NUMERIC', 'provider': 'keboola.snowflake-transformation', 'timestamp': '2024-04-29T13:18:35+0200'}, {'id': '1718019354', 'key': 'KBC.datatype.length', 'value': '1,0', 'provider': 'keboola.snowflake-transformation', 'timestamp': '2024-04-29T13:18:35+0200'}], 'STR': [{'id': '1718019341', 'key': 'KBC.datatype.type', 'value': 'VARCHAR', 'provider': 'storage', 'timestamp': '2024-04-29T13:18:34+0200'}, {'id': '1718019342', 'key': 'KBC.datatype.nullable', 'value': '1', 'provider': 'storage', 'timestamp': '2024-04-29T13:18:34+0200'}, {'id': '1718019343', 'key': 'KBC.datatype.basetype', 'value': 'STRING', 'provider': 'storage', 'timestamp': '2024-04-29T13:18:34+0200'}, {'id': '1718019344', 'key': 'KBC.datatype.length', 'value': '6', 'provider': 'storage', 'timestamp': '2024-04-29T13:18:34+0200'}, {'id': '1718019355', 'key': 'KBC.datatype.type', 'value': 'VARCHAR', 'provider': 'keboola.snowflake-transformation', 'timestamp': '2024-04-29T13:18:35+0200'}, {'id': '1718019356', 'key': 'KBC.datatype.nullable', 'value': '1', 'provider': 'keboola.snowflake-transformation', 'timestamp': '2024-04-29T13:18:35+0200'}, {'id': '1718019357', 'key': 'KBC.datatype.basetype', 'value': 'STRING', 'provider': 'keboola.snowflake-transformation', 'timestamp': '2024-04-29T13:18:35+0200'}, {'id': '1718019358', 'key': 'KBC.datatype.length', 'value': '6', 'provider': 'keboola.snowflake-transformation', 'timestamp': '2024-04-29T13:18:35+0200'}]}}

### Table removed

{'id': 'in.c-keboola-ex-google-drive-1119451229.test-Sheet1', 'isTyped': False, 'name': 'test-Sheet1', 'distributionType': None, 'distributionKey': [], 'indexType': None, 'indexKey': [], 'bucket': {'uri': 'https://connection.keboola.com/v2/storage/buckets/in.c-keboola-ex-google-drive-1119451229', 'id': 'in.c-keboola-ex-google-drive-1119451229', 'name': 'c-keboola-ex-google-drive-1119451229', 'displayName': 'keboola-ex-google-drive-1119451229', 'idBranch': 865218, 'stage': 'in', 'description': '', 'tables': 'https://connection.keboola.com/v2/storage/buckets/in.c-keboola-ex-google-drive-1119451229', 'created': '2024-04-29T13:20:57+0200', 'lastChangeDate': '2024-04-29T13:21:05+0200', 'isReadOnly': False, 'dataSizeBytes': 0, 'rowsCount': 0, 'isMaintenance': False, 'backend': 'snowflake', 'sharing': None, 'hasExternalSchema': False, 'databaseName': ''}, 'primaryKey': [], 'transactional': False, 'columns': ['Test_data'], 'syntheticPrimaryKeyEnabled': False, 'columnMetadata': {}}
