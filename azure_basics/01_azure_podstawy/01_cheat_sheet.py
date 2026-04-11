"""
01 Azure Cloud dla QA - cheat sheet
Kamil Bartocha | wersja 1.0

Najwazniejsze komendy i wzorce dla Module 01.
"""

import subprocess
import json
import datetime

# =============================================================================
# HELPER - uruchamianie Azure CLI z Pythona
# =============================================================================

def az(command, output="json"):
    """Run Azure CLI command and return parsed JSON or raw text."""
    full_cmd = ["az"] + command.split() + ["--output", output]
    result = subprocess.run(full_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Azure CLI error: {result.stderr.strip()}")
    if output == "json":
        return json.loads(result.stdout)
    return result.stdout.strip()


# =============================================================================
# KONTO I SUBSKRYPCJA
# =============================================================================

# Aktywna subskrypcja
account = az("account show")
# account["name"]        - nazwa subskrypcji
# account["id"]          - subscription ID
# account["tenantId"]    - tenant ID
# account["state"]       - "Enabled" / "Disabled"

# Wszystkie subskrypcje
subscriptions = az("account list")
for sub in subscriptions:
    print(f"{sub['name']}: {sub['id']} [{sub['state']}]")

# Zmiana aktywnej subskrypcji
# az("account set --subscription <id lub nazwa>")

# Wersja CLI
version = az("version")
# version["azure-cli"]  - np. "2.60.0"


# =============================================================================
# RESOURCE GROUPS
# =============================================================================

# Lista resource groups
groups = az("group list")
# groups[i]["name"]                          - nazwa
# groups[i]["location"]                      - lokalizacja
# groups[i]["tags"]                          - slownik tagow
# groups[i]["properties"]["provisioningState"] - "Succeeded"

# Tylko nazwy (JMESPath query)
names = az("group list --query [].name")

# Filtrowanie po lokalizacji
we_groups = az("group list --query \"[?location=='westeurope']\"")

# Filtrowanie po tagu (JMESPath)
test_groups = az("group list --query \"[?tags.env=='test']\"")

# Tworzenie resource group
result = az("group create --name rg-qa-lab --location westeurope")
# result["name"]
# result["properties"]["provisioningState"]  - "Succeeded"

# Usuwanie resource group (--yes bez potwierdzenia)
# az("group delete --name rg-qa-lab --yes")

# Sprawdzenie czy resource group istnieje
def resource_group_exists(name):
    names = az("group list --query [].name")
    return name in names


# =============================================================================
# REGIONY
# =============================================================================

# Lista wszystkich regionow
locations = az("account list-locations")
# locations[i]["name"]                - np. "westeurope"
# locations[i]["displayName"]         - np. "West Europe"
# locations[i]["regionalDisplayName"] - np. "(Europe) West Europe"

# Regiony europejskie
eu_locations = [
    loc for loc in locations
    if "(Europe)" in loc.get("regionalDisplayName", "")
]

# Sprawdzenie czy region istnieje
def region_exists(region_name):
    locations = az("account list-locations")
    return any(loc["name"] == region_name for loc in locations)


# =============================================================================
# TAGOWANIE
# =============================================================================

def build_qa_tags(project, env="test", owner="qa-team", pr=None, module="01"):
    """Build standard QA tag set for Azure resources."""
    ttl = (datetime.date.today() + datetime.timedelta(days=1)).isoformat()
    tags = {
        "env": env,
        "owner": owner,
        "project": project,
        "module": module,
        "ttl": ttl,
    }
    if pr:
        tags["pr"] = pr
    return tags


def create_tagged_rg(name, location, tags):
    """Create resource group with tags dict."""
    tags_str = " ".join(f"{k}={v}" for k, v in tags.items())
    return az(f"group create --name {name} --location {location} --tags {tags_str}")


def cleanup_expired_rgs(dry_run=True):
    """Delete resource groups where tag 'ttl' is past today."""
    today = datetime.date.today()
    groups = az("group list")
    removed = []
    for rg in groups:
        ttl_str = rg.get("tags", {}).get("ttl")
        if not ttl_str:
            continue
        try:
            ttl_date = datetime.date.fromisoformat(ttl_str)
        except ValueError:
            continue
        if ttl_date < today:
            print(f"{'[DRY RUN] ' if dry_run else ''}Removing {rg['name']} (ttl: {ttl_str})")
            if not dry_run:
                az(f"group delete --name {rg['name']} --yes")
            removed.append(rg["name"])
    return removed


# =============================================================================
# FORMAT WYJSCIA
# =============================================================================

# JSON (domyslny) - do przetwarzania w Python
groups_json = az("group list")

# Tabela - czytelna dla czlowieka
print(az("group list", output="table"))

# TSV - do parsowania w skryptach Bash
raw_tsv = az("group list --query [].name", output="tsv")
names_list = raw_tsv.splitlines()

# =============================================================================
# PRZYDATNE KOMENDY CLI (uruchamiane bezposrednio w terminalu)
# =============================================================================

# az login                                    # logowanie interaktywne
# az login --use-device-code                  # logowanie przez kod (CI/CD)
# az account show                             # aktywne konto
# az account list --output table              # wszystkie subskrypcje
# az group list --output table                # resource groups jako tabela
# az group list --query "[].{N:name,L:location}" --output table
# az account list-locations --output table    # dostepne regiony
# az version                                  # wersja CLI
# az --help                                   # pomoc
# az group --help                             # pomoc dla resource group
