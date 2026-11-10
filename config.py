"""VELOCITY ICELANDIC - language pack, brand and motion design constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
FPS = 30

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY ICELANDIC"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "ICELANDIC"
HANDLE = "@velocityicelandic"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {
    "code": "is",
    "name": "Icelandic",
    "native_name": "Íslenska",
    "history_key": "icelandic",
    "english_voice": "en-US-AvaNeural",
    "english_fallback_voice": "en-US-GuyNeural",
    "native_voice": "is-IS-GunnarNeural",
    "native_fallback_voice": "is-IS-GudrunNeural",
    "native_engine": "edge",
    "native_lang_code": "is",
    "english_rate": "-2%",
    "native_rate": "-6%",
    "english_pitch": "+0Hz",
    "native_pitch": "+0Hz",
    "native_label": "ÍSLENSKA",
    "translit_label": "SAY IT LIKE",
    "greeting": "Halló!",
    "encouragement": "Frábært!",
    "rtl": False,
    "char_tiles": False,
    "script_font": "",
}
# ==== LANGUAGE PACK END ====

AI_MODEL = os.getenv("AI_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 4.0
OUTRO_DURATION = 5.2
EN_CARD_IN = 0.55
GAP_EN_NATIVE = 0.5
NATIVE_CARD_LEAD = 0.35
GAP_BEFORE_REPEAT = 0.8
TAIL_HOLD = 1.4
MAX_REEL_DURATION = 88.0

# ---------------------------------------------------------------- palette

INK = "#3C3C3C"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#A560E8"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

PALETTE = [GREEN, BLUE, PURPLE, ORANGE, RED, YELLOW, TEAL, PINK]

# ---------------------------------------------------------------- categories
# (english, native, icon, accent)

# ==== CATEGORY TABLE START ====
CATEGORY_TABLE = [
    ("Greetings", "Kveðjur", "hand", "#1CB0F6"),
    ("Basic Phrases", "Grunnsetningar", "chat", "#58CC02"),
    ("Common Expressions", "Algengar Orðasambönd", "chat", "#1CB0F6"),
    ("Travel", "Ferðalög", "plane", "#1CB0F6"),
    ("Restaurant", "Veitingastaður", "fork", "#FF7A00"),
    ("Shopping", "Innkaup", "bag", "#E056A0"),
    ("Emergency", "Neyðarástand", "siren", "#FF4B4B"),
    ("Family Terms", "Fjölskylduorð", "heart", "#E056A0"),
    ("Numbers", "Tölur", "hash", "#A560E8"),
    ("Time", "Tími", "clock", "#00A889"),
    ("Motivation", "Hvatning", "rocket", "#A560E8"),
    ("Love", "Ást", "heart", "#FF4B4B"),
    ("Success", "Velgengni", "trophy", "#F5A700"),
    ("Wisdom", "Viska", "book", "#A560E8"),
    ("Happiness", "Hamingja", "smile", "#F5A700"),
    ("Self Improvement", "Sjálfsbæting", "leaf", "#58CC02"),
    ("Gratitude", "Þakklæti", "heart", "#FF7A00"),
    ("Friendship", "Vinátta", "users", "#00A889"),
    ("Hope", "Von", "sun", "#FF7A00"),
    ("Creativity", "Sköpunargáfa", "palette", "#E056A0"),
    ("Inner Peace", "Innri Friður", "lotus", "#00A889"),
    ("Confidence", "Sjálfstraust", "shield", "#1CB0F6"),
    ("Perseverance", "Þrautseigja", "mountain", "#FF7A00"),
    ("Inspiration", "Innblástur", "sparkles", "#A560E8"),
    ("Positive Life", "Jákvætt Líf", "sun", "#58CC02"),
    ("Courage", "Hugrekki", "shield", "#FF4B4B"),
    ("Kindness", "Góðvild", "heart", "#E056A0"),
    ("Patience", "Þolinmæði", "hourglass", "#00A889"),
    ("Forgiveness", "Fyrirgefning", "hands", "#FF7A00"),
    ("Strength", "Styrkur", "dumbbell", "#FF4B4B"),
    ("Joy", "Gleði", "smile", "#F5A700"),
    ("Balance", "Jafnvægi", "scale", "#00A889"),
    ("Growth", "Vöxtur", "sprout", "#58CC02"),
    ("Purpose", "Tilgangur", "target", "#A560E8"),
    ("Mindfulness", "Núvitund", "lotus", "#00A889"),
    ("Daily Routine", "Dagleg venja", "calendar", "#1CB0F6"),
    ("Weather", "Veður", "cloud", "#1CB0F6"),
    ("Feelings", "Tilfinningar", "smile", "#E056A0"),
    ("Food", "Matur", "fork", "#FF7A00"),
    ("Health", "Heilsa", "heart", "#58CC02"),
    ("Work", "Vinna", "briefcase", "#1CB0F6"),
    ("Technology", "Tækni", "chip", "#A560E8"),
    ("Nature", "Náttúra", "leaf", "#58CC02"),
    ("Animals", "Dýr", "paw", "#FF7A00"),
    ("Colors", "Litir", "palette", "#E056A0"),
    ("Directions", "Áttir", "compass", "#1CB0F6"),
    ("Body Parts", "Líkamshlutar", "hand", "#00A889"),
    ("Clothes", "Föt", "shirt", "#E056A0"),
    ("Music", "Tónlist", "music", "#A560E8"),
    ("Sports", "Íþóttir", "ball", "#FF7A00"),
    ("Holidays", "Frídagar", "gift", "#FF4B4B"),
    ("Education", "Menntun", "book", "#1CB0F6"),
    ("Culture", "Menning", "globe", "#00A889"),
    ("Finance", "Fjármál", "coin", "#58CC02"),
    ("Relationships", "Tengsl", "users", "#E056A0"),
]
# ==== CATEGORY TABLE END ====

CATEGORIES = [c[0] for c in CATEGORY_TABLE]
CATEGORIES_NATIVE = {c[0]: c[1] for c in CATEGORY_TABLE}
CATEGORY_META = {c[0]: {"native": c[1], "icon": c[2], "accent": c[3]} for c in CATEGORY_TABLE}
MAX_RECENT_CATEGORIES = 25

# ==== HASHTAGS START ====
HASHTAGS = [
    "#learnicelandic",
    "#icelandiclessons",
    "#icelandicforbeginners",
    "#languagelearning",
    "#icelandicvocabulary",
    "#velocityicelandic",
    "#dailyicelandic",
    "#icelandic",
    "#learnlanguages",
    "#speakicelandic",
    "#bilingual",
    "#languagetips",
]
# ==== HASHTAGS END ====
