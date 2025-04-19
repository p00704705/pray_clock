import sys
import time
import random
import socket
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont
from playsound import playsound
import threading
import pygame
from pydub import AudioSegment
from pydub.playback import  _play_with_simpleaudio
import fcntl
import struct
import os
os.environ["SDL_AUDIODRIVER"] = "alsa"
os.environ["AUDIODEV"] = "hw:1,0"
# List of messages
messages = [
    "Joshua 1:9 - 'Have I not commanded you? Be strong and courageous. Do not be afraid; do not be discouraged, for the LORD your God will be with you wherever you go.'",
    "Psalm 23:4 - 'Even though I walk through the darkest valley, I will fear no evil, for you are with me; your rod and your staff, they comfort me.'",
    "Psalm 34:18 - 'The LORD is close to the brokenhearted and saves those who are crushed in spirit.'",
    "Isaiah 41:10 - 'So do not fear, for I am with you; do not be dismayed, for I am your God. I will strengthen you and help you; I will uphold you with my righteous right hand.'",
    "Jeremiah 29:11 - 'For I know the plans I have for you,' declares the LORD, 'plans to prosper you and not to harm you, plans to give you hope and a future.'",
    "Matthew 11:28-30 - 'Come to me, all you who are weary and burdened, and I will give you rest. Take my yoke upon you and learn from me, for I am gentle and humble in heart, and you will find rest for your souls. For my yoke is easy and my burden is light.'",
    "John 14:27 - 'Peace I leave with you; my peace I give you. I do not give to you as the world gives. Do not let your hearts be troubled and do not be afraid.'",
    "Romans 8:28 - 'And we know that in all things God works for the good of those who love him, who have been called according to his purpose.'",
    "Romans 15:13 - 'May the God of hope fill you with all joy and peace as you trust in him, so that you may overflow with hope by the power of the Holy Spirit.'",
    "Philippians 4:6-7 - 'Do not be anxious about anything, but in every situation, by prayer and petition, with thanksgiving, present your requests to God. And the peace of God, which transcends all understanding, will guard your hearts and your minds in Christ Jesus.'",
    "Philippians 4:13 - 'I can do all this through him who gives me strength.'",
    "2 Timothy 1:7 - 'For the Spirit God gave us does not make us timid, but gives us power, love and self-discipline.'",
    "Hebrews 13:5-6 - 'God has said, “Never will I leave you; never will I forsake you.” So we say with confidence, “The Lord is my helper; I will not be afraid. What can mere mortals do to me?”'",
    "1 Peter 5:7 - 'Cast all your anxiety on him because he cares for you.'",
    "Revelation 21:4 - 'He will wipe every tear from their eyes. There will be no more death or mourning or crying or pain, for the old order of things has passed away.'",
    "Deuteronomy 31:6 - 'Be strong and courageous. Do not be afraid or terrified because of them, for the LORD your God goes with you; he will never leave you nor forsake you.'",
    "Proverbs 3:5-6 - 'Trust in the LORD with all your heart and lean not on your own understanding; in all your ways submit to him, and he will make your paths straight.'",
    "Psalm 55:22 - 'Cast your cares on the LORD and he will sustain you; he will never let the righteous be shaken.'",
    "Isaiah 40:31 - 'But those who hope in the LORD will renew their strength. They will soar on wings like eagles; they will run and not grow weary, they will walk and not be faint.'",
    "Psalm 46:1 - 'God is our refuge and strength, an ever-present help in trouble.'",
    "Romans 8:38-39 - 'For I am convinced that neither death nor life, neither angels nor demons, neither the present nor the future, nor any powers, neither height nor depth, nor anything else in all creation, will be able to separate us from the love of God that is in Christ Jesus our Lord.'",
    "2 Corinthians 12:9-10 - 'But he said to me, “My grace is sufficient for you, for my power is made perfect in weakness.” Therefore I will boast all the more gladly about my weaknesses, so that Christ’s power may rest on me.'",
    "Psalm 91:4 - 'He will cover you with his feathers, and under his wings you will find refuge; his faithfulness will be your shield and rampart.'",
    "Psalm 91:11 - 'For he will command his angels concerning you to guard you in all your ways.'",
    "Lamentations 3:22-23 - 'Because of the LORD’s great love we are not consumed, for his compassions never fail. They are new every morning; great is your faithfulness.'",
    "1 Thessalonians 5:11 - 'Therefore encourage one another and build each other up, just as in fact you are doing.'",
    "Colossians 3:15 - 'Let the peace of Christ rule in your hearts, since as members of one body you were called to peace. And be thankful.'",
    "Psalm 121:1-2 - 'I lift up my eyes to the mountains—where does my help come from? My help comes from the LORD, the Maker of heaven and earth.'",
    "Matthew 6:33 - 'But seek first his kingdom and his righteousness, and all these things will be given to you as well.'",
    "Hebrews 11:1 - 'Now faith is confidence in what we hope for and assurance about what we do not see.'",
    "John 16:33 - 'I have told you these things, so that in me you may have peace. In this world you will have trouble. But take heart! I have overcome the world.'",
    "Isaiah 43:2 - 'When you pass through the waters, I will be with you; and when you pass through the rivers, they will not sweep over you. When you walk through the fire, you will not be burned; the flames will not set you ablaze.'",
    "Zephaniah 3:17 - 'The LORD your God is with you, the Mighty Warrior who saves. He will take great delight in you; in his love he will no longer rebuke you, but will rejoice over you with singing.'",
    "Galatians 6:9 - 'Let us not become weary in doing good, for at the proper time we will reap a harvest if we do not give up.'",
    "Isaiah 26:3 - 'You will keep in perfect peace those whose minds are steadfast, because they trust in you.'",
    "1 John 4:18 - 'There is no fear in love. But perfect love drives out fear, because fear has to do with punishment. The one who fears is not made perfect in love.'",
    "Matthew 5:16 - 'In the same way, let your light shine before others, that they may see your good deeds and glorify your Father in heaven.'",
    "Psalm 37:4 - 'Take delight in the LORD, and he will give you the desires of your heart.'",
    "Micah 6:8 - 'He has shown you, O mortal, what is good. And what does the LORD require of you? To act justly and to love mercy and to walk humbly with your God.'",
    "1 Corinthians 15:58 - 'Therefore, my dear brothers and sisters, stand firm. Let nothing move you. Always give yourselves fully to the work of the Lord, because you know that your labor in the Lord is not in vain.'",
    "Romans 12:12 - 'Be joyful in hope, patient in affliction, faithful in prayer.'",
    "James 1:12 - 'Blessed is the one who perseveres under trial because, having stood the test, that person will receive the crown of life that the Lord has promised to those who love him.'",
    "Psalm 139:14 - 'I praise you because I am fearfully and wonderfully made; your works are wonderful, I know that full well.'",
    "1 Corinthians 16:13 - 'Be on your guard; stand firm in the faith; be courageous; be strong.'",
    "Psalm 27:1 - 'The LORD is my light and my salvation—whom shall I fear? The LORD is the stronghold of my life—of whom shall I be afraid?'",
    "2 Thessalonians 3:3 - 'But the Lord is faithful, and he will strengthen you and protect you from the evil one.'",
    "Nahum 1:7 - 'The LORD is good, a refuge in times of trouble. He cares for those who trust in him.'",
    "Matthew 19:26 - 'Jesus looked at them and said, “With man this is impossible, but with God all things are possible.”'",
    "Psalm 73:26 - 'My flesh and my heart may fail, but God is the strength of my heart and my portion forever.'",
    "James 5:16 - 'Therefore confess your sins to each other and pray for each other so that you may be healed. The prayer of a righteous person is powerful and effective.'",
    "Isaiah 55:9 - 'As the heavens are higher than the earth, so are my ways higher than your ways and my thoughts than your thoughts.'",
    "2 Corinthians 4:16-18 - 'Therefore we do not lose heart. Though outwardly we are wasting away, yet inwardly we are being renewed day by day. For our light and momentary troubles are achieving for us an eternal glory that far outweighs them all. So we fix our eyes not on what is seen, but on what is unseen, since what is seen is temporary, but what is unseen is eternal.'",
    "Psalm 100:4-5 - 'Enter his gates with thanksgiving and his courts with praise; give thanks to him and praise his name. For the LORD is good and his love endures forever; his faithfulness continues through all generations.'",
    "Ephesians 6:10 - 'Finally, be strong in the Lord and in his mighty power.'",
    "Proverbs 18:10 - 'The name of the LORD is a fortified tower; the righteous run to it and are safe.'",
    "Psalm 32:7 - 'You are my hiding place; you will protect me from trouble and surround me with songs of deliverance.'",
    "Isaiah 54:17 - 'No weapon forged against you will prevail, and you will refute every tongue that accuses you. This is the heritage of the servants of the LORD, and this is their vindication from me, declares the LORD.'",
    "1 John 5:14 - 'This is the confidence we have in approaching God: that if we ask anything according to his will, he hears us.'",
    "Psalm 30:5 - 'For his anger lasts only a moment, but his favor lasts a lifetime; weeping may stay for the night, but rejoicing comes in the morning.'",
    "1 Chronicles 16:11 - 'Look to the LORD and his strength; seek his face always.'",
    "Isaiah 40:29 - 'He gives strength to the weary and increases the power of the weak.'",
    "Psalm 56:3 - 'When I am afraid, I put my trust in you.'",
    "Hebrews 4:16 - 'Let us then approach God’s throne of grace with confidence, so that we may receive mercy and find grace to help us in our time of need.'",
    "Matthew 7:7 - 'Ask and it will be given to you; seek and you will find; knock and the door will be opened to you.'",
    "James 4:7 - 'Submit yourselves, then, to God. Resist the devil, and he will flee from you.'",
    "Isaiah 41:13 - 'For I am the LORD your God who takes hold of your right hand and says to you, Do not fear; I will help you.'",
    "1 Corinthians 10:13 - 'No temptation has overtaken you except what is common to mankind. And God is faithful; he will not let you be tempted beyond what you can bear. But when you are tempted, he will also provide a way out so that you can endure it.'",
    "Romans 8:31 - 'What, then, shall we say in response to these things? If God is for us, who can be against us?'",
    "Deuteronomy 33:27 - 'The eternal God is your refuge, and underneath are the everlasting arms. He will drive out your enemies before you, saying, Destroy them!'",
    "1 Peter 1:6-7 - 'In all this you greatly rejoice, though now for a little while you may have had to suffer grief in all kinds of trials. These have come so that the proven genuineness of your faith—of greater worth than gold, which perishes even though refined by fire—may result in praise, glory and honor when Jesus Christ is revealed.'",
    "Psalm 37:5 - 'Commit your way to the LORD; trust in him and he will do this.'",
    "John 15:5 - 'I am the vine; you are the branches. If you remain in me and I in you, you will bear much fruit; apart from me you can do nothing.'",
    "2 Corinthians 1:3-4 - 'Praise be to the God and Father of our Lord Jesus Christ, the Father of compassion and the God of all comfort, who comforts us in all our troubles, so that we can comfort those in any trouble with the comfort we ourselves receive from God.'",
    "Psalm 18:2 - 'The LORD is my rock, my fortress and my deliverer; my God is my rock, in whom I take refuge, my shield and the horn of my salvation, my stronghold.'",
    "Isaiah 46:4 - 'Even to your old age and gray hairs I am he, I am he who will sustain you. I have made you and I will carry you; I will sustain you and I will rescue you.'",
    "Colossians 3:23-24 - 'Whatever you do, work at it with all your heart, as working for the Lord, not for human masters, since you know that you will receive an inheritance from the Lord as a reward. It is the Lord Christ you are serving.'",
    "Psalm 28:7 - 'The LORD is my strength and my shield; my heart trusts in him, and he helps me. My heart leaps for joy, and with my song I praise him.'",
    "Psalm 9:9-10 - 'The LORD is a refuge for the oppressed, a stronghold in times of trouble. Those who know your name trust in you, for you, LORD, have never forsaken those who seek you.'",
    "Hebrews 12:1 - 'Therefore, since we are surrounded by such a great cloud of witnesses, let us throw off everything that hinders and the sin that so easily entangles. And let us run with perseverance the race marked out for us.'",
    "2 Timothy 4:7 - 'I have fought the good fight, I have finished the race, I have kept the faith.'",
    "Jeremiah 31:3 - 'The LORD appeared to us in the past, saying: I have loved you with an everlasting love; I have drawn you with unfailing kindness.'",
    "Psalm 29:11 - 'The LORD gives strength to his people; the LORD blesses his people with peace.'",
    "John 11:25-26 - 'Jesus said to her, “I am the resurrection and the life. The one who believes in me will live, even though they die; and whoever lives by believing in me will never die. Do you believe this?”'",
    "Philippians 1:6 - 'Being confident of this, that he who began a good work in you will carry it on to completion until the day of Christ Jesus.'",
    "1 Thessalonians 3:13 - 'May he strengthen your hearts so that you will be blameless and holy in the presence of our God and Father when our Lord Jesus comes with all his holy ones.'"
]
def get_device_ip(interface="wlan0"):
    """Get the IP address of the specific network interface."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ip_address = fcntl.ioctl(
            sock.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', interface[:15].encode('utf-8'))
        )[20:24]
        return socket.inet_ntoa(ip_address)
    except Exception as e:
        return f"IP: Not available ({str(e)})"

# Path to the sound file
sound_file_path = "/home/pi/pray/24ctu.mp3"  # Update this path

# Prayer times in 24-hour format
prayer_times = ["09:00", "12:00", "15:00", "18:00", "21:00"]

class PrayerReminder(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.current_message = random.choice(messages)
        self.device_ip = get_device_ip()
        self.next_prayer_time = self.get_next_prayer_time()
        self.update_message()

    def initUI(self):
        self.setWindowTitle('Prayer Reminder')
        self.showFullScreen()
        self.setStyleSheet("background-color: black;")

        # Layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # IP Address Label
        self.ip_label = QLabel()
        self.ip_label.setFont(QFont('Arial', 20))
        self.ip_label.setStyleSheet("color: yellow;")
        layout.addWidget(self.ip_label)

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

        # Timer to update message every 5 minutes
        self.message_timer = QTimer(self)
        self.message_timer.timeout.connect(self.update_message)
        self.message_timer.start(1 * 60 * 1000)  # 5 minutes interval

    def update_time(self):
        current_time = datetime.now().strftime('%H:%M:%S')
        self.time_label.setText(current_time)
        self.ip_label.setText(f"Device IP: {self.device_ip}")

    def update_message(self):
        self.current_message = random.choice(messages)
        self.message_label.setText(self.current_message)
        current_time = datetime.now().strftime('%H:%M')
        print(current_time)
        print(type(current_time))
        if current_time in prayer_times:
            sound = AudioSegment.from_mp3("/home/pi/pray/24ctu.mp3")
            _play_with_simpleaudio(sound)

    def close_application(self):
        """Close the application when the button is clicked."""
        self.close()

    def get_next_prayer_time(self):
        now = datetime.now()
        for prayer_time in prayer_times:
            prayer_datetime = datetime.strptime(prayer_time, '%H:%M').replace(year=now.year, month=now.month, day=now.day)
            if prayer_datetime > now:
                return prayer_datetime
        # If no future prayer time today, set to the first prayer time tomorrow
        next_day = now.replace(day=now.day + 1, hour=0, minute=0, second=0, microsecond=0)
        return datetime.strptime(prayer_times[0], '%H:%M').replace(year=next_day.year, month=next_day.month, day=next_day.day)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PrayerReminder()
    ex.show()
    sys.exit(app.exec_())
