#!/bin/bash
# Sync live config to repo and push
cp /etc/mpd.conf ~/radio-config/
cp /etc/asound.conf ~/radio-config/
cp /var/lib/mpd/playlists/*.m3u ~/radio-config/playlists/

cd ~/radio-config
git add -A
if git diff --cached --quiet; then
    echo "No changes to commit."
else
    git commit -m "${1:-Update radio config}"
    git push
fi
