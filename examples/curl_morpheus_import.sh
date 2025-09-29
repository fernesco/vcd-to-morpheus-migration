#!/usr/bin/env bash
set -euo pipefail

MORPHEUS="${MORPHEUS_HOST:-https://morpheus.example.com}"
TOKEN="${MORPHEUS_TOKEN:-xxxxx}"

curl -sS -H "Authorization: BEARER $TOKEN" -H "Content-Type: application/json"  -X POST "$MORPHEUS/api/accounts" -d '{"tenant":{"name":"Example","code":"EX"}}'
