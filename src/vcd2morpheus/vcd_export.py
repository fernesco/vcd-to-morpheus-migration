from __future__ import annotations
import os
from .utils.logging import setup_logger
from .utils.files import write_json
import requests

log = setup_logger("vcd_export")

def export_all(vcd_host: str, user: str, password: str, api_version: str, out_path: str):
    """Export minimal taxonomy from VCD. Extend to collect VDCs, catalogs, edges, networks, vApps."""
    sess = requests.Session()
    sess.verify = os.getenv("VERIFY_SSL","true").lower() == "true"
    sess.auth = (user, password)
    headers = {"Accept": f"application/*+xml;version={api_version}"}

    orgs_resp = sess.get(f"{vcd_host}/api/org", headers=headers, timeout=60)
    if orgs_resp.status_code >= 400:
        log.error("Failed to fetch orgs: %s %s", orgs_resp.status_code, orgs_resp.text[:200])
        raise SystemExit(1)

    payload = {
        "meta": {"source": "VCD", "host": vcd_host},
        "orgs_xml": orgs_resp.text
    }
    write_json(out_path, payload)
    log.info("Export written to %s", out_path)
