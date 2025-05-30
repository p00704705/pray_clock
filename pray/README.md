# Prayer Reminder App

This is a fullscreen prayer reminder application for Linux (e.g., Raspberry Pi). It displays a randomly selected Bible verse on the screen, updates every few minutes, and plays an audio notification at specific prayer times throughout the day.

## 📋 Features

- Fullscreen GUI with PyQt5
- Displays current time and device IP address
- Randomly displays a Bible verse from a predefined list
- Plays a custom sound at scheduled prayer times (e.g., 9 AM, 12 PM, etc.)
- Manual button to trigger the sound playback
- Designed to run at boot with optional autologin and screensaver disabled

## 🕒 Default Prayer Times

- 09:00
- 12:00
- 15:00
- 18:00
- 21:00

These can be changed in the `prayer_times` list in the Python script.

## 📦 Requirements

- Python 3
- PyQt5
- Pydub
- simpleaudio
- ffmpeg (for audio decoding)
- ALSA (sound system for Linux)
- Optional: `xauth`, `xserver`, and `DISPLAY=:0` environment variable for GUI over SSH

## 🛠 Installation

1. **Clone the repo** (or copy the script to your Pi):

   ```bash
   git clone https://github.com/yourusername/pray_clock.git
   cd pray_clock