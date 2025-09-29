import json, pathlib, typing as t

def write_json(path: str, data: t.Any) -> None:
    p = pathlib.Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, indent=2))

def read_json(path: str) -> t.Any:
    return json.loads(pathlib.Path(path).read_text())
