import requests
basali=0
basarisiz=0
for i in range(69685,69690):
    url = "https://www.gutenberg.org/cache/epub/"+str(i)+"/pg"+str(i)+".txt"  # İndirmek istediğiniz dosyanın URL'sini buraya ekleyin
    response = requests.get(url)
    print(url)
    if response.status_code == 200:
        with open("pg"+str(i)+".txt", 'wb') as file:
            file.write(response.content)
        basali+=1;
        print(basali, '. dosya başarıyla indirildi.')
    else:
        basarisiz+=1
        print(basarisiz,'. dosya indirilemedi . Hata kodu:', response.status_code)
       
       


# https://www.gutenberg.org/ebooks/47629.txt.utf-8