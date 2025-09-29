from __future__ import annotations
from .utils.logging import setup_logger
from .utils.files import read_json
from .utils.http import post, bearer

log = setup_logger("morpheus_import")

def do_import(m_host: str, token: str, payloads_path: str, apply: bool = True):
    data = read_json(payloads_path)
    headers = {"Content-Type": "application/json", **bearer(token)}
    for t in data.get("tenants", []):
        if apply:
            r = post(f"{m_host}/api/accounts", headers=headers, json=t)
            if r.status_code >= 300:
                log.error("Tenant create failed: %s %s", r.status_code, r.text[:200])
            else:
                log.info("Tenant upserted: %s", t["tenant"]["name"])
        else:
            log.info("[DRY RUN] Would create tenant: %s", t["tenant"]["name"])
