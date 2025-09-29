# HOWTO: Run the VCD → Morpheus Migration

## 1) Prepare environment
- Python 3.9+
- `pip install -r requirements.txt`
- Copy `.env.example` to `.env` and fill in credentials.

## 2) Export from VCD
- Exports orgs, vdcs, networks, edges, catalogs, vapps into a single JSON.
- Uses VCD API `Accept: application/*+xml;version={api_version}` under the hood.

## 3) Transform
- Applies mapping rules (org→tenant, vdc→resource-pool, catalog→blueprint).
- Produces idempotent Morpheus payloads.

## 4) Import to Morpheus
- Creates/updates Tenants, Library Items (Blueprints), Networks.
- Safe by default; set `--apply` to perform changes.
