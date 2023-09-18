import math
import random
# uzunluk = int(input("Uzunluk giriniz"))

# for i in range (uzunluk):
#     print(" "*i + "*"*(uzunluk-i)+"*"*(uzunluk-i-1))
    
    
# xxxxx
# |
# |
# |
# |   x

# x = int(input("x sayısı girin"))
# y= int(input("Y sayısı girin"))

# for i in range(y):
#     if i ==0:
#         print("x"*x)
#     elif i==y-1:
#         print("|"+" "*(x-2) + "x")
#     else:
#         print("|")

# ! girilen değere kadar toplamını yazdıran toplam

# x = int(input("sayı giriniz: "))
# toplam = 0
# for i in range (x):
#     toplam+=i
# print(toplam)

# ! while 

# i=0
# while i<10:
#     print(i)
#     i+=1

# ! sayı tahmin oyunu
# hak = 5
# sayi = random.randint(0,9)
# print("sayi : " , sayi)






# while hak>0:
#     tahmin = int(input("tahmininizi giriniz: "))
    
#     if tahmin == sayi:
       
#         print("Bildiniz")
        
        
#         break
#     else:
#         hak-=1
#         if hak != 0:
#            print("tekrar deneyiniz")
        
#         elif hak ==0:
#             print("hakkınız bitti")
       
# ! ATM uygulaması
# bakiye =1000
# print("Bakiyeniz: " , bakiye)
# while True:
#     print("""İşlemler: 
# 1. Para Çekme
# 2. Para Yatırma
# 3. Para Gönderme
# 4. Çıkış""")
#     x = int(input("Yapmak istediğiniz işlemi seçin: "))
#     if x==4:
#         print("çıkış yapıldı")
#         break

#     elif x==1:
#         cekme = int(input("Çekmek istediğiniz miktarı girin : "))
#         bakiye-=cekme
#     elif x ==2:
#         yatirma = int(input("Yatırmak istediğiniz mikarı girin: "))
#         bakiye+=yatirma
#     elif x ==3:
#         gonderme = int(input("Göndermek istediğiniz miktarı girin: "))
#         bakiye-=gonderme
        
#     print("Yeni bakiyeniz: " , bakiye)
   
# ! Listeler

# isimler = ["Emre", "Ali", "Ahmet", "Mehmet"]

# for i in isimler:
#     print(i)


# for i in range(len(isimler)):
#     print(isimler[i])

# isimler.append("abc")
# isimler.insert(0, "Ayşe")
# isimler.pop(2)
# print(isimler)

# print(isimler[::-1])
# print(isimler[2][3])

# liste1 = [1,2,3,4,5,6,7,8,9,10]
# liste2 = [11,12,13,14,15,16,17,18,19,20]

# for i in liste2:
#     liste1.append(i)

# print(liste1)

# bilgi= "emre orman 36 izmir"
# print(bilgi.split())

# ! Çok boyutlu listeler

# listem = [["Emre", "Ali" , "Ahmet" , "Ayşe"],[25,24,28,27]]
# # print(listem[0][1])
# for i in range(len(listem[0])):
#     print(listem[0][i] , listem[1][i])

# listem=[18,6,34,1,66,41,2]
# listem.sort(reverse=True)
# print(listem[1])

# listem2=["Istanbul","Izmir","Ankara","Bursa","Antalya","Muğla","Zonguldak","1","2","3","4"]
# listem2.sort(reverse=True)
# print(listem2)
# isimler ="Emre","Orman",1,2,4,3
# print(isimler)