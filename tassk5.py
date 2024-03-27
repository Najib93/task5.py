#Task1
def calculate_bmi(weight, height):
    """
    BMI hesablayan funksiya
    """
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi):
    """
    BMI kateqoriyasını təyin edən funksiya
    """
    if bmi < 18.5:
        return "Az çəki"
    elif 18.5 <= bmi < 25:
        return "Normal çəki"
    elif 25 <= bmi < 30:
        return "Artıq çəki"
    else:
        return "Piylənmə"

def main():
    weight = float(input("Çəkini kiloqramla daxil edin: "))
    height = float(input("Boyunuzu metrlə daxil edin: "))

    bmi = calculate_bmi(weight, height)
    print("BMI-niz:", bmi)

    bmi_category = get_bmi_category(bmi)
    print("BMI kateqoriyası:", bmi_category)

if __name__ == "__main__":
    main()
class ButceAlati:
    def __init__(self):
        self.gider_listesi = []
        self.gelir_listesi = []

    def gider_ekle(self, gider):
        self.gider_listesi.append(gider)

    def gelir_ekle(self, gelir):
        self.gelir_listesi.append(gelir)

    def toplam_gider_hesapla(self):
        return sum(self.gider_listesi)

    def toplam_gelir_hesapla(self):
        return sum(self.gelir_listesi)

    def kalan_butce_hesapla(self):
        toplam_gider = self.toplam_gider_hesapla()
        toplam_gelir = self.toplam_gelir_hesapla()
        return toplam_gelir - toplam_gider

def main():
    butce_alati = ButceAlati()

    while True:
        gider = float(input("Aylık giderleri girin (bitirmek için 0'a basın): "))
        if gider == 0:
            break
        butce_alati.gider_ekle(gider)

    while True:
        gelir = float(input("Aylık gelirleri girin (bitirmek için 0'a basın): "))
        if gelir == 0:
            break
        butce_alati.gelir_ekle(gelir)

    kalan_butce = butce_alati.kalan_butce_hesapla()

    print("\nToplam Gider: {:.2f}".format(butce_alati.toplam_gider_hesapla()))
    print("Toplam Gelir: {:.2f}".format(butce_alati.toplam_gelir_hesapla()))
    print("Kalan Bütçe: {:.2f}".format(kalan_butce))

if __name__ == "__main__":
    main()



#Task2
def calculate_bmi(weight, height):
    """
    BMI hesablayan funksiya
    """
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi):
    """
    BMI kateqoriyasını təyin edən funksiya
    """
    if bmi < 18.5:
        return "Az çəki"
    elif 18.5 <= bmi < 25:
        return "Normal çəki"
    elif 25 <= bmi < 30:
        return "Artıq çəki"
    else:
        return "Piylənmə"

def main():
    weight = float(input("Çəkini kiloqramla daxil edin: "))
    height = float(input("Boyunuzu metrlə daxil edin: "))

    bmi = calculate_bmi(weight, height)
    print("BMI-niz:", bmi)

    bmi_category = get_bmi_category(bmi)
    print("BMI kateqoriyası:", bmi_category)

if __name__ == "__main__":
    main()

