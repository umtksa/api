import requests
import re

# Online txt dosyasını indir
url = "https://raw.githubusercontent.com/umtksa/api/main/sentences.txt"
response = requests.get(url)
if response.status_code == 200:
    sentences = response.text.splitlines()  # Her satırı bir eleman olarak alır
else:
    print("Dosya indirilemedi.")
    sentences = []

# Regex patternleri
patterns = {
    'zaman': r'\b(ne zaman\w*)\b',
    'nasıl': r'\b(nasıl\w*)\b',
    'naber': r'\b(naber\w*)\b',
    'hangi': r'\b(hangi\w*)\b',
    'yer': r'\b(nere|nere\w*)\b',
    'fiyat': r'\b(kaça|fiyat\w*)\b',
    'miktar': r'\b(kaç)\b',
    'kişi': r'\b(kim|kim\w*)\b',
    'mı': r'\b(mi\w*|mü\w*|mı\w*|mu\w*)\b',
    'ne': r'\b(ne|ne\w*)\b'
}

def identify_question_type(sentence):
    if '?' not in sentence:
        return 'Belirlenemedi', sentence

    for category, pattern in patterns.items():
        match = re.search(pattern, sentence, re.IGNORECASE)
        if match:
            return category, match.group()

    return 'Belirlenemedi', sentence

def process_sentences(sentences):
    categorized_questions = {
        'zaman': [],
        'nasıl': [],
        'naber': [],
        'hangi': [],
        'yer': [],
        'fiyat': [],
        'miktar': [],
        'kişi': [],
        'mı': [],
        'ne': [],
        'Belirlenemedi': []
    }

    for sentence in sentences:
        category, matched_part = identify_question_type(sentence)
        if category == 'Belirlenemedi':
            categorized_questions['Belirlenemedi'].append(sentence)
        else:
            categorized_questions[category].append(sentence)

    return categorized_questions

# Sonuçları yazdırma
categorized_questions = process_sentences(sentences)

# Başlıkları bir kez yazdır ve altına o başlıktaki cümleleri yazdır
for category in patterns.keys():
    if categorized_questions[category]:
        print(f"--- {category} soruları ---")
        for question in categorized_questions[category]:
            print(f"- {question}")


# Soru olmayan cümleleri en sona koy
if categorized_questions['Belirlenemedi']:
    print(f"--- soru olmayanlar ---")
    for sentence in categorized_questions['Belirlenemedi']:
        print(f"- {sentence}")
