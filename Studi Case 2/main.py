import datetime
#IMPLEMENTASI CLASS DIAGRAM PERPUSTAKAAN

class Author:
    "Representasi dari Penulis."
    
    def __init__(self, name: str, birth_year: int):
        self.name: str = name
        self.birth_year: int = birth_year

    def get_age(self, current_year: int) -> int:
        """Menghitung usia penulis berdasarkan tahun saat ini."""
        return current_year - self.birth_year
    
    def __str__(self):
        return f"Penulis: {self.name}, Lahir: {self.birth_year}"

class LibraryItem:
    "Class dasar (Superclass) untuk semua item di perpustakaan."
    
    def __init__(self, item_id: int, title: str):
        self.item_id: int = item_id
        self.title: str = title
        self.late_fee_per_day = 5000 # Contoh denda per hari (Rp 5000)

    def display_info(self) -> None:
        """Menampilkan informasi dasar item (abstrak)."""
        # Metode ini akan di-override di subclass, tapi didefinisikan di sini
        print(f"ID Item: {self.item_id}, Judul: {self.title}")

    def calculate_late_fee(self, days_late: int) -> float:
        """Menghitung denda keterlambatan."""
        if days_late <= 0:
            return 0.0
        return float(days_late * self.late_fee_per_day)

    def __str__(self):
        return f"Item Perpustakaan: {self.title} (ID: {self.item_id})"

class Book(LibraryItem):
    "Subclass Book, mewarisi dari LibraryItem."
    
    def __init__(self, item_id: int, title: str, isbn: str, author: Author):
        # Memanggil konstruktor superclass
        super().__init__(item_id, title) 
        self.isbn: str = isbn
        # Asosiasi Book terhubung ke Author
        self.author: Author = author 

    def display_info(self) -> None:
        """Menampilkan informasi buku secara lengkap (override dari LibraryItem)."""
        print("-" * 30)
        print(f"Jenis: Buku | ID: {self.item_id}")
        print(f"Judul: {self.title}")
        print(f"ISBN: {self.isbn}")
        print(f"Penulis: {self.author.name}")
        print("-" * 30)

    # Metode calculate_late_fee() diwarisi dari LibraryItem

class LibraryMember:
    "Representasi Anggota Perpustakaan."
    
    def __init__(self, member_id: int, name: str):
        self.member_id: int = member_id
        self.name: str = name
        # Atribut borrowed_items: List yang menampung objek LibraryItem
        self.borrowed_items: list[LibraryItem] = [] 

    def borrow_item(self, item: LibraryItem) -> None:
        """Anggota meminjam sebuah item."""
        if item not in self.borrowed_items:
            self.borrowed_items.append(item)
            print(f"-> {self.name} berhasil meminjam '{item.title}'")
        else:
            print(f"-> GAGAL: '{item.title}' sudah dipinjam oleh {self.name}")

    def return_item(self, item: LibraryItem) -> None:
        """Anggota mengembalikan sebuah item."""
        if item in self.borrowed_items:
            self.borrowed_items.remove(item)
            print(f"-> {self.name} berhasil mengembalikan '{item.title}'")
        else:
            print(f"-> GAGAL: '{item.title}' tidak ditemukan dalam daftar pinjaman {self.name}")

    def __str__(self):
        titles = [item.title for item in self.borrowed_items]
        return (f"Anggota: {self.name} (ID: {self.member_id}), "
                f"Dipinjam ({len(self.borrowed_items)}): {', '.join(titles) if titles else 'Tidak ada'}")

#ENTRY POINT (main)

def main():
    print("--- DEMO IMPLEMENTASI CLASS DIAGRAM SISTEM PERPUSTAKAAN ---")
    current_year = datetime.date.today().year

    # 1. Buat Objek Author
    author1 = Author(name="Andrea Hirata", birth_year=1962)
    print(f"\n[A] Informasi Penulis")
    print(author1)
    print(f"Usia penulis: {author1.get_age(current_year)} tahun")

    # 2. Buat Objek Book (mewarisi LibraryItem)
    book1 = Book(
        item_id=101, 
        title="Laskar Pelangi", 
        isbn="978-9799-7973-1-3", 
        author=author1
    )
    
    # 3. Demonstrasi Pewarisan dan Polymorphism
    print("\n[B] Informasi Buku (Menggunakan display_info)")
    book1.display_info()

    # 4. Buat Objek LibraryMember
    member1 = LibraryMember(member_id=2001, name="Dewi Sartika")
    
    # 5. Demonstrasi Peminjaman, Pengembalian, dan Denda
    print("\n[C] Aksi Peminjaman dan Pengembalian")
    
    # Pinjam Item
    print(f"Status Awal: {member1}")
    member1.borrow_item(book1)
    print(f"Status Setelah Pinjam: {member1}")
    
    # Perhitungan Denda
    days_late = 12
    fee = book1.calculate_late_fee(days_late)
    print(f"\nItem '{book1.title}' terlambat {days_late} hari.")
    print(f"Denda yang dihitung: Rp {fee:,.0f}")
    
    # Kembalikan Item
    member1.return_item(book1)
    print(f"Status Setelah Kembali: {member1}")

if __name__ == "__main__":
    main()
