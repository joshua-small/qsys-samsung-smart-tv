"""Verify reviewed source bytes and product/release identity before packaging."""
import argparse
import hashlib
from pathlib import Path
from package_checks import check_identity

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--release-tag", help="Exact release tag; must equal v + source and project version")
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
source = (root / "content/SamsungSmartTV.qplug").read_bytes()
if hashlib.sha256(source).hexdigest() != "b3b5c36d46360a0a191e5e7bdce3ef9dea370c1ee6ae4dc4ef0e3ee71d9756e9":
    raise SystemExit("Update the reviewed source digest for an intentional plugin revision")
try:
    version = check_identity(source.decode("utf-8-sig"), (root / "SamsungSmartTV.csproj").read_text(),
        "JoshuaSmall.Qsys.SamsungSmartTV", args.release_tag)
except ValueError as error:
    raise SystemExit(str(error)) from error
if not (root / "icon.png").read_bytes().startswith(b"\x89PNG\r\n\x1a\n"):
    raise SystemExit("Invalid package icon")
if "https://joshua-small.github.io/qsys-samsung-smart-tv/registration/joshuasmall.qsys.samsungsmarttv/index.json" not in (root / "README.md").read_text():
    raise SystemExit("README Library feed does not match package identity")
print("Verified", "SamsungSmartTV.qplug", version, hashlib.sha256(source).hexdigest())
