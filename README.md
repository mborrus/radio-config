# radio-config

An internet radio built on a Raspberry Pi with a PCM5102 DAC over I2S. Streams stations via MPD, with a physical button (GPIO 23) to skip between stations and a volume knob for analog control. Software volume in MPD tames the baseline level before it hits the DAC.

## Stations

| # | Name         | URL |
|---|--------------|-----|
| 1 | WNYU         | https://www.wnyu-ice-cast-relay.com/wnyu.mp3 |
| 2 | WCFM 91.9    | http://wcfm-streaming.williams.edu:8000/stream |
| 3 | WKCR         | http://wkcr.streamguys1.com/live |
| 4 | Folk Alley   | http://freshgrass.streamguys1.com/folkalley-128mp3 |
| 5 | Folk Forward | https://ice5.somafm.com/folkfwd-128-mp3 |

## Syncing changes

After editing the live config, copy files here and commit:

```bash
~/radio-config/sync.sh "describe your change"
```

To deploy from this repo back to the system:

```bash
sudo cp ~/radio-config/mpd.conf /etc/mpd.conf
sudo cp ~/radio-config/asound.conf /etc/asound.conf
cp ~/radio-config/playlists/*.m3u /var/lib/mpd/playlists/
sudo cp ~/radio-config/boot-config.txt /boot/firmware/config.txt
sudo cp ~/radio-config/rc.local /etc/rc.local
sudo cp ~/radio-config/radio_button.py ~/radio_button.py
sudo systemctl restart mpd
```
