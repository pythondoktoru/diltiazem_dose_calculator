# diltiazem iv doz hesaplayıcı:
kilo = int(input("Hastanın kilosunu giriniz: "))
ilk_doz_k = 0.25
ikinci_doz_k = 0.35

ilk_doz = kilo * ilk_doz_k
ikinci_doz = kilo * ikinci_doz_k

if ilk_doz < 20:
    print(f"ilk doz: {ilk_doz} mg İV")
else:
    print(f"ilk doz: 20 mg İV")

if ikinci_doz < 25:
    print(f"ikinci doz: {ikinci_doz} mg İV")
else:
    print(f"ikinci doz: 25 mg İV")
