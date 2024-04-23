#!/bin/bash

set -eo pipefail

# Kontrola, jestli jsou nastaveny potřebné proměnné prostředí
required_vars=(KBC_STORAGE_API_TOKEN KBC_PROJECT_ID KBC_BRANCH_ID WORKDIR)
for var in "${required_vars[@]}"; do
  if [ -z "${!var}" ]; then
    echo "Error: Environment variable $var is not set." >&2
    exit 1
  fi
done

# Název souboru
MANIFEST_FILE="$WORKDIR/.keboola/manifest.json"

# Aktualizace hodnoty name v JSON souboru
jq --argjson project_id "$KBC_PROJECT_ID" --argjson project_id "$KBC_PROJECT_ID" '.project.id = $project_id  ' "$MANIFEST_FILE" > temp.json && mv temp.json "$MANIFEST_FILE"


# Cesta k souboru .env.local
ENV_FILE="$WORKDIR/.env.local"

echo "KBC_STORAGE_API_TOKEN=\"$KBC_STORAGE_API_TOKEN\"" > "$ENV_FILE"
echo "KBC_PROJECT_ID=\"$KBC_PROJECT_ID\"" >> "$ENV_FILE"
echo "KBC_BRANCH_ID=\"$KBC_BRANCH_ID\"" >> "$ENV_FILE"

# Spuštění kbc pull s logováním
kbc pull -d "$WORKDIR" --force 2>&1 | tee "$RUNNER_TEMP/log.txt"


