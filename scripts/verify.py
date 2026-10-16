"""Verify package identity and source integrity before publishing."""
from pathlib import Path
import hashlib
import re
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
source = (root / "content/SamsungSmartTV.qplug").read_bytes()
assert hashlib.sha256(source).hexdigest() == "be02405496d2d00b3dcd284e8709c4368ccde7c4b55569193653592f62f23ec3", "Update the reviewed source digest for an intentional plugin revision"
info = re.search(r"PluginInfo\s*=\s*\{(.*?)\}", source.decode("utf-8-sig"), re.S)[1]
version = re.search(r'\bVersion\s*=\s*"([^"]+)"', info)[1]
project = ET.parse(root / "SamsungSmartTV.csproj").getroot()
assert version == project.findtext("PropertyGroup/Version"), "Plugin/package version mismatch"
assert project.findtext("PropertyGroup/PackageId") == "JoshuaSmall.Qsys.SamsungSmartTV"
assert (root / "icon.png").read_bytes().startswith(b"\x89PNG\r\n\x1a\n")
assert "https://joshua-small.github.io/qsys-samsung-smart-tv/registration/joshuasmall.qsys.samsungsmarttv/index.json" in (root / "README.md").read_text()
print("Verified", "SamsungSmartTV.qplug", version, hashlib.sha256(source).hexdigest())
