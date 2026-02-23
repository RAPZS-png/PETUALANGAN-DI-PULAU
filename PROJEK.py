import time
import sys
import os
import random
def ketik(teks):
    for huruf in teks:
        sys.stdout.write(huruf)
        sys.stdout.flush()
        time.sleep(0.10)
    print()
def nama_player():
    nama = input("masukkan nama karakter : ")
    if nama == "":
        nama = "NoName"
    return nama

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def ending(nama, tipe):
    if tipe == "koper":
        jumlah_koper = random.randint(1, 2)
        koper_benar = random.randint(1, jumlah_koper)

        ketik(f"\n{nama} menemukan {jumlah_koper} koper misterius")
        ketik("Salah satunya mungkin berisi barang yang bisa menyelamatkanku.")

        for i in range(1, jumlah_koper + 1):
            ketik(f"{i}. Buka koper {i}")

        pilihan = input("Pilih nomor koper: ")

        if pilihan.isdigit() and 1 <= int(pilihan) <= jumlah_koper:
            if int(pilihan) == koper_benar:
                ketik("Koper terbuka...")
                ketik("Isinya FLARE!")
                ketik("Kamu menyalakan flare.")
                ketik("Helikopter datang menjemput.")
                ketik("ENDING: SELAMAT DENGAN FLARE")
            else:
                ketik("Koper terbuka...")
                ketik("Isinya cuma sampah.")
                ketik("Tidak ada flare.")
                ketik("ENDING: GAGAL MENEMUKAN FLARE")
            exit()

kayu = 0

def menu_aksi(nama):
    global kayu, stamina

    while True:
        tampil_stamina()
        print(f"Kayu: {kayu}")
        print("\nApa yang mau kamu lakukan?")
        print("1. Jelajah pulau")
        print("2. Nebang pohon (+5 kayu)")
        print("3. Bengong")
        print("4. Tidur (ganti hari dan reset stamina)")

        pilihan = input("Pilih 1-4: ")

        if pilihan not in ["1", "2", "3", "4"]:
            print("Pilih angka 1 sampai 4, jangan ngaco.")
            continue

        if pilihan == "1":
            jelajah(nama)

        elif pilihan == "2":
            nebang()

        elif pilihan == "3":
            bengong()

        elif pilihan == "4":
            tidur()
            tampil_hari()
            
def jelajah(nama):
    ketik(f"\n{nama} menjelajah pulau...")
    kurang_stamina(15)

    event = random.randint(1,3)

    if event == 1:
        ketik("Kamu menemukan buah liar.")
        inventory.append("Buah")
    elif event == 2:
        ketik("menemukan koper misterius.")
        ending(nama, "koper")
    else:
        ketik("Tidak menemukan apa-apa.")

def nebang():
    global kayu
    ketik("\nKamu menebang pohon...")
    kurang_stamina(20)
    kayu += 5
    print("Dapet 5 kayu.")

def bengong():
    ketik("\nKamu bengong menatap laut...")
    ketik("\nMelakukan hal tak berguna yang mengurangi stamina.")
    kurang_stamina(5)

def tidur():
    global stamina
    ketik("\nKamu tidur semalaman...")
    stamina = 100
    next_hari()



def prolog(nama, skip = False):
    if skip:
        return
    tampil_hari()
    tampil_stamina
    ketik(f"\n{nama} hari ini pergi ke maladewa dengan menaiki pewasat.")
    ketik("ia pergi kesana untuk berlibur dan menjauh sejenak dari kelelahan yang menimpa nya.")
    ketik("Ia menatap jendela pesawat dengan senyum kecil.")
    ketik("Ia yakin perjalanan ini akan membawanya pada ketenangan yang dia cari selama ini.")
    ketik("\nNamun, dunia seakan berkata lain.")
    ketik("\nMesin meraung aneh")
    ketik("lampu berkedip")
    ketik("\nGelap.")
    ketik("....")
    ketik("\nIa terbangun di pulau asing.")
    ketik("terdengar debur ombak dan angin kencang.")
    ketik("\nhah, ini gue dimana?")
    ketik("gimana pun cara nya gue tetep harus hidup.")

stamina = 100
def tampil_stamina():
    print(f"stamina : {stamina}/100")
def kurang_stamina(jumlah):
    global stamina
    stamina -= jumlah
    if stamina <= 0:
        stamina = 0
        print("lau kecapean. tumbang")
        print("GAME OVER")
        exit()
hari =  1
def tampil_hari():
    print("\n" + "="*25)
    print(f"        HARI KE-{hari}")
    print("="*25 + "\n")
    time.sleep(1)

def next_hari():
    global hari
    hari +=1

nama = nama_player()
tampil_stamina()
inventory = []
KAPASITAS_MAX = 8 
prolog(nama) 
clear()
tampil_hari()
menu_aksi(nama)

def starting_item():
    tambah_item("Kapak", 1)
    tambah_item("Air Minum", 5)
    


KAPASITAS_MAX = 8
inventory = []

def lihat_inventory():
    print("\n=== INVENTORY ===")

    if not inventory:
        print("Inventory kosong!")
    else:
        for index, item in enumerate(inventory, start=1):
            print(f"{index}. {item}")

    print(f"Slot: {len(inventory)}/{KAPASITAS_MAX}")



def tambah_item(item):
    if not item.strip():
        return  

    if len(inventory) >= KAPASITAS_MAX:
        print("Inventory penuh!")
        return

    if item in inventory:
        print(f"{item} sudah ada!")
        return

    inventory.append(item)
    print(f"{item} ditambahkan!")



def hapus_item(item):
    if item not in inventory:
        print(f" {item} tidak ada!")
        return

    inventory.remove(item)
    print(f" {item} dihapus!")



tambah_item("")
tambah_item("")
tambah_item("")
lihat_inventory()
hapus_item("")
lihat_inventory()
import time
import sys
import os
import random
def ketik(teks):
    for huruf in teks:
        sys.stdout.write(huruf)
        sys.stdout.flush()
        time.sleep(0.10)
    print()
def nama_player():
    nama = input("masukkan nama karakter : ")
    if nama == "":
        nama = "NoName"
    return nama

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def ending(nama, tipe):
    if tipe == "koper":
        jumlah_koper = random.randint(1, 2)
        koper_benar = random.randint(1, jumlah_koper)

        ketik(f"\n{nama} menemukan {jumlah_koper} koper misterius")
        ketik("Salah satunya mungkin berisi barang yang bisa menyelamatkanku.")

        for i in range(1, jumlah_koper + 1):
            ketik(f"{i}. Buka koper {i}")

        pilihan = input("Pilih nomor koper: ")

        if pilihan.isdigit() and 1 <= int(pilihan) <= jumlah_koper:
            if int(pilihan) == koper_benar:
                ketik("Koper terbuka...")
                ketik("Isinya FLARE!")
                ketik("Kamu menyalakan flare.")
                ketik("Helikopter datang menjemput.")
                ketik("ENDING: SELAMAT DENGAN FLARE")
            else:
                ketik("Koper terbuka...")
                ketik("Isinya cuma sampah.")
                ketik("Tidak ada flare.")
                ketik("ENDING: GAGAL MENEMUKAN FLARE")
            exit()

kayu = 0

def menu_aksi(nama):
    global kayu, stamina

    while True:
        tampil_stamina()
        print(f"Kayu: {kayu}")
        print("\nApa yang mau kamu lakukan?")
        print("1. Jelajah pulau")
        print("2. Nebang pohon (+5 kayu)")
        print("3. Bengong")
        print("4. Tidur (ganti hari dan reset stamina)")

        pilihan = input("Pilih 1-4: ")

        if pilihan not in ["1", "2", "3", "4"]:
            print("Pilih angka 1 sampai 4, jangan ngaco.")
            continue

        if pilihan == "1":
            jelajah(nama)

        elif pilihan == "2":
            nebang()

        elif pilihan == "3":
            bengong()

        elif pilihan == "4":
            tidur()
            tampil_hari()
            
def jelajah(nama):
    ketik(f"\n{nama} menjelajah pulau...")
    kurang_stamina(15)

    event = random.randint(1,3)

    if event == 1:
        ketik("Kamu menemukan buah liar.")
        inventory.append("Buah")
    elif event == 2:
        ketik("menemukan koper misterius.")
        ending(nama, "koper")
    else:
        ketik("Tidak menemukan apa-apa.")

def nebang():
    global kayu
    ketik("\nKamu menebang pohon...")
    kurang_stamina(20)
    kayu += 5
    print("Dapet 5 kayu.")

def bengong():
    ketik("\nKamu bengong menatap laut...")
    ketik("\nMelakukan hal tak berguna yang mengurangi stamina.")
    kurang_stamina(5)

def tidur():
    global stamina
    ketik("\nKamu tidur semalaman...")
    stamina = 100
    next_hari()



def prolog(nama, skip = True):
    if skip:
        return
    tampil_hari()
    tampil_stamina
    ketik(f"\n{nama} hari ini pergi ke maladewa dengan menaiki pewasat.")
    ketik("ia pergi kesana untuk berlibur dan menjauh sejenak dari kelelahan yang menimpa nya.")
    ketik("Ia menatap jendela pesawat dengan senyum kecil.")
    ketik("Ia yakin perjalanan ini akan membawanya pada ketenangan yang dia cari selama ini.")
    ketik("\nNamun, dunia seakan berkata lain.")
    ketik("\nMesin meraung aneh")
    ketik("lampu berkedip")
    ketik("\nGelap.")
    ketik("....")
    ketik("\nIa terbangun di pulau asing.")
    ketik("terdengar debur ombak dan angin kencang.")
    ketik("\nhah, ini gue dimana?")
    ketik("gimana pun cara nya gue tetep harus hidup.")

stamina = 100
def tampil_stamina():
    print(f"stamina : {stamina}/100")
def kurang_stamina(jumlah):
    global stamina
    stamina -= jumlah
    if stamina <= 0:
        stamina = 0
        print("lau kecapean. tumbang")
        print("GAME OVER")
        exit()
hari =  1
def tampil_hari():
    print("\n" + "="*25)
    print(f"        HARI KE-{hari}")
    print("="*25 + "\n")
    time.sleep(1)

def next_hari():
    global hari
    hari +=1

nama = nama_player()
tampil_stamina()
inventory = []
KAPASITAS_MAX = 8 
prolog(nama) 
clear()
tampil_hari()
menu_aksi(nama)

def starting_item():
    tambah_item("Kapak", 1)
    tambah_item("Air Minum", 5)
    


KAPASITAS_MAX = 8
inventory = []

def lihat_inventory():
    print("\n=== INVENTORY ===")

    if not inventory:
        print("Inventory kosong!")
    else:
        for index, item in enumerate(inventory, start=1):
            print(f"{index}. {item}")

    print(f"Slot: {len(inventory)}/{KAPASITAS_MAX}")



def tambah_item(item):
    if not item.strip():
        return  

    if len(inventory) >= KAPASITAS_MAX:
        print("Inventory penuh!")
        return

    if item in inventory:
        print(f"{item} sudah ada!")
        return

    inventory.append(item)
    print(f"{item} ditambahkan!")



def hapus_item(item):
    if item not in inventory:
        print(f" {item} tidak ada!")
        return

    inventory.remove(item)
    print(f" {item} dihapus!")



tambah_item("")
tambah_item("")
tambah_item("")
lihat_inventory()
hapus_item("")
lihat_inventory()
