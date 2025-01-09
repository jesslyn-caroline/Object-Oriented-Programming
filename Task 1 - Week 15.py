import os
# from prettytable import PrettyTable

def cls():
    if os.name == 'nt': _ = os.system('cls')
    else: _ = os.system('clear')

### ==== Start of Input Handle ==== ###

def checkNipValidity(kode):
    if len(kode) == 0 or kode.count(" ") == len(kode):
        raise ValueError("Kode tidak boleh kosong")

    if len(kode) != 9:
        raise ValueError("Kode harus memiliki 9 angka")

    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for i in kode:
        if i not in num:
            raise ValueError(f"Kode hanya boleh berupa angka")

    return True

def checkCodeValidity(kode):
    if len(kode) == 0 or kode.count(" ") == len(kode):
        raise ValueError("Kode tidak boleh kosong")

    if len(kode) != 9:
        raise ValueError("Kode harus memiliki 9 angka")

    if int(kode[0:2]) > 24:
        raise ValueError("Kode tahun angkatan tidak valid")

    if kode[2:5] not in ["111", "112", "113", "211", "212"]:
        raise ValueError(f"Kode jurusan tidak valid")

    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for i in kode:
        if i not in num:
            raise ValueError(f"Kode hanya boleh berupa angka")

    return True

def checkNameValidity(nama):
    nama = nama.lower()
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
    'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    if len(nama) == 0 or nama.count(" ") == len(nama):
        raise ValueError("Nama tidak boleh kosong")

    for i in nama:
        if i not in letters and i != " ":
            raise ValueError("Nama hanya boleh berupa huruf dan spasi")

    return True

def checkGenderValidity (jenisKelamin):
    jenisKelamin = jenisKelamin.upper()
    if len(jenisKelamin) == 0 or jenisKelamin.count(" ") == len(jenisKelamin):
        raise ValueError("Jenis Kelamin tidak boleh kosong")

    if jenisKelamin != 'L' and jenisKelamin != 'P':
        raise ValueError("Jenis kelamin hanya boleh berupa P atau L")

    return True

def checkPhoneNumValidity (nomorHp):
    if len(nomorHp) == 0 or nomorHp.count(" ") == len(nomorHp):
        raise ValueError("Nomor HP tidak boleh kosong")

    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    if nomorHp[0] != '+':
        raise ValueError("Nomor HP harus berawal dengan tanda '+'")

    nomorHpLength = len(nomorHp)
    if nomorHpLength < 8 or nomorHpLength > 15:
        raise ValueError("Nomor HP hanya boleh terdiri dari 8 - 12 karakter")

    for i in range (1, nomorHpLength):
        if nomorHp[i] not in num and nomorHp[i] != " ":
            raise ValueError("Nomor HP hanya boleh terdiri dari nomor dan spasi")

    return True

def checkClassValidity(kelas):
    kelas = kelas.upper()
    if len(kelas) == 0 or kelas.count(" ") == len(kelas):
        raise ValueError("Kelas tidak boleh kosong")

    if kelas != "A" and kelas != "B" and kelas != "C":
        raise ValueError("Kelas hanya ada A / B / C")

    return True

def checkTimeValidity(jam):
    jam = jam.lower()
    if len(jam) == 0 or jam.count(" ") == len(jam):
        raise ValueError("Jam tidak boleh kosong")

    if jam != "sore" and jam != "pagi":
        raise ValueError("Hanya tersedia opsi Pagi dan Sore")

    return True

### ==== End of Input Handle ==== ###


### ==== Start of Mhs Dsn Class ==== ###

class Parent:
    def __init__ (self, nama, nomorHp, jenisKelamin, As):
        self.nama = nama
        self.nomorHp = nomorHp
        self.jenisKelamin = jenisKelamin
        self.As = As

class Mhs (Parent):
    def __init__ (self, nim, nama, kelas, jam, nomorHp, jenisKelamin):
        super().__init__ (nama, nomorHp, jenisKelamin, 'mhs')
        self.nim = nim
        self.kelas = kelas
        self.jam = jam
        self.jurusan = 'IF' if nim[2:5] == '111' else 'TI' if nim[2:5] == '112' else 'SI' if nim[2:5] == '113' else 'MN' if nim[2:5] == '211' else 'AK'
    
    def row (self):
        return [self.nim, self.nama, self.kelas, self.jam, self.nomorHp, self.jenisKelamin, self.jurusan]
    
class Dsn (Parent):
    def __init__ (self, nip, nama, jabatan, nomorHp, jenisKelamin):
        super().__init__ (nama, nomorHp, jenisKelamin, 'dsn')
        self.nip = nip
        self.jabatan = jabatan
    
    def row (self):
        return [self.nip, self.nama, self.jabatan, self.nomorHp, self.jenisKelamin]

### ==== End of Mhs Dsn Class ==== ###


### ==== Start of Mhs Dsn List Class ==== ###
class ParentList:
    def __init__ (self):
        self.lst = []
    
    def length (self):
        return len(self.lst)
    
    def addToList (self, data):
        self.lst.append(data);
    
    def searchByName (self, name):
        found = []
        for i in self.lst:
            if i.name == name:
                return found
        
        return False
    
    def getList (self):
        pass
    
class MhsList(ParentList):
    def __init__ (self):
        super().__init__()
    
    def searchByNim (self, nim):
        for i in self.lst:
            if i.nim == nim:
                return True
        
        return False
    
    def getList (self):
        tableMhs = PrettyTable()
        tableMhs.field_names = ["NIM", "Nama", "Kelas", "Jam", "Nomor HP", "Jenis Kelamin", "Jurusan"]
        for i in self.mhs:
            tableMhs.add_row(i.row())

class DsnList(ParentList):
    def __init__ (self):
        super().__init__()
    
    def searchByNip (self, nip):
        for i in self.lst:
            if i.nip == nip:
                return True
        
        return False
    
    def getList (self):
        tableDsn = PrettyTable()
        tableDsn.field_names = ["NIP", "Nama", "Jabatan", "Nomor HP", "Jenis Kelamin"]
        for i in self.dsn:
            tableDsn.add_row(i.row())


class AllList:
    def __init__ (self):
        self.mhs = MhsList()
        self.dsn = DsnList()
    
    def addMhs (self, data):
        self.mhs.addToList(data)
    
    def addDsn (self, data):
        self.dsn.addToList(data)
    
    def searchByNip (self, nip):
        return self.dsn.searchByNip(nip)
    
    def searchByNim (self, nim):
        return self.mhs.searchByNim(nim)
        
    def searchByNameDsn (self, name):
        return self.dsn.searchByNameDsn(name)
    
    def searchByNameMhs (self, name):
        return self.mhs.searchByNameMhs(name)
    
    def getList (self):
        self.mhs.getList()
        print()
        self.dsn.getList()
        
        mhsLen = self.mhs.length()
        dsnLen = self.dsn.length()
        
        print(f'Total Mahasiswa yang hadir: {mhsLen}')
        print(f'Total Dosen yang hadir: {dsnLen}')
        print(f'Total kehadiran: {mhsLen + dsnLen}')

### ==== End of Mhs Dsn List Class ==== ###

### ==== Start of Single Responsibility Principle ==== ###

def mainMenu():
    print('Menu')
    print('-' * 50)
    print('1. Lihat daftar kehadiran')
    print('2. Tambah pengunjung')
    print('3. Mencari pengunjung')
    print('4. Exit')
    print('-' * 50)

def visitorList():
    lst.getList()

def addVisitor():
    print('Tambah pengunjung')
    print('-' * 50)
    print('1. Mahasiswa')
    print('2. Dosen')
    print('-' * 50)

    option = inputOption_two()

    if option == '1': 
        pos = addVisitorMhs()
        if pos: print("Mahasiswa tersebut telah ditambahkan")
        else: print("Mahasiswa tersebut telah terdaftar sebelumnya")

    elif option == '2': 
        pos = addVisitorDsn()
        if pos: print("Dosen tersebut telah ditambahkan")
        else: print("Dosen tersebut telah terdaftar sebelumnya")

def inputOption_two():
    optionValid = False
    while not optionValid:
        try:
            op = input('Pilihan opsi ( 1 / 2 ): ')

            if len(op) == op.count(" "): raise ValueError('Opsi tidak boleh kosong')
            if not op.isnumeric(): raise ValueError('Opsi harus berupa angka')
            if op not in ['1', '2']: raise ValueError('Opsi yang tersedia hanya 1 / 2')

            optionValid = True

        except ValueError as err:
            print(f'Invalid Input: {err}')

    return op

def inputOption_four():
    optionValid = False
    while not optionValid:
        try:
            op = input("Pilihan menu ( 1 / 2 / 3 / 4 ): ")
            if len(op) == op.count(" "): raise ValueError('Opsi tidak boleh kosong')
            if not op.isnumeric(): raise ValueError('Opsi harus berupa angka')
            if op not in ['1', '2', '3', '4']: raise ValueError('Opsi yang tersedia hanya 1 / 2 / 3 / 4')

            optionValid = True

        except ValueError as err:
            print(f'Invalid Input: {err}')

    return op

def inputHandle(neededData, handleFunction):
    valid = False
    while not valid:
        try:
            data = input(f"{neededData}: ")
            valid = handleFunction(data)

        except ValueError as err:
            print(f'Invalid Input: {err}')

    return data

def addVisitorMhs():
    nim = inputHandle("NIM", checkCodeValidity)
    nama = inputHandle("Nama", checkNameValidity)
    jenisKelamin = inputHandle("Jenis Kelamin", checkGenderValidity)
    nomorHp = inputHandle("Nomor HP", checkPhoneNumValidity)
    kelas = inputHandle("Kelas", checkClassValidity)
    jam = inputHandle("Jam", checkTimeValidity)

    nama = nama.lower()
    jenisKelamin = jenisKelamin.upper()
    kelas = kelas.upper()
    jam = jam.lower()

    found = lst.searchByNim(nim)
    if not found:
        mhs = Mhs(nim, nama, jenisKelamin, nomorHp, kelas, jam)
        lst.addMhs(mhs)
        return True

    else: return False

def addVisitorDsn():
    nip = inputHandle("NIP", checkCodeValidity)
    nama = inputHandle("Nama", checkNameValidity)
    jenisKelamin = inputHandle("Jenis Kelamin", checkGenderValidity)
    nomorHp = inputHandle("Nomor HP", checkPhoneNumValidity)
    jabatan = input("Jabatan: ")

    nama = nama.lower()
    jenisKelamin = jenisKelamin.upper()

    found = lst.searchByNip(nip)
    if not found:
        dsn = Dsn(nip, nama, jabatan, nomorHp, jenisKelamin)
        lst.addDsn(dsn)
        return True

    else: return False

def searchVisitor():
    print('Mencari pengunjung')
    print('-' * 50)
    print('1. Mahasiswa')
    print('2. Dosen')
    print('-' * 50)

    option = inputOption_two()

    print()
    print('-' * 50)
    print('1. NIM / NIP')
    print('2. Nama')
    print('-' * 50)
    print()

    if option == '1':
        searchBy = inputOption_two()

        if searchBy == '1': 
            found = searchByNim()
            if found: print('Mahasiswa tersebut ditemukan di dalam daftar')
            else: print('Mahasiswa tersebut tidak terdaftar')

        elif searchBy == '2': 
            found = searchByNameMhs()

            if found: 
                table = PrettyTable()
                table.field_names = ["NIM", "Nama", "Kelas", "Jam", "Nomor HP", "Jenis Kelamin", "Jurusan"]
                for i in found:
                    table.add_row(i.row())

                print(table)

            else: print('Mahasiswa tersebut tidak terdaftar')

    elif option == '2':
        searchBy = inputOption_two()

        if searchBy == '1': 
            found = searchByNip()
            if found: print('Dosen tersebut ditemukan di dalam daftar')
            else: print('Dosen tersebut tidak terdaftar')

        elif searchBy == '2': 
            if found: 
                table = PrettyTable()
                table.field_names = ["NIP", "Nama", "Jabatan", "Nomor HP", "Jenis Kelamin"]
                for i in found:
                    table.add_row(i.row())

                print(table)

            else: print('Dosen tersebut tidak terdaftar')

def searchByNim():
    nim = inputHandle("NIM", checkCodeValidity)

    found = lst.searchByNim(nim)
    return found

def searchByNameMhs():
    nama = inputHandle("Nama", checkNameValidity)
    nama = nama.lower()

    found = lst.searchByNameMhs(nama)
    return found

def searchByNip():
    nip = inputHandle("NIP", checkCodeValidity)

    found = lst.searchByNip(nip)
    return found

def searchByNameDsn():
    nama = inputHandle("Nama", checkNameValidity)
    nama = nama.lower()

    found = lst.searchByNameDsn(nama)
    return found

### ==== End of Single Responsibility Principle ==== ###


### ==== Main Program ==== ###

if __name__ == '__main__':
    lst = AllList()

    while True:
        cls()
        mainMenu()

        op = inputOption_four()
        cls()

        if op == '1': visitorList()
        elif op == '2': addVisitor()
        elif op == '3': searchVisitor()
        elif op == '4':
            print("Thank you")
            break

        print()
        print()
        input("Any button to continue")
