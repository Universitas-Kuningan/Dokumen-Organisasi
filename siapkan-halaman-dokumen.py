from pathlib import Path

# Jalankan dari folder utama repo. Script ini menambahkan front matter Jekyll
# ke setiap file Markdown agar GitHub Pages mengubahnya menjadi halaman HTML.
root = Path.cwd()
count = 0
for path in root.rglob("*.md"):
    if any(part.startswith(".") or part.startswith("_") for part in path.relative_to(root).parts):
        continue
    text = path.read_text(encoding="utf-8")
    if text.startswith("---\n") or text.startswith("---\r\n"):
        continue
    path.write_text("---\nlayout: document\n---\n\n" + text, encoding="utf-8")
    count += 1
print(f"Selesai: {count} file Markdown disiapkan untuk GitHub Pages.")
