from pathlib import Path
import hashlib, io, zipfile
root=Path(__file__).resolve().parent
parts=[root/f"pom-space-source.zip.part{i:02}" for i in range(1,5)]
data=b"".join(p.read_bytes() for p in parts)
if hashlib.sha256(data).hexdigest() != "57828bc23e0e8d16bd175d9899254167d108a79b9233249e2b923f727b03550f":
    raise SystemExit("Archive mismatch: download all four parts from the same revision.")
with zipfile.ZipFile(io.BytesIO(data)) as z:
    for name in z.namelist():
        target=(root/name).resolve()
        if not target.is_relative_to(root): raise SystemExit("Unsafe archive path")
    z.extractall(root)
print("Verified and extracted pom-space. Read pom-space/README.md before setup.")
