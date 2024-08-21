import requests
import re

# Online txt dosyasını indir
url = "https://raw.githubusercontent.com/umtksa/api/main/sentences.txt"
response = requests.get(url)
sentences = response.text.splitlines() if response.status_code == 200 else []

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
        return 'Belirlenemedi'
    
    for category, pattern in patterns.items():
        if re.search(pattern, sentence, re.IGNORECASE):
            return category

    return 'Belirlenemedi'

def process_sentences(sentences):
    categorized_questions = {category: [] for category in patterns.keys()}  # Kategorileri oluştur
    categorized_questions['Belirlenemedi'] = []

    for sentence in sentences:
        category = identify_question_type(sentence)
        categorized_questions[category].append(sentence)

    return categorized_questions

# Sonuçları yazdırma
categorized_questions = process_sentences(sentences)

for category, questions in categorized_questions.items():
    if questions:
        print(f"--- {category} ---")
        for question in questions:
            print(f"- {question}")
