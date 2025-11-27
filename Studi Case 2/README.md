# Implementasi Sistem Perpustakaan (Berdasarkan Class Diagram UML)

Dokumen ini menjelaskan proses pemetaan dan implementasi struktur kelas dari *Class Diagram* UML Sistem Perpustakaan menjadi kode Python. Fokus utamanya adalah pada replikasi hubungan **Pewarisan** dan **Asosiasi** yang kompleks.

## 1. Tujuan Implementasi

Tujuan utama implementasi ini adalah menciptakan model Python yang mencerminkan:
1.  **Pewarisan (Inheritance):** Hubungan **"is-a"** di mana `Book` adalah jenis `LibraryItem`.
2.  **Asosiasi:** Hubungan **"has-a"** antara `Book` dengan `Author` (1-ke-1) dan `LibraryMember` dengan `LibraryItem` (1-ke-0..\*).
3.  **Polymorphism:** Metode yang sama (`display_info`, `calculate_late_fee`) digunakan di *superclass* (`LibraryItem`) dan di-*override* atau diwariskan oleh *subclass* (`Book`).

---

## 2. Proses Pemetaan (Thinking Process)

### A. Pewarisan (Inheritance)

| UML Class | Hubungan | Pemetaan ke Python | Catatan Implementasi |
| :--- | :--- | :--- | :--- |
| **LibraryItem** | Superclass | `class LibraryItem:` | Kelas dasar yang mendefinisikan atribut umum (ID, *title*) dan perilaku umum (menghitung denda). |
| **Book** | Subclass | `class Book(LibraryItem):` | Mewarisi atribut `item_id` dan `title`. Menambahkan atribut spesifik (`isbn`). Metode `display_info()` di-*override* untuk menyertakan detail spesifik buku. |

### B. Hubungan Asosiasi

| Hubungan UML | Kelas Pemilik | Tipe Data Atribut | Penjelasan Kode |
| :--- | :--- | :--- | :--- |
| **Book $\rightarrow$ Author** (1-ke-1) | `Book` | `self.author: Author` | Setiap objek `Book` menerima dan menyimpan satu objek `Author` dalam konstruktornya, mereplikasi hubungan komposisi/agregasi. |
| **LibraryMember $\rightarrow$ LibraryItem** (0..\* ) | `LibraryMember` | `self.borrowed_items: list[LibraryItem]` | Objek `LibraryMember` menyimpan daftar (`list`) dari objek `LibraryItem` (atau subclass-nya, seperti `Book`). |

### C. Penanganan Metode Kunci

| Metode UML | Class | Implementasi Python | Fungsi |
| :--- | :--- | :--- | :--- |
| `get_age()` | `Author` | `def get_age(self, current_year: int) -> int:` | Menggunakan modul `datetime` atau variabel tahun eksternal untuk menghitung usia penulis, sesuai parameter diagram. |
| `calculate_late_fee()`| `LibraryItem` | `def calculate_late_fee(self, days_late: int) -> float:` | Logika perhitungan denda ditetapkan di *superclass* dan diwariskan oleh semua item. |
| `borrow_item()` / `return_item()` | `LibraryMember` | `def borrow_item(self, item: LibraryItem)` | Memanipulasi (`append`/`remove`) list `self.borrowed_items` untuk merefleksikan perubahan status pinjaman anggota. |

---

## 3. Hasil Implementasi Utama

#### Pewarisan
```python
class Book(LibraryItem):
    # ... mendapatkan item_id dan title dari super()
    def display_info(self) -> None:
        # Override metode untuk menampilkan detail ISBN dan Author
````

#### Asosiasi (LibraryMember dan LibraryItem)

```python
class LibraryMember:
    def __init__(self, ...):
        self.borrowed_items: list[LibraryItem] = [] 

    def borrow_item(self, item: LibraryItem) -> None:
        self.borrowed_items.append(item)
```
