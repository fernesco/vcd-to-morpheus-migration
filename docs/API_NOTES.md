# API Notes

## VMware Cloud Director (VCD)
- Auth: Basic + session or bearer
- Key endpoints (example):
  - `GET /api/org` — list orgs
  - `GET /api/org/{orgId}/vdcs` — org vDCs
  - `GET /api/admin/edgeGateway/{id}` — edge details
  - `GET /api/catalog` — catalogs

## HPE Morpheus
- Auth: `Authorization: BEARER <token>`
- Key endpoints (subset):
  - `POST /api/accounts` — create tenant
  - `GET /api/accounts` — list tenants
  - `POST /api/library/blueprints` — create blueprint
  - `POST /api/networks/profiles` — create network profile
  - `POST /api/zones` — register clouds (vCenter/HVM/etc.)
