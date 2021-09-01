class hesapmakinesi (object):

   def __init__(self,sayi1,sayi2):

       self.value1 = self.sayi1
       self.value2 = self.sayi2

    
   def topla(self):

        return self.value1 + self.value2

   def cikar (self):

       return self.sayi1 - self.sayi2

   def carp (self):

        return self.sayi1 * self.sayi2

   def bol (self):

       return self.sayi1 / self.sayi2



sayilar1 = int(input("Birinci Sayıyı Giriniz: "))
sayilar2 = int(input("İkinci Sayıyı Giriniz:  "))
sonuc = hesapmakinesi(sayilar1,sayilar2)
print("Girilen Sayıların Toplamı: ",sonuc.topla())

