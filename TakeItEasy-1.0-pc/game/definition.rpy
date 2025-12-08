#MUSIC
#ALL MUSIC IS ORIGINAL
define opening = "audio/music/overworkd.ogg"
define audio.home = "audio/music/homesweethome.ogg"
define audio.cafe = "audio/music/coffeebreak.ogg"
define audio.sad = "audio/music/areyouproud.ogg"
define audio.looking = "audio/music/getbusy.ogg"


#SFX
#ALL SOUNDS COURTESY OF PIXABAY
define sound.park = "audio/sounds/park.mp3"
define sound.office = "audio/sounds/office.mp3"
define bleh = "audio/sounds/ticktock.mp3"
define sound.night = "audio/sounds/night.mp3"
define sound.audience = "audio/sounds/audience.mp3"
define sound.feet = "audio/sounds/footsteps.mp3"


#FONT
define font = "DejaVuSans.ttf"


#IMAGEBUTTONS


#CHARACTERS
define tk = Character("Tobias", image="tobias", who_color="#310707")
image tobias base = "side tobias base.webp"
image tobias blush = "side tobias blush.webp"
image tobias happy = "side tobias happy.webp"
image tobias home = "side tobias home.webp"
image tobias pensive = "side tobias pensive.webp"
image tobias relaxed = "side tobias relaxed.webp"
image tobias sad = "side tobias sad.webp"
image tobias serious = "side tobias serious.webp"
image tobias smiley = "side tobias smiley.webp"
define anon = Character("???", who_color = "#000000")
define dog = Character("Lilith", who_color = "#000000")
define tv = Character("Television", who_color = "#000000")
define nt = Character("Naoya", who_color = "#17021f")
define js = Character("Julia", who_color = "#2e6139")
define lv = Character("Leonel", who_color = "#8f751f")
define ke = Character("Klarika", who_color = "#3c2945")
define rr = Character("Romeo", who_color = "#292620")
define ei = Character("Evie", who_color="#923776")
define tp = Character("Theo", who_color = "#2b2a31")
define guy = Character("Auctioneer", who_color = "#000000")
define yall = Character("Attendee", who_color = "#000000")


#CHOICES + COUNTERS
default good_end_counters = 0
default usual_choice = False
default interrogate1 = False
default interrogate2 = False
default interrogate3 = False
default question1 = False
default question2 = False
default question3 = False
default check_window = False
default check_box = False
default check_vanity = False
define q1 = False
define q2 = False
default earlyBird = False
default onTime = False

#TRANSFORMATIONS
transform slightleft:
    xalign 0.25
    yalign 1.0
transform slightright:
    xalign 0.75
    yalign 1.0
transform centerpos:
    xalign 0.5
    yalign 1.0


#FILE AND JOURNAL MECHANICS DEFINITIONS
default dfileread1 = False
default dfileread2 = False
default dfileread3 = False
default kfileread1 = False
default kfileread2 = False
default kfileread3 = False
default vfileread1 = False
default vfileread2 = False
default vfileread3 = False
default photo1 = False
default photo2 = False
default evidence1 = False
default evidence2 = False