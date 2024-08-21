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
    'hangi': r'\b(hangi\w*)\b',
    'yer': r'\b(nere|nere\w*)\b',
    'fiyat': r'\b(kaça)\b',
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

def extract_core_question(sentence, category):
    # Her kategori için özelleştirilmiş çıkarım fonksiyonları burada yer alabilir
    if category == 'zaman':
        return re.sub(patterns[category], '', sentence).strip()
    elif category == 'yer':
        return re.sub(patterns[category], '', sentence).strip()
    # Diğer kategoriler için de benzer işlemler yapılabilir
    return sentence

def process_sentences(sentences):
    identified_questions = []
    unidentified_questions = []

    for sentence in sentences:
        category, matched_part = identify_question_type(sentence)
        if category == 'Belirlenemedi':
            unidentified_questions.append(sentence)
        else:
            core_question = extract_core_question(sentence, category)
            identified_questions.append((category, core_question))

    return identified_questions, unidentified_questions

# Sonuçları yazdırma
identified_questions, unidentified_questions = process_sentences(sentences)

for q_type, sentence in identified_questions:
    print(f"{q_type} - {sentence}")

print(f"-----")

for sentence in unidentified_questions:
    print(f"Cümle: {sentence}")
