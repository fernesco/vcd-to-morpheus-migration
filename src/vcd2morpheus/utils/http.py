from __future__ import annotations
import os, requests
from typing import Dict, Any
from tenacity import retry, stop_after_attempt, wait_exponential

VERIFY = os.getenv("VERIFY_SSL", "true").lower() == "true"

def bearer(token: str) -> Dict[str,str]:
    return {"Authorization": f"BEARER {token}"}

@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=1, max=10))
def get(url: str, headers: Dict[str,str]=None, params: Dict[str,Any]=None) -> requests.Response:
    return requests.get(url, headers=headers, params=params, verify=VERIFY, timeout=60)

@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=1, max=10))
def post(url: str, headers: Dict[str,str]=None, json: Any=None) -> requests.Response:
    return requests.post(url, headers=headers, json=json, verify=VERIFY, timeout=60)
