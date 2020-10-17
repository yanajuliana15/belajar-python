#Contoh penggunaan While Loop
#Catatan: Penentuan ruang lingkup di Python bisa menggunakan tab alih-alih menggunakan tanda kurung

count = 0
while (count < 9):
    print ("The count is: ", count)
    count = count + 1

print ("Good bye!")

count = 1 
while ( count < 9):
    print (" count is ",count)
    count = count + 2
print ( "good bye")

#Contoh pengulangan for sederhana
angka = [1,2,3,4,5]
for x in angka:
    print(x)

#Contoh pengulangan for
buah = ["nanas", "apel", "jeruk"]
for makanan in buah:
    print ("Saya suka makan", makanan)


sayuran = ["tomat","koll","wortel"]
for makanan in sayuran :
    print ("saya suka makan",makanan)


i = 2
while(i < 100):
    j = 5
    while(j <= (i/j)):
        if not(i%j): break
        j = j + 1
    if (j > i/j) : print(i, " is prime")
    i = i + 1

print("Good bye!")