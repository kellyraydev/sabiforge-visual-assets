# SabiForge Digital — visual asset library

Independent pictures for the existing SabiForge Digital site. This project does not contain the homepage, navigation, pricing, or contact system.

Batch 1 is ready for review:

| Asset | Master | Use |
| --- | --- | --- |
| Desktop hero devices | `library/masters/hero-desktop.jpg` · 1280×720 | Homepage hero from 768px up |
| Mobile hero devices | `library/masters/hero-mobile.jpg` · 720×1280 | Homepage hero below 768px |
| Maison Vale Interiors | `library/masters/maison-vale-interiors.jpg` · 1152×864 | Fictional interiors concept |
| AURA Clothing | `library/masters/aura-clothing.jpg` · 1152×864 | Fictional clothing concept |

Delivery files (JPEG, WebP, AVIF) are in `library/web/`. Names, sizes, placement, and descriptions are in `ASSET-MANIFEST.json`.

## Review the pictures

```bash
npm install
npm run dev
```

The review board runs at `http://127.0.0.1:4721`.

Before that, link the delivery files into the review server:

```bash
mkdir -p review/public
ln -sfn ../../library/web review/public/studio
```

## Move approved files into the Astro site

Follow `docs/TRANSFER.md`. In short: copy `library/web/` to `public/studio/` in the existing site, then copy either the Astro or the React components from `integration/`.

Licensing notes are in `docs/LICENSING.md`.

This private repository is only the visual asset library. It does not contain the SabiForge website.

Batch 2 stays on hold until it is explicitly approved. The hero dashboards use illustrative naira amounts. They do not set SabiForge’s service-package prices.
