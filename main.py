from tika import parser
from tika import language

# PDF dosyasını parse et
raw = parser.from_file('data/1.pdf')

# Metadata kısmını al
metadata = raw['metadata']

def extract_metadata(metadata):
    # Metadata'dan gerekli bilgileri al
    with open("logs/metadata.log", "w", encoding="utf-8") as log_file:
        for key, value in metadata.items():
            log_file.write(f"{key}: {value}\n")

content = raw['content']
def extract_content(content):
    # İçeriği log dosyasına yaz
    with open("logs/content.log", "w", encoding="utf-8") as log_file:
        log_file.write(content)

def detect_language(content):
    # İçeriğin dilini tespit et
    lang = language.from_buffer(content)
    with open("logs/language.log", "w", encoding="utf-8") as log_file:
        log_file.write(f"Detected language: {lang}\n")

detect_language(content)