# VCD → Morpheus Migration Toolkit

**Version:** v1.0 • **Date:** 2025-09-29

This repository contains reference automation to **migrate VMware Cloud Director (VCD) constructs** into the **HPE Morpheus Enterprise** taxonomy.

> ⚠️ This is a community reference. Test in non‑production first.

## What it does

- **Export** VCD taxonomy (Orgs, Org VDCs, Networks, Edge Gateways, Catalogs, vApps).
- **Transform** exports into Morpheus‑ready payloads (Tenants, Resource Pool mappings, Network Profiles, Blueprints).
- **Import** into Morpheus via API (create/update **Tenants**, **Groups/Clouds**, **Library Items/Blueprints**).

## High‑level mapping

| VCD                       | Morpheus                                   |
|--------------------------|--------------------------------------------|
| Org                      | Tenant                                     |
| Org VDC                  | Resource Pool (in registered vCenter)      |
| Edge Gateway             | NSX‑T Tier‑1 (as Network Profile)          |
| Network / Segment        | Network/Subnet in Network Profile          |
| Catalog (OVA/ISO/script) | Library Item / Blueprint                    |
| vApp                     | App Blueprint (multi‑VM)                   |

## Repo layout

```
vcd-to-morpheus-migration/
 ├─ src/vcd2morpheus/
 │   ├─ vcd_export.py          # VCD API export
 │   ├─ transform_map.py       # Mapping + validation
 │   ├─ morpheus_import.py     # Morpheus API import
 │   ├─ cli.py                 # Simple CLI wrapper
 │   └─ utils/
 │       ├─ http.py            # requests helpers & retry
 │       ├─ files.py           # IO helpers
 │       └─ logging.py         # structured logs
 ├─ config/
 │   ├─ config.yaml            # endpoints, auth, defaults
 │   └─ mapping_overrides.yaml # per‑CSP mapping tweaks
 ├─ examples/
 │   ├─ curl_vcd_export.sh     # raw VCD curl exports
 │   ├─ curl_morpheus_import.sh# raw Morpheus curl
 │   └─ sample_outputs/        # example JSON exports
 ├─ scripts/
 │   └─ quickstart.sh          # end‑to‑end run helper
 ├─ docs/
 │   ├─ HOWTO.md               # runbook
 │   └─ API_NOTES.md           # endpoint notes
 ├─ tests/
 │   └─ test_transform.py
 ├─ requirements.txt
 ├─ README.md
 ├─ LICENSE
 └─ .github/workflows/ci.yml
```

## Quickstart

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Set environment
cp .env.example .env
# edit .env with VCD and Morpheus credentials

# Dry‑run (export + transform only)
python -m vcd2morpheus.cli --config config/config.yaml export --out ./out/vcd_export.json && python -m vcd2morpheus.cli --config config/config.yaml transform --in ./out/vcd_export.json --out ./out/morpheus_payloads.json --dry-run

# Execute import (creates tenants/blueprints; idempotent)
python -m vcd2morpheus.cli --config config/config.yaml import --in ./out/morpheus_payloads.json --apply
```

## Security

- Supports **.env** secrets, no secrets in code.
- Optional **MFA/API token** use recommended.

## License

MIT
