# Şehirler ve plakaları
plaka_bilgileri = {
    "Adana": "01",
    "Adıyaman": "02",
    "Afyon": "03",
    "Ağrı": "04",
    "Amasya": "05",
    "Ankara": "06",
    "Antalya": "07",
    "Artvin": "08",
    "Aydın": "09",
    "Balıkesir": "10",
    "Bilecik": "11",
    "Bingöl": "12",
    "Bitlis": "13",
    "Bolu": "14",
    "Burdur": "15",
    "Bursa": "16",
    "Çanakkale": "17",
    "Çankırı": "18",
    "Çorum": "19",
    "Denizli": "20",
    "Diyarbakır": "21",
    "Edirne": "22",
    "Elazığ": "23",
    "Erzincan": "24",
    "Erzurum": "25",
    "Eskişehir": "26",
    "Gaziantep": "27",
    "Giresun": "28",
    "Gümüşhane": "29",
    "Hakkari": "30",
    "Hatay": "31",
    "Isparta": "32",
    "Mersin": "33",
    "İstanbul": "34",
    "İzmir": "35",
    "Kars": "36",
    "Kastamonu": "37",
    "Kayseri": "38",
    "Kırklareli": "39",
    "Kırşehir": "40",
    "Kocaeli": "41",
    "Konya": "42",
    "Kütahya": "43",
    "Malatya": "44",
    "Manisa": "45",
    "Kahramanmaraş": "46",
    "Mardin": "47",
    "Muğla": "48",
    "Muş": "49",
    "Nevşehir": "50",
    "Niğde": "51",
    "Ordu": "52",
    "Rize": "53",
    "Sakarya": "54",
    "Samsun": "55",
    "Siirt": "56",
    "Sinop": "57",
    "Sivas": "58",
    "Tekirdağ": "59",
    "Tokat": "60",
    "Trabzon": "61",
    "Tunceli": "62",
    "Şanlıurfa": "63",
    "Uşak": "64",
    "Van": "65",
    "Yozgat": "66",
    "Zonguldak": "67",
    "Aksaray": "68",
    "Bayburt": "69",
    "Karaman": "70",
    "Kırıkkale": "71",
    "Batman": "72",
    "Şırnak": "73",
    "Bartın": "74",
    "Ardahan": "75",
    "Iğdır": "76",
    "Yalova": "77",
    "Karabük": "78",
    "Kilis": "79",
    "Osmaniye": "80",
    "Düzce": "81"
}

# Plaka ve şehir eşleşmesini kontrol eden fonksiyon
def clean(cumle):
    plaka = None
    sehir = None
    
    # Şehir ismini bulma
    for sehir_adi in plaka_bilgileri.keys():
        if sehir_adi.lower() in cumle.lower():
            sehir = sehir_adi
            break
    
    # Plaka numarasını bulma
    for plaka_numarasi in plaka_bilgileri.values():
        if plaka_numarasi in cumle:
            plaka = plaka_numarasi
            break
    
    return plaka, sehir

# Plaka kodunu ve şehir adını sorgulayan fonksiyon
def plaka_sorgula(cumle):
    plaka, sehir = clean(cumle)
    
    if plaka and sehir:
        # Eğer hem plaka hem şehir varsa, bunları karşılaştırıyoruz
        if plaka == plaka_bilgileri[sehir]:
            return "Evet, doğru!"
        else:
            if cumle.lower().find(plaka) < cumle.lower().find(sehir.lower()):
                # Önce plaka kodu yazıldıysa, şehir doğru mu diye kontrol et
                dogru_sehir = [s for s, p in plaka_bilgileri.items() if p == plaka]
                return f"Hayır, {plaka} plakalı il {dogru_sehir[0]}."
            else:
                # Önce şehir ismi yazıldıysa, plaka doğru mu diye kontrol et
                return f"Hayır, {sehir} ilinin plakası {plaka_bilgileri[sehir]}."
    elif plaka:
        # Yalnızca plaka varsa
        for sehir, plaka_numarasi in plaka_bilgileri.items():
            if plaka == plaka_numarasi:
                return f"{plaka}, {sehir} ilinin plakasıdır."
        return f"{plaka} plaka kodu olan bir il yok."
    elif sehir:
        # Yalnızca şehir varsa
        return f"{sehir} ilinin plaka kodu {plaka_bilgileri[sehir]}."
    else:
        return "Geçerli bir soru algılanamadı."

# Test soruları
sorular = [
    "16 nerenin plakasıdır?",
    "33 nerenin plakasıdır?",
    "Antalyanın plakası nedir?",
    "İzmir'in plakası nedir?",
    "İzmir'in plakası kaçtır?",
    "Ankara'nın plakası nedir?",
    "Ankara'nın plakası kaçtır?",
    "31 Hatayın plakası mıdır?",
    "07 Hatayın plakası mıdır?",
    "hatayın plakası 34 müdür?",
    "hatayın plakası 31 midir?"
]

for soru in sorular:
    print(f"Soru: {soru}")
    print(f"Cevap: {plaka_sorgula(soru)}")
    print(" " * 50)
