import os

def cls():
    if os.name == 'nt':  
        os.system('cls')  
    else:
        os.system('clear')  

def checkSortOptionValidity(sortOption):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
    'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
    if len(sortOption) == 0 or sortOption.count(" ") == len(sortOption):
        raise ValueError("Opsi tidak boleh kosong")
        
    for i in sortOption:
        if i not in letters:
            raise ValueError("Opsi hanya boleh berupa huruf")
    
    if sortOption not in ["id", "nama", "jenis", "harga"]:
        raise ValueError("Hanya tersedia opsi pengurutan berdasarkan Nama, NIM, dan jurusan")
    
    return True

class Stock:
    def __init__(self):
        self.storage = []
    
    def addToStorage(self, item):
        self.storage.append(item)
    
    def showStorage(self):
        print("Daftar Stock")
        print("="*30)
        
        stock_iter = iter(self.storage)
        try:
            while True:
                i = next(stock_iter)
                print(f"[ {i.id} ] [ {i.nama} ] [ Rp {i.harga} ]")
                print(f"Jumlah Stock: [ {i.stok} ]")
                history_iter = iter(i.history)
                try:
                    while True:
                        j = next(history_iter)
                        print(f"[ {j} ]", end=" ")
                        
                except StopIteration:
                    pass
                
                print()
                print()
        except StopIteration:
            pass
    
    def checkStock(self):
        stock_iter = iter(self.storage)
        try:
            while True:
                yield next(stock_iter)
                
        except StopIteration:
            pass

class Item:
    def __init__(self, id, nama, harga, jenis):
        self.id = id
        self.nama = nama
        self.harga = harga
        self.jenis = jenis
        self.stok = 0
        self.history = []
        
    def incStock(self, qty):
        self.stok += qty
        self.history.append(qty)
        
    def decStock(self, qty):
        if qty <= self.stok:
            self.stok -= qty
            self.history.append(-qty)
        else:
            print("Stok tidak mencukupi untuk pengurangan")

stockList = Stock()

while True:
    cls()
    print("Menu")
    print("=" * 30)
    print("1. Lihat daftar stock")
    print("2. Lihat stock yang hampir kosong")
    print("3. Tambah Barang")
    print("4. Kurangi Barang")
    print("5. Pengurutan data")
    print("6. Exit")
    
    op = int(input("Pilihan menu ( 1 / 2 / 3 / 4 / 5 / 6) : "))
    cls()
    if op == 1:
        stockList.showStorage()
    
    elif op == 2:
        limit = None
        while True:
            try:
                limit = int(input("Barang dengan jumlah berapakah yang ingin dilihat? "))
                if limit < 0:
                    raise ValueError("Nilai tidak boleh negatif")
                
                break

            except ValueError as err:
                print(f"Invalid input : {err}")

        stock_iter = iter(stockList.checkStock())
        try:
            while True:
                i = next(stock_iter)
                if i.stok <= limit:
                    print(f"[ {i.id} ] [ {i.nama} ] [ Rp {i.harga} ]")
                    print(f"Jumlah Stock: [ {i.stok} ]")
                    history_iter = iter(i.history)
                    try:
                        while True:
                            j = next(history_iter)
                            print(f"[ {j} ]", end=" ")
                    except StopIteration:
                        pass
                    print()
                    print()
        except StopIteration:
            pass
    
    elif op == 3:
        nama = str(input("Nama barang yang ingin ditambahkan : ")).lower()
        found = False
        
        stock_iter = iter(stockList.checkStock())
        try:
            while True:
                i = next(stock_iter)
                if i.nama == nama:
                    found = i
                    break
        except StopIteration:
            pass
        
        if not found:
            harga = int(input("Harga barang : "))
            qty = int(input("Stok awal barang : "))
            jenis = str(input("Jenis barang : "))
            item = Item(len(stockList.storage), nama, harga, jenis)
            item.incStock(qty)
            stockList.addToStorage(item)
        else:
            qty = int(input("Quantity : "))
            found.incStock(qty)
    
    elif op == 4:
        nama = str(input("Nama barang yang ingin dikurangi : ")).lower()
        found = False
        stock_iter = iter(stockList.checkStock())
        try:
            while True:
                i = next(stock_iter)
                if i.nama == nama:
                    found = i
                    break
                
        except StopIteration:
            pass
        
        if not found:
            print("Barang tidak ditemukan")
        else:
            qty = int(input("Quantity : "))
            found.decStock(qty)
    
    elif op == 5:
        sortOption = None
        sortOptionValid = False
        while not sortOptionValid:
            try:
                sortOption = str(input("Pengurutan berdasarkan : ")).lower()
                sortOptionValid = checkSortOptionValidity(sortOption)
            
            except ValueError as err:
                print(f"Invalid input : {err}")
        
        stockList.sortedBy(sortOption)
        stockList.showStorage()
    
    elif op == 6:
        break

    test = str(input("[ENTER] to continue"))
