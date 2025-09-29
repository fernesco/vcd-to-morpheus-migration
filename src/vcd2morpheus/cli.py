from __future__ import annotations
import argparse, os, yaml
from dotenv import load_dotenv
from .vcd_export import export_all
from .transform_map import transform
from .morpheus_import import do_import
from .utils.logging import setup_logger

log = setup_logger("cli")

def load_cfg(path: str) -> dict:
    load_dotenv(override=True)
    with open(path) as f:
        text = os.path.expandvars(f.read())
    return yaml.safe_load(text)

def main():
    ap = argparse.ArgumentParser(prog="vcd2morpheus")
    ap.add_argument("--config", required=True, help="Path to config.yaml")
    sub = ap.add_subparsers(dest="cmd")

    ap_export = sub.add_parser("export")
    ap_export.add_argument("--out", required=True, help="Output JSON path")

    ap_transform = sub.add_parser("transform")
    ap_transform.add_argument("--in", required=True, dest="inp")
    ap_transform.add_argument("--out", required=True, dest="outp")
    ap_transform.add_argument("--overrides", default="config/mapping_overrides.yaml")
    ap_transform.add_argument("--dry-run", action="store_true")

    ap_import = sub.add_parser("import")
    ap_import.add_argument("--in", required=True, dest="inp")
    ap_import.add_argument("--apply", action="store_true")

    args = ap.parse_args()
    cfg = load_cfg(args.config)
    vcd = cfg["vcd"]; morp = cfg["morpheus"]

    if args.cmd == "export":
        export_all(vcd["host"], vcd["user"], vcd["password"], vcd["api_version"], args.out)
    elif args.cmd == "transform":
        transform(args.inp, args.outp)
    elif args.cmd == "import":
        do_import(morp["host"], morp["token"], args.inp, apply=args.apply)
    else:
        ap.print_help()

if __name__ == "__main__":
    main()
