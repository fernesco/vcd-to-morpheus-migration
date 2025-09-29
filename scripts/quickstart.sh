#!/usr/bin/env bash
set -euo pipefail
python -m vcd2morpheus.cli --config config/config.yaml export --out ./out/vcd_export.json
python -m vcd2morpheus.cli --config config/config.yaml transform --in ./out/vcd_export.json --out ./out/morpheus_payloads.json
python -m vcd2morpheus.cli --config config/config.yaml import --in ./out/morpheus_payloads.json --apply
