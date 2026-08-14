#!/usr/bin/env python3
"""Génère le sprite SVG inline des icônes selfh.st pour la landing SPUTNK."""
import re, os

ICONS_DIR = '/tmp/sputnk-landing/icons'
OUT = '/tmp/sputnk-landing/sprite.svg'

# slug selfh.st -> id symbol
MAP = {
    'proxmox': 'proxmox',
    'pikvm': 'nanokvm',
    'arcane': 'arcane',
    'uptime-kuma': 'status',
    'authentik': 'sso',
    'vaultwarden': 'bitwarden',
    'wizarr': 'wizarr',
    'jellyfin': 'jellyfin',
    'jellyseerr': 'seerr',
    'sonarr': 'sonarr',
    'radarr': 'radarr',
    'prowlarr': 'prowlarr',
    'qbittorrent': 'qbit',
    'immich': 'pics',
    'nextcloud': 'cloud',
    'stirling-pdf': 'pdf',
    'ntfy': 'ntfy',
    'open-webui': 'llm',
}

syms = []
for slug, sid in MAP.items():
    p = os.path.join(ICONS_DIR, slug + '.svg')
    with open(p) as f:
        svg = f.read()
    # extraire le viewBox du root
    m = re.search(r'viewBox="([^"]+)"', svg)
    vb = m.group(1) if m else '0 0 512 512'
    # retirer les balises root, garder le contenu
    inner = re.sub(r'<svg[^>]*>', '', svg, count=1)
    inner = re.sub(r'</svg>', '', inner, count=1)
    inner = re.sub(r'\n\s*', ' ', inner).strip()
    syms.append(f'<symbol id="i-{sid}" viewBox="{vb}">{inner}</symbol>')

sprite = ('<svg xmlns="http://www.w3.org/2000/svg" style="display:none" aria-hidden="true">'
          + ''.join(syms) + '</svg>')
with open(OUT, 'w') as f:
    f.write(sprite)
print(f'sprite écrit: {OUT} — {len(sprite)} octets — {len(syms)} symboles')
