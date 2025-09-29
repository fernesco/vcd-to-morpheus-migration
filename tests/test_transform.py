from src.vcd2morpheus.transform_map import transform
from pathlib import Path
import json, tempfile

def test_transform_tmp():
    tmp = tempfile.TemporaryDirectory()
    input_path = Path(tmp.name) / "in.json"
    out_path = Path(tmp.name) / "out.json"
    input_path.write_text(json.dumps({"meta": {"source": "VCD"}}))
    transform(str(input_path), str(out_path))
    assert out_path.exists()
    data = json.loads(out_path.read_text())
    assert "tenants" in data
