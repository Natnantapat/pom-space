from pathlib import Path
import hashlib,zipfile,io
root=Path(__file__).resolve().parent
parts=sorted(root.glob("pom-space-source.zip.part*"))
data=b"".join(p.read_bytes() for p in parts)
assert hashlib.sha256(data).hexdigest()=="3c45a8caf2d6766704f80d6c454a27ae861a3b2ac563de96c67d2345b4fe975d", "Download all parts before extracting"
with zipfile.ZipFile(io.BytesIO(data)) as z:z.extractall(root)
print("Ready: open pom-space, then npm ci, npm run build, npm start")
