# Syllabus: Azure Cloud dla QA Automation Engineer
**Autor:** Kamil Bartocha | **Wersja:** 1.0 | **Poziom:** Sredniozaawansowany/Zaawansowany

---

## Cel kursu

Kurs przeznaczony dla doswiadczonych inzynierow automatyzacji testow (5+ lat, Python/Pytest),
ktorzy chca zrozumiec Azure Cloud w kontekscie testowania systemow API-driven i Big Data.
Po kursie uczestnik bedzie potrafil projektowac strategie testowania dla aplikacji chmurowych,
uzywac Azure SDK w Pythonie oraz budowac pipeline'y CI/CD z testami na Azure DevOps.

---

## Grupa docelowa

- Lead / Senior QA Automation Engineer
- Doswiadczenie: Python (Pytest), testowanie API, systemy rozproszone
- Brak wymaganej znajomosci Azure (kurs zaczyna od podstaw chmury)

---

## Mapa modułów

| Nr  | Modul                                      | Czas  |
|-----|--------------------------------------------|-------|
| 01  | Azure - podstawy i srodowisko pracy        | 3h    |
| 02  | Azure DevOps - CI/CD i Test Plans          | 4h    |
| 03  | Tozsamosc i bezpieczenstwo (AAD, Key Vault)| 3h    |
| 04  | Azure Storage - dane testowe w chmurze     | 3h    |
| 05  | Testowanie REST API z Azure API Management | 4h    |
| 06  | Messaging: Service Bus i Event Hubs        | 3h    |
| 07  | Serverless: Azure Functions i Logic Apps   | 3h    |
| 08  | Kontenery: AKS i Container Apps            | 4h    |
| 09  | Obserwowalnosc: Monitor i App Insights     | 3h    |
| 10  | Big Data: Data Factory i Synapse Analytics | 4h    |
| 11  | Wzorce testowania z Python SDK             | 4h    |
| 12  | Infrastructure as Code dla QA (Terraform)  | 3h    |

**Laczny czas:** ~41 godzin

---

## Modul 01 - Azure: podstawy i srodowisko pracy

**Cel:** Sprawne poruszanie sie po ekosystemie Azure bez wiedzy wstepnej.

### Tematy
- Czym jest chmura obliczeniowa - modele IaaS / PaaS / SaaS
- Struktura Azure: tenant, subskrypcja, grupa zasobow (resource group), zasob (resource)
- Azure Portal - nawigacja, dashboardy, Cost Management
- Azure CLI (`az`) - instalacja, logowanie, podstawowe komendy
- Azure Cloud Shell - praca bez lokalnej instalacji
- Regiony i strefy dostepnosci (availability zones) - wplyw na testy
- Tagowanie zasobow - konwencje dla srodowisk testowych (`env:test`, `owner:qa`)
- Azure Free Tier - co mozna uzywac bezplatnie

### Cwiczenia praktyczne
1. Zaloz konto Azure i skonfiguruj Azure CLI lokalnie
2. Utworz resource group `rg-qa-lab` w wybranym regionie przez CLI
3. Przejrzyj koszty symulowanej subskrypcji w Cost Management
4. Otaguj zasoby skryptem Bash/Python uzywajac Azure CLI

### Narzedzia
- Azure CLI, Azure Portal, Azure Cloud Shell

---

## Modul 02 - Azure DevOps: CI/CD i Test Plans

**Cel:** Budowanie pipeline'ow testowych i raportowanie wynikow w Azure DevOps.

### Tematy
- Azure DevOps vs GitHub Actions - kiedy co stosowac
- Repozytoria (Repos) - git workflow dla zespolow QA
- Azure Pipelines - YAML pipeline, agenci (hosted vs self-hosted)
- Etapy pipeline'u: build → test → deploy → verify
- Artefakty (Artifacts) - pakowanie i wersjonowanie testow
- Azure Test Plans - test cases, test suites, test runs, exploratory testing
- Publikowanie wynikow testow Pytest w formacie JUnit XML
- Powiadomienia i integracje (Slack, Teams, email)
- Branch policies - wymuszanie testow przed merge

### Cwiczenia praktyczne
1. Stworz projekt w Azure DevOps i podlacz repozytorium
2. Napisz YAML pipeline uruchamiajacy testy Pytest (hosted agent)
3. Skonfiguruj publikowanie raportu `pytest --junitxml=report.xml`
4. Dodaj branch policy wymagajacy przejscia pipeline'u przed PR merge
5. Zbuduj multi-stage pipeline: `test` → `deploy` → `smoke-test`

### Narzedzia
- Azure DevOps, Pytest, pytest-html, JUnit XML

---

## Modul 03 - Tozsamosc i bezpieczenstwo: AAD, RBAC, Key Vault

**Cel:** Bezpieczne uwierzytelnianie w testach i zarzadzanie tajnymi danymi.

### Tematy
- Azure Active Directory (AAD / Entra ID) - tenants, uzytkownicy, grupy
- Service Principal vs Managed Identity - co stosowac w testach automatycznych
- RBAC (Role-Based Access Control) - przydzielanie minimalnych uprawnien
- OAuth 2.0 i token JWT - jak dzialaja tokeny w Azure
- Pobieranie tokenow w Pythonie (`azure-identity`)
- Azure Key Vault - przechowywanie sekretow, certyfikatow, kluczy
- Pobieranie sekretow z Key Vault w testach Pytest (fixture)
- Rotacja sekretow - testy odporne na zmiane kluczy
- Skanowanie kodu pod katem wycieku sekretow (truffleHog, git-secrets)

### Cwiczenia praktyczne
1. Stworz Service Principal i przypisz mu role `Reader` na resource group
2. Pobierz token AAD w Pythonie uzywajac `azure-identity`
3. Dodaj sekret do Key Vault i odczytaj go w fixture Pytest
4. Napisz fixture `auth_token` wielokrotnego uzytku dla calego suite testow
5. Skonfiguruj pipeline tak, zeby sekrety nie byly w zmiennych YAML

### Narzedzia
- `azure-identity`, `azure-keyvault-secrets`, Pytest fixtures

---

## Modul 04 - Azure Storage: dane testowe w chmurze

**Cel:** Zarzadzanie danymi testowymi w Azure Storage - tworzenie, czyszczenie, izolacja.

### Tematy
- Typy storage: Blob, Table, Queue, File Share - kiedy co uzywac
- Azure Blob Storage - kontenery, obiekty, hierarchia
- Operacje CRUD na Blob Storage w Pythonie (`azure-storage-blob`)
- Azure Table Storage - NoSQL, partycje, klucze wierszy
- Azure Queue Storage - kolejki komunikatow, TTL
- Strategie danych testowych: test data factories, snapshot/restore
- Izolacja danych testowych - dedykowane kontenery per test run
- Czyszczenie danych po tescie - pytest fixtures `yield` + teardown
- Generowanie danych testowych: Faker + Azure Storage

### Cwiczenia praktyczne
1. Stworz Storage Account i kontener Blob przez CLI
2. Napisz fixture Pytest uploadujacy/pobierajacy plik z Blob Storage
3. Zaimplementuj test data factory zapisujacy rekordy do Table Storage
4. Napisz cleanup fixture czyszczacy dane po test run
5. *(Trudniejsze)* Zbuduj system snapshot/restore dla danych testowych

### Narzedzia
- `azure-storage-blob`, `azure-data-tables`, Faker

---

## Modul 05 - Testowanie REST API z Azure API Management

**Cel:** Kompleksowe testowanie API hostowanego w Azure APIM.

### Tematy
- Azure API Management (APIM) - architektura: gateway, developer portal, backend
- Polityki APIM (policies) - rate limiting, transformacje, mock responses
- Subskrypcje i klucze API - uwierzytelnianie w testach
- Testowanie z `requests` i `httpx` (async) w Pythonie
- Parametryzacja testow API - `pytest.mark.parametrize`
- Schema validation - walidacja odpowiedzi JSON (Pydantic, jsonschema)
- Contract testing - Pact dla API w Azure
- Testowanie wersjonowania API (v1, v2)
- Mock server - testowanie bez backendu (mockoon, APIM mock policy)
- Performance testing API - locust + Azure Load Testing

### Cwiczenia praktyczne
1. Skonfiguruj API w APIM i przetestuj przez klienta HTTP w Pythonie
2. Napisz suite testow API z parametryzacja (pozytywne, negatywne, brzegowe)
3. Dodaj walidacje schematu odpowiedzi za pomoca Pydantic
4. Skonfiguruj rate limiting w APIM i napisz testy weryfikujace limit (429)
5. *(Trudniejsze)* Zaimplementuj contract testing z Pact dla wybranego API

### Narzedzia
- `requests`, `httpx`, `pytest`, Pydantic, Pact, Azure Load Testing

---

## Modul 06 - Messaging: Service Bus i Event Hubs

**Cel:** Testowanie systemow asynchronicznych i event-driven w Azure.

### Tematy
- Architektura message-driven vs event-driven - roznice w podejsciu do testow
- Azure Service Bus - kolejki (queues), tematy (topics), subskrypcje
- Operacje w Pythonie: publish, receive, settle (`azure-servicebus`)
- Dead-letter queue (DLQ) - testowanie obslugi bledow
- Azure Event Hubs - streaming zdarzen, consumer groups, partycje
- Producent i konsument w Pythonie (`azure-eventhub`)
- Strategie testowania async: polling, callbacks, test doubles
- Izolacja - dedykowane kolejki/tematy per test run
- Porownanie z Kafka - migracja testow

### Cwiczenia praktyczne
1. Stworz Service Bus namespace, kolejke i wyslij/odbierz wiadomosc w Pythonie
2. Napisz test weryfikujacy, ze wiadomosc trafia do DLQ po bledzie
3. Zbuduj prosty producer/consumer test dla Event Hubs
4. Napisz fixture tworzacy i usuwajacy dedykowane kolejki per test
5. *(Trudniejsze)* Przetestuj scenariusz: wiadomosc → przetworzenie → zapis do Storage

### Narzedzia
- `azure-servicebus`, `azure-eventhub`, Pytest

---

## Modul 07 - Serverless: Azure Functions i Logic Apps

**Cel:** Testowanie funkcji serverless i workflow automatyzacji.

### Tematy
- Azure Functions - triggery (HTTP, Timer, Service Bus, Blob, Event Hub)
- Lokalny development i testowanie: Azure Functions Core Tools
- Testy jednostkowe funkcji w Pythonie (pytest, unittest.mock)
- Testy integracyjne - deploymenty do srodowiska testowego
- Testowanie timeoutow i cold start
- Logic Apps - przeplywy pracy (workflows), konektory
- Testowanie Logic Apps - triggery reczne, historia uruchomien
- Durable Functions - testowanie long-running workflows
- Monitorowanie i logi funkcji w Application Insights

### Cwiczenia praktyczne
1. Stworz Azure Function z triggerem HTTP i przetestuj lokalnie
2. Napisz testy jednostkowe funkcji uzywajac `unittest.mock`
3. Deploy funkcji do Azure i napisz testy integracyjne end-to-end
4. Przetestuj funkcje z triggerem Service Bus - wyslij wiadomosc, weryfikuj efekt
5. *(Trudniejsze)* Napisz testy dla Logic App z kilkoma krokami i warunkami

### Narzedzia
- Azure Functions Core Tools, `azure-functions`, Pytest, `unittest.mock`

---

## Modul 08 - Kontenery: AKS i Container Apps

**Cel:** Uruchamianie testow w kontenerach i testowanie aplikacji kontenerowych.

### Tematy
- Kontenery w Azure: ACI, AKS, Container Apps - kiedy co stosowac
- Docker - podstawy dla QA: budowanie obrazow testowych, docker-compose
- Azure Container Registry (ACR) - przechowywanie obrazow
- Azure Kubernetes Service (AKS) - podstawy dla QA: pods, services, deployments
- `kubectl` - podstawowe komendy dla inzynirow testow
- Uruchamianie testow Pytest w kontenerach (Job, CronJob)
- Azure Container Apps - skalowanie testow, Jobs API
- Testowanie readiness/liveness probe
- Chaos engineering podstawy - testowanie odpornosci (Azure Chaos Studio)

### Cwiczenia praktyczne
1. Stwórz Dockerfile dla projektu testowego Pytest i zbuduj obraz
2. Wypchnij obraz do ACR i uruchom testy jako Azure Container Instance
3. Deploy prostej aplikacji na AKS i napisz testy smoke
4. Skonfiguruj Kubernetes Job uruchamiajacy suite testow
5. *(Trudniejsze)* Przetestuj autoskalowanie aplikacji pod obciazeniem

### Narzedzia
- Docker, `kubectl`, Azure CLI, `azure-mgmt-containerinstance`

---

## Modul 09 - Obserwowalnosc: Monitor i Application Insights

**Cel:** Uzycie telemetrii Azure do debugowania testow i weryfikacji zachowania systemu.

### Tematy
- Azure Monitor - metryki, logi, alerty, dashboardy
- Application Insights - traces, requests, exceptions, dependencies, custom events
- Log Analytics Workspace - Kusto Query Language (KQL) podstawy
- Weryfikacja logow w testach - assertions na logach aplikacji
- Metryki jako asercje testowe - "czy aplikacja jest zdrowa po deploymencie?"
- Distributed tracing - sledzenie requestow przez mikrouslugi
- Azure Monitor Alerts - testowanie alertow
- Custom metrics z SDK Pythona w testach
- Smoke tests post-deployment oparte na health endpoints

### Cwiczenia praktyczne
1. Skonfiguruj Application Insights i wyslij custom event z Pythona
2. Napisz zapytanie KQL zwracajace bledy z ostatnich 15 minut
3. Napisz test weryfikujacy, ze po akcji w aplikacji pojawia sie log w AI
4. Zbuduj post-deployment smoke test sprawdzajacy metryki w Monitor
5. *(Trudniejsze)* Przetestuj distributed trace - weryfikuj spany w Log Analytics

### Narzedzia
- `azure-monitor-query`, `opencensus-ext-azure`, KQL, Pytest

---

## Modul 10 - Big Data: Data Factory i Synapse Analytics

**Cel:** Testowanie pipeline'ow danych i walidacja jakosci danych w Azure.

### Tematy
- Azure Data Factory (ADF) - pipeline'y ETL/ELT, datasety, linked services
- Testowanie pipeline'ow ADF: triggery, debug runs, parametryzacja
- Azure Data Lake Storage Gen2 (ADLS) - hierarchiczny namespace
- Azure Synapse Analytics - workspace, dedicated SQL pool, Spark pool
- Strategie testowania danych: schema validation, row counts, data quality
- Great Expectations - framework do walidacji jakosci danych
- Testowanie transformacji Spark w Pythonie (pytest + pyspark)
- Delta Lake - testowanie ACID transactions
- Porownanie wynikow: expected vs actual dla pipeline'ow ETL

### Cwiczenia praktyczne
1. Uruchom pipeline ADF manualnie przez API i sprawdz status w Pythonie
2. Napisz test weryfikujacy liczbe rekordow po zaladowaniu danych
3. Zwaliduj schemat danych w ADLS uzywajac Pandas + pytest
4. Skonfiguruj Great Expectations dla datasetu i uruchom w pipeline
5. *(Trudniejsze)* Napisz end-to-end test: wgraj dane → uruchom ADF → weryfikuj wynik w Synapse

### Narzedzia
- `azure-mgmt-datafactory`, `azure-storage-file-datalake`, Great Expectations,
  PySpark, Pandas

---

## Modul 11 - Wzorce testowania z Python Azure SDK

**Cel:** Zaawansowane wzorce automatyzacji testow specyficzne dla Azure.

### Tematy
- Azure SDK dla Pythona - struktura pakietow `azure-*`
- Uwierzytelnianie w testach: `DefaultAzureCredential` vs explicit credential
- Pytest fixtures dla zasobow Azure - scope: function, class, session
- Parametryzacja po srodowiskach (dev/test/staging) - pytest + conftest
- Testowanie idempotentnosci operacji Azure
- Retry i resilience - testowanie z `tenacity`
- Mocking zasobow Azure - `unittest.mock`, `pytest-mock`, VCR cassettes
- Test isolation - dynamiczne nazwy zasobow, cleanup guarantees
- Raportowanie i metryki testow - Allure + Azure DevOps

### Cwiczenia praktyczne
1. Zbuduj zestaw fixture'ow sesyjnych dla Storage, Service Bus i Key Vault
2. Napisz testy parametryzowane dzialajace na 3 srodowiskach przez CLI flag
3. Napisz test idempotentnosci dla operacji zapisu do Blob Storage
4. Zaimplementuj VCR cassettes dla testow bez dostepen do Azure
5. *(Trudniejsze)* Zbuduj framework testowy z conftest.py dla calego projektu Azure

### Narzedzia
- `azure-identity`, `pytest-mock`, `vcrpy`, Allure, `tenacity`

---

## Modul 12 - Infrastructure as Code dla QA: Terraform

**Cel:** Autonomiczne tworzenie i niszczenie srodowisk testowych przez QA.

### Tematy
- Po co QA uzywa IaC - srodowiska on-demand, reproducibility
- Terraform podstawy - providers, resources, variables, outputs
- Provider `azurerm` - tworzenie zasobow Azure przez Terraform
- `terraform plan / apply / destroy` - cykl zycia srodowiska testowego
- Workspace'y Terraform - izolowane srodowiska (test-pr-123)
- Zmienne i sekrety w Terraform (Azure Key Vault, env variables)
- Terratest - testowanie infrastruktury Terraform w Go/Pythonie
- Bicep jako alternatywa - porownanie z Terraform
- Pipeline IaC w Azure DevOps: plan → review → apply → test → destroy

### Cwiczenia praktyczne
1. Napisz Terraform tworzacy resource group + storage account dla testow
2. Parametryzuj konfiguracje przez `variables.tf` (region, env name)
3. Dodaj output z connection stringiem i uzyj go w testach Pytest
4. Skonfiguruj pipeline DevOps: `tf apply` → testy → `tf destroy`
5. *(Trudniejsze)* Zbuduj modul Terraform tworzacy kompletne srodowisko testowe
   (APIM + Service Bus + Storage + App Insights)

### Narzedzia
- Terraform, `azurerm` provider, Azure DevOps, Pytest

---

## Projekt koncowy

**Nazwa:** QA Automation Framework dla aplikacji Azure-native

**Zakres:**
- Aplikacja: REST API + Service Bus consumer + Blob Storage writer
- Infrastruktura: provisioning przez Terraform (srodowisko testowe)
- Testy: integracyjne (Pytest), kontraktowe (Pact), wydajnosciowe (Locust)
- Pipeline: Azure DevOps (build → provision → test → report → destroy)
- Obserwowalnosc: weryfikacja logow w Application Insights po kazdem test run
- Dane testowe: factory + cleanup fixtures, dane w Azure Storage

**Kryteria zaliczenia:**
- Pipeline uruchamia sie automatycznie na PR
- Testy pokrywaja: happy path, bledy, brzegowe przypadki
- Infrastruktura jest tworzona i niszczona w ramach pipeline
- Raport wynikow widoczny w Azure DevOps Test Plans

---

## Materialy dodatkowe

| Zasob                                           | Link/Notatka                          |
|-------------------------------------------------|---------------------------------------|
| Azure SDK dla Pythona                           | docs.microsoft.com/python/api/azure   |
| AZ-900 (Azure Fundamentals) - egzamin           | certyfikat opcjonalny po module 01    |
| AZ-400 (DevOps Engineer) - egzamin              | certyfikat opcjonalny po module 02    |
| Pytest dokumentacja                             | docs.pytest.org                       |
| Great Expectations dokumentacja                 | greatexpectations.io/docs             |
| Terraform Azure Provider                        | registry.terraform.io/azurerm         |

---

## Wymagania wstepne

- Python 3.10+ (biegla znajomosc)
- Pytest - doswiadczenie w pisaniu fixture'ow i parametryzacji
- REST API - testowanie HTTP, znajomosc statusow i naglowkow
- Git - praca z branchami, pull requests
- Terminal (bash/zsh) - komfort w pracy z CLI
- Konto Azure (Free Tier wystarczy do modulu 07)
