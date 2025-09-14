                        # 1.Dictionary 

# key-value pairs ,ilk yazdigimiz anahtar okinci yazdigimiz degerler oluyor
fruits = {"apple" : 100 , "banana" :200 , "oragnge" : 300}
print(fruits["apple"])
# Dictionary'deki anahtarlari gostermek icin keys() kullancam .
print(fruits.keys())
# Dictionary'deki Degerleri gostermek icin values() kullancam .
print(fruits.values())
# Dictionary values deki degerleri liste donusturmek icin 
print(list(fruits.values()))
# Dictionary ile veri eklemek icin 
fruits["Mellon"] = 250
print(fruits)
# get pramaetresi degeri almak icin kullaniyoruz 
print(fruits.get("Mellon" , 0))
#
last_dictionary = {"k1" : 10 , "k2" : [10,20,30,40,50], "k3" : "string" ,"k4" : {"a" : 100 , "b" : 200}}
print(last_dictionary["k2"][2])
print(last_dictionary["k4"]["b"])

                        #2.SET
# Python’da set (küme) veri tipi, benzersiz öğelerden oluşan ve sırasız bir koleksiyon sağlar. Set’ler özellikle tekrar eden öğeleri filtrelemek, kesişim, birleşim, fark gibi küme işlemleri yapmak için çok kullanışlıdır. 
#Set olusturmak - Asaginda Eple 3 kere olmasina ramaen ekrana yazdigimda bir kere gorunuyor -
fruits = {"Eple","Pare","Jodre","Eple","Eple"}
print(fruits)
#eleman eklemek icin add() kullaniyoruz
fruits.add("cherry")
print(fruits)
#Eleman silme remove()
fruits.remove("Jodre")
print(fruits)
# Tum elemanlari temizlemek icin clear() 
fruits.clear()
print(fruits)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Birleşim
print(a | b)  # {1, 2, 3, 4, 5, 6}

# Kesişim
print(a & b)  # {3, 4}

# Fark
print(a - b)  # {1, 2}
print(b - a)  # {5, 6}

# Simetrik fark (iki kümede sadece birinde olanlar)
print(a ^ b)  # {1, 2, 5, 6}

                        #2.TUPLE
# Python’da tuple (demet), değiştirilemez (immutable) ve sıralı bir veri tipidir. Listelere benzer ama içeriği sonradan değiştirilemez. Tuple’lar genellikle sabit veri depolamak veya fonksiyonlardan birden fazla değer döndürmek için kullanılır.
# Boş tuple       
t1 = ()
# Tek elmemani tuple (virgul onemli)
t2 = (5,)
print(t2)
# Birden fazla eleman
t3 = (1, 2, 3, 4)
print(t3)
# Farklı veri tipleri de olabilir
t4 = (1, "apple", 3.14, True)
print(t4)
                    # 2. Tuple Elemanlarına Erişim
t = (10,20,30,40,50)    
print([0])  #ilk elemean
print([-1])  #son eleman
print(t[1:4])  #dilimleme (20,30,40)    

                    #Boolean
#True veye False iki sekilde deger donduruyor .                  
print(5>4)