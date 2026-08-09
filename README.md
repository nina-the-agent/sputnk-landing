# SPUTNK Landing

Landing page pour sputnk.net — hébergée dans le conteneur `docker` (CT 101, mirage), servie via Cloudflare Tunnel.

## Déploiement

La page est servie par un simple serveur statique. Structure :

```
index.html
```

## Services listés

- Jellyfin, Radarr, Sonarr, qBittorrent, Prowlarr, Jellyseerr, Photos, Nextcloud, SSO, Arcane (Docker)

## Infrastructure

- Hébergement : CT 101 (docker) — mirage, VLAN 40 SERVICE (10.0.40.125)
- Exposition : Cloudflare Tunnel SPUTNK_OPN_SENSE
- URLs : https://sputnk.net → landing · https://docker.sputnk.net → Arcane
