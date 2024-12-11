from dotenv import load_dotenv
import os


def get_env(var):
    load_dotenv()
    return os.getenv(var)

languages = ['en'
             #    "ar",
             #    "bg",
             #    "cs", "da", "de", "en",
             #      "bg", "cs", "da", "de", "el", "es", "fi", "fr", "he", "hi", "hr", "hu", "id",
             #      "it", "ja", "ko", "ms", "nl", "no", "pl", "pt", "pt-br", "ro", "sk", "sl", "sr", "sv",
             #      "th", "tr", "uk", "zh-cn", "zh-hk"
             ]