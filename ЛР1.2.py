# TODO Найдите количество книг, которое можно разместить на дискете
Disk_volume = 2.53
Pages = 240
Lines = 50
simbols = 25
Per_one = 4
Disk_volume_b = Disk_volume * 1024 * 1024
Book_volume_B = Pages * Lines * simbols * Per_one
Number = Disk_volume_b // Book_volume_B
print("Количество книг, помещающихся на дискету:", int(Number))