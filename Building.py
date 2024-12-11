# Building a Guessing game
nomor_rahasia = 9
hitung_tebakan = 0
max_tebakan = 3
while hitung_tebakan < max_tebakan:
    tebakan = int(input('tebak: '))
    hitung_tebakan += 1
    if tebakan == nomor_rahasia:
        print('Kamu benar')
        break
    else:
        print('Maaf, kamu gagal')

# Building the Car Game
command = ""
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        print("Car Started....")
    elif command == "stop":
        print("Car Stopped.")
    elif command == "help":
        print("""
              start - menyalakan mobil
              stop - menghentikan mobil
              quit - to quit
              """)
    elif command == "quit":
        break
    else:
        print("Maaf, saya tidak mengerti")