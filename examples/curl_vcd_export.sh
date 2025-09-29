#!/usr/bin/env bash
set -euo pipefail

VCD_HOST="${VCD_HOST:-https://vcd.example.com}"
AUTH="${VCD_AUTH:-user:pass}"
VER="${VCD_API_VERSION:-33.0}"

curl -k -u "$AUTH" -H "Accept: application/*+xml;version=$VER" "$VCD_HOST/api/org" -o orgs.xml
