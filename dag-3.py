#index
myString = "Warisjan"
print(myString[7])
print(len(myString))
#Slicing , starting index , stopping index , stepping size
# indexleri parcalama islemi yaparken kullaniyoruz
barcode ="AVC12312399"
#barcode[Slicing:starting index:stopping index :stepping size]
# Starting : nereden basyalarak paracayacagimizi
print(barcode[3::])  
#stopping : nerede bitecegini 
print(barcode[:5:])  
#stepping size : kacar adim atlayacigini bildiriyor
print(barcode[::2]) 
# stepping size'i -1 yaparsak barkod numarasini terse cevirir
print(barcode[::-1])
# degiskene index atarsak indexin kacinci dizide oldugu konumunu verir
print(barcode.index("A"))
#split()
print(type(barcode.split()))

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                 List
                append,count,insert,pop,remove,reverce,sort
           List- icinde birden fazla veri tutmak icin kullaniyoruz
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
myList=[10,20,30]
print(len(myList))
print(len(myList)-1)
print(myList[1])
print(type(myList[1]))
#append-listeye yeni eleman eklemek istiyorsak kullaniriz 
myList.append(80)
print(myList)
#count- len ile farklidir , cout dizi icinde kac tane eleman var bize verir
print(myList.count(10))
#insert - eleman eklemek iscin kullaniyoruz ama farki index olrak kacinci eleman ve ne ekleyecegimizi girebiliriz
myList.insert(3,"W")
print(myList)
#pop listedeki son elemani cikarir
myList.pop()
print(myList)
#remove-cikarmak istedigimiz elemani girerek cikarabiliri
myList.remove(10)
print(myList)
#reverse-tersine cevirmek
myList.reverse()
print(myList)
#sort- 
#
myInteger= 50
myInteger=str(myInteger)
print(type(myInteger))
myList.remove("W")
print(myList)
#Liste icinde liste barinabilir
lastList =['a','b','c',['wc','toalet'],'d','w']
print(lastList[3][1])