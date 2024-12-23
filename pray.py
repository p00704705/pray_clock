import os
import sys
import time
import random
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont
import pygame

# Set environment variables for audio playback
os.environ["SDL_AUDIODRIVER"] = "alsa"
os.environ["AUDIODEV"] = "hw:1,0"  # Update to the correct audio device (e.g., hw:1,0 for USB Audio Device)

# List of verses/messages
messages = [
    "Joshua 1:9 - 'Be strong and courageous. Do not be afraid; do not be discouraged, for the LORD your God will be with you wherever you go.'",
    "Psalm 23:4 - 'Even though I walk through the darkest valley, I will fear no evil, for you are with me; your rod and your staff, they comfort me.'",
    "Philippians 4:13 - 'I can do all this through him who gives me strength.'",
    # Add more messages as needed
]

# Path to the sound file
sound_file_path = "/home/pi/pray/15s.mp3"  # Update this path

# Prayer times in 24-hour format
prayer_times = ["09:00", "12:00", "15:00", "18:00", "21:00"]

class PrayerReminder(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.current_message = random.choice(messages)
        self.next_prayer_time = self.get_next_prayer_time()
        self.update_message()

    def initUI(self):
        self.setWindowTitle('Prayer Reminder')
        self.showFullScreen()
        self.setStyleSheet("background-color: black;")

        # Layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # Time Label
        self.time_label = QLabel()
        self.time_label.setFont(QFont('Arial', 30))
        self.time_label.setStyleSheet("color: white;")
        layout.addWidget(self.time_label)

        # Message Label
        self.message_label = QLabel()
        self.message_label.setFont(QFont('Arial', 30))
        self.message_label.setStyleSheet("color: white;")
        self.message_label.setWordWrap(True)  # Enable word wrapping
        layout.addWidget(self.message_label)

        # Close Button
        self.close_button = QPushButton("Close")
        self.close_button.setFont(QFont('Arial', 20))
        self.close_button.setStyleSheet("color: white; background-color: red;")
        self.close_button.clicked.connect(self.close_application)
        layout.addWidget(self.close_button)

        self.setLayout(layout)

        # Timer to update time every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # 1 second interval

        # Timer to update verse every 5 minutes
        self.message_timer = QTimer(self)
        self.message_timer.timeout.connect(self.update_message)
        self.message_timer.start(5 * 60 * 1000)  # 5 minutes interval

    def update_time(self):
        current_time = datetime.now().strftime('%H:%M:%S')
        self.time_label.setText(current_time)

        # Check if it's time for prayer
        if datetime.now() >= self.next_prayer_time:
            self.play_audio()
            self.next_prayer_time = self.get_next_prayer_time()

    def update_message(self):
        self.current_message = random.choice(messages)
        self.message_label.setText(self.current_message)

    def get_next_prayer_time(self):
        now = datetime.now()
        for prayer_time in prayer_times:
            prayer_datetime = datetime.strptime(prayer_time, '%H:%M').replace(
                year=now.year, month=now.month, day=now.day)
            if prayer_datetime > now:
                return prayer_datetime
        # If no future prayer time today, set to the first prayer time tomorrow
        next_day = now.replace(day=now.day + 1, hour=0, minute=0, second=0, microsecond=0)
        return datetime.strptime(prayer_times[0], '%H:%M').replace(
            year=next_day.year, month=next_day.month, day=next_day.day)

    def play_audio(self):
        """Play the reminder sound."""
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file_path)
            pygame.mixer.music.play()
        except Exception as e:
            print(f"Error playing sound: {e}")

    def close_application(self):
        """Close the application when the button is clicked."""
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PrayerReminder()
    ex.show()
    sys.exit(app.exec_())
