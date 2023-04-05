def arama(dosya_adi, a_kelime):

    adet = 0
    with open(dosya_adi, 'r') as dosya:
        for ara in dosya:
            kelimeler = ara.strip().split()
            for kelime in kelimeler:
                if kelime.lower() == a_kelime.lower():
                    adet += 1
    return adet


dosya_adi = "alice_in_wonderland.txt"
a_kelimeler = ["upon", "sigh", "Dormouse","jury-box","swim"]

for a_kelime in a_kelimeler:
    adet = arama(dosya_adi, a_kelime)
    print(f"'{a_kelime}' kelimesi {adet} kez geçiyor.")