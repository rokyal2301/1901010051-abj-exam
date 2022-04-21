while True:
    tanya=input("Input Data Inventory Baru (Ya/Tidak)? ")
    if tanya == "ya" or tanya == "Ya":
        file = open ("db-inventory.txt", "a")
        print("*"*40)
        nama_perangkat = input("Nama Perangkat : ")
        Lokasi = input("Lokasi : ")
        print("-"*40)
        file.write("Nama Perangkat : " + nama_perangkat +", \t Lokasi : " + Lokasi +"\n" )
        file.close()
    elif tanya == "tidak" or tanya == "Tidak" :
        file = open ("db-inventory.txt", "r")
        print("*"*40)    
        for item in file:
            item = item.strip()
            print(item)
        break