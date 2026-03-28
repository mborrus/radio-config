# radio-config

MPD configuration for the radio (Raspberry Pi + PCM5102 DAC).

## Stations

| # | Name         | URL |
|---|--------------|-----|
| 1 | WNYU         | https://www.wnyu-ice-cast-relay.com/wnyu.mp3 |
| 2 | WCFM 91.9    | http://wcfm-streaming.williams.edu:8000/stream |
| 3 | WKCR         | http://wkcr.streamguys1.com/live |
| 4 | Folk Alley   | http://freshgrass.streamguys1.com/folkalley-128mp3 |
| 5 | Folk Forward | https://ice5.somafm.com/folkfwd-128-mp3 |

## Files

- `mpd.conf` — MPD config (lives at `/etc/mpd.conf`)
- `asound.conf` — ALSA softvol config (lives at `/etc/asound.conf`)
- `playlists/` — MPD playlists (live at `/var/lib/mpd/playlists/`)

## Usage

Switch stations:

```bash
mpc play 1   # WNYU
mpc play 4   # Folk Alley
```

Set volume (software, physical knob still works on top):

```bash
mpc volume 50
```

## Syncing changes

After editing the live config, copy files here and commit:

```bash
cp /etc/mpd.conf ~/radio-config/
cp /etc/asound.conf ~/radio-config/
cp /var/lib/mpd/playlists/*.m3u ~/radio-config/playlists/
cd ~/radio-config && git add -A && git commit -m "describe your change"
```

To deploy from this repo back to the system:

```bash
sudo cp ~/radio-config/mpd.conf /etc/mpd.conf
sudo cp ~/radio-config/asound.conf /etc/asound.conf
cp ~/radio-config/playlists/*.m3u /var/lib/mpd/playlists/
sudo systemctl restart mpd
```
