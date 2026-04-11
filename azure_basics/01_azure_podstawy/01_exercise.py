"""
01 Azure Cloud dla QA - cwiczenia (rozwiazania)
Kamil Bartocha | wersja 1.0
"""

import subprocess
import json
import datetime


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
# Sekcja 1 - Chmura obliczeniowa
# =============================================================================

# Cwiczenie 1.1 - nazwa i ID subskrypcji
account = az("account show")
name = account["name"]
sub_id = account["id"]
print(f"Subskrypcja: {name} (ID: {sub_id})")


# Cwiczenie 1.2 - klasyfikacja uslug Azure
SERVICES = [
    "Azure Virtual Machines",
    "Azure App Service",
    "Microsoft 365",
    "Azure Functions",
    "Azure Virtual Network",
    "Azure SQL Database",
    "Azure Blob Storage",
    "Azure Kubernetes Service",
]

classified = {
    "IaaS": ["Azure Virtual Machines", "Azure Virtual Network"],
    "PaaS": [
        "Azure App Service",
        "Azure Functions",
        "Azure SQL Database",
        "Azure Blob Storage",
        "Azure Kubernetes Service",
    ],
    "SaaS": ["Microsoft 365"],
}

for model, services in classified.items():
    print(f"{model}: {', '.join(services)}")


# Cwiczenie 1.3 - sprawdzenie stanu subskrypcji
account = az("account show")
state = account["state"]
if state == "Enabled":
    print("OK - subskrypcja aktywna")
else:
    print(f"UWAGA - stan: {state}")


# =============================================================================
# Sekcja 2 - Hierarchia Azure
# =============================================================================

# Cwiczenie 2.1 - tenant ID i subscription ID
account = az("account show")
tenant_id = account["tenantId"]
subscription_id = account["id"]
print(f"Tenant ID:       {tenant_id}")
print(f"Subscription ID: {subscription_id}")


# Cwiczenie 2.2 - tabela resource groups
groups = az("group list")
print(f"{'Nazwa':<40} {'Lokalizacja':<20} Stan")
print("-" * 72)
for rg in groups:
    name = rg["name"]
    location = rg["location"]
    state = rg["properties"]["provisioningState"]
    print(f"{name:<40} {location:<20} {state}")


# Cwiczenie 2.3 - resource groups per lokalizacja
groups = az("group list")
location_counts = {}
for rg in groups:
    location = rg["location"]
    location_counts[location] = location_counts.get(location, 0) + 1

for location, count in sorted(location_counts.items()):
    print(f"{location}: {count}")


# =============================================================================
# Sekcja 3 - Azure CLI
# =============================================================================

# Cwiczenie 3.1 - wersja CLI
version_info = az("version")
cli_version = version_info["azure-cli"]
print(f"Azure CLI: {cli_version}")


# Cwiczenie 3.2 - --query dla pol name i location
groups = az("group list --query [].{name:name,location:location}")
for rg in groups:
    print(f"{rg['name']:<40} {rg['location']}")


# Cwiczenie 3.3 - output tsv, podzial na linie
raw = az("group list --query [].name", output="tsv")
names = raw.splitlines()
print(f"Znalezione resource groups ({len(names)}):")
for name in names:
    print(f"  {name}")


# Cwiczenie 3.4 - resource_group_exists
def resource_group_exists(name):
    names = az("group list --query [].name")
    return name in names


print(resource_group_exists("rg-qa-lab"))
print(resource_group_exists("rg-nie-istnieje"))


# =============================================================================
# Sekcja 4 - Regiony
# =============================================================================

# Cwiczenie 4.1 - liczba regionow i 5 pierwszych
locations = az("account list-locations")
total = len(locations)
sorted_names = sorted(loc["name"] for loc in locations)
print(f"Laczna liczba regionow: {total}")
print("Pierwsze 5 (alfabetycznie):")
for name in sorted_names[:5]:
    print(f"  {name}")


# Cwiczenie 4.2 - regiony europejskie po regionalDisplayName
locations = az("account list-locations")
eu_regions = [
    loc["name"]
    for loc in locations
    if "(Europe)" in loc.get("regionalDisplayName", "")
]
print(f"Regiony europejskie ({len(eu_regions)}):")
for region in sorted(eu_regions):
    print(f"  {region}")


# Cwiczenie 4.3 - sprawdzenie czy 'polandcentral' istnieje
locations = az("account list-locations")
target = "polandcentral"
found = next((loc for loc in locations if loc["name"] == target), None)
if found:
    print(f"Znaleziono: {found['displayName']}")
else:
    print(f"Nie znaleziono regionu '{target}'")


# =============================================================================
# Sekcja 5 - Tagowanie
# =============================================================================

# Cwiczenie 5.1 - build_qa_tags z parametrami
def build_qa_tags(project, env="test", owner="qa-team"):
    ttl = (datetime.date.today() + datetime.timedelta(days=1)).isoformat()
    return {
        "env": env,
        "owner": owner,
        "project": project,
        "ttl": ttl,
    }


tags = build_qa_tags("azure-basics")
print(tags)


# Cwiczenie 5.2 - tworzenie resource group z tagami
rg_name = "rg-qa-lab-kb"
tags = build_qa_tags("azure-basics")
tags_str = " ".join(f"{k}={v}" for k, v in tags.items())
result = az(f"group create --name {rg_name} --location westeurope --tags {tags_str}")
print(f"Nazwa: {result['name']}")
print(f"Tagi:  {result['tags']}")


# Cwiczenie 5.3 - resource groups z tagiem owner=qa-team
groups = az("group list")
qa_groups = [
    rg for rg in groups
    if rg.get("tags", {}).get("owner") == "qa-team"
]
print(f"Resource groups z owner=qa-team: {len(qa_groups)}")
for rg in qa_groups:
    print(f"  {rg['name']}")


# Cwiczenie 5.4 - cleanup_expired_rgs
def cleanup_expired_rgs(dry_run=True):
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
    print(f"Usunieto {len(removed)} resource groups.")
    return removed


cleanup_expired_rgs(dry_run=True)
