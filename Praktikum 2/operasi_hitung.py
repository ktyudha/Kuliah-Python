def hitung_genap_ganjil(data):
    bilangan_genap = [bilangan for bilangan in data if bilangan % 2 == 0]
    bilangan_ganjil = [bilangan for bilangan in data if bilangan % 2 != 0]

    return bilangan_genap, bilangan_ganjil