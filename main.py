from tika import parser

# PDF dosyasını parse et
raw = parser.from_file('data/1.pdf')

# Metadata kısmını al
metadata = raw['metadata']

with open("logs/metadata.log", "w", encoding="utf-8") as log_file:
    for key, value in metadata.items():
        log_file.write(f"{key}: {value}\n")