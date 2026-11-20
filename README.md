# Dokumen Organisasi KPSI — Universitas Kuningan

Pusat dokumen organisasi, kebijakan, dan peta proses bisnis Kantor Pusat Sistem
Informasi (KPSI) Universitas Kuningan.

Baca versi web: https://universitas-kuningan.github.io/Dokumen-Organisasi/

## Isi dokumen

### Pedoman

| Dokumen | Versi | Status |
|---|---|---|
| Pedoman Organisasi dan Tata Kerja KPSI | 1.0 (10 November 2026) | Rancangan untuk dibahas dan ditetapkan |

### Peta Proses Bisnis

| Dokumen | Versi | Status |
|---|---|---|
| Peta Proses Bisnis KPSI Level 0 | 1.0 | Rancangan untuk pembahasan dan penetapan |
| PB-01 Pengelolaan Permintaan dan Analisis Kebutuhan TI | 1.2 | Rancangan |
| PB-02 Pengembangan dan Integrasi Aplikasi | 1.3 | Draf |
| PB-03 Pengelolaan Infrastruktur Jaringan dan Server | 1.2 | Draf |
| PB-04 Pengelolaan Website Universitas dan Unit Kerja | 1.1 | Draf |
| PB-05 Pengelolaan Layanan E-Learning | 1.0 | Draf |
| PB-06 Penanganan Gangguan dan Insiden TI | 1.1 | Draf |
| PP-01 Pengelolaan Dokumentasi dan Informasi Teknis TI | 1.1 | Draf |

Semua dokumen di atas masih berstatus rancangan/draf dan belum ditetapkan.

## Struktur repositori

```text
.
├── index.html                  # Beranda situs dokumen
├── _config.yml                 # Konfigurasi Jekyll / GitHub Pages
├── _layouts/
│   └── document.html           # Tampilan halaman dokumen (termasuk Mermaid)
├── pedoman-organisasi/
│   └── Pedoman_Organisasi_dan_Tata_Kerja_KPSI.md
├── peta_proses_bisnis/
│   ├── 0_PETA-PROSES-BISNIS-KPSI.md
│   ├── utama/                  # PB-01 s.d. PB-06
│   └── pendukung/              # PP-01
└── siapkan-halaman-dokumen.py  # Menambahkan front matter Jekyll ke file Markdown
```

## Cara kerja situs

Dokumen ditulis dalam Markdown dan diterbitkan sebagai situs web melalui
GitHub Pages (Jekyll):

- Setiap file Markdown memakai layout `document` sehingga tampil sebagai
  halaman HTML.
- Diagram alur ditulis dengan Mermaid dan dirender di browser.
- `siapkan-halaman-dokumen.py` menambahkan front matter Jekyll
  (`layout: document`) ke file Markdown yang belum memilikinya. Jalankan dari
  folder utama repositori:

  ```bash
  python3 siapkan-halaman-dokumen.py
  ```

## Cara berkontribusi

1. Fork repositori ini.
2. Buat branch baru untuk perubahan Anda, misalnya `tambah-pp02`.
3. Ubah atau tambah dokumen, lalu commit.
4. Buka pull request ke repositori utama
   (`Universitas-Kuningan/Dokumen-Organisasi`, branch `main`) dan jelaskan
   perubahannya.
5. Perubahan dibahas dan digabungkan oleh pengelola repositori.

Penamaan versi mengikuti nama file, misalnya `PB02_KPSI_v1-3.md` berarti
PB-02 versi 1.3.
