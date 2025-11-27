Implementasi Sistem Universitas (Berdasarkan Class Diagram UML)

## 1. Tujuan Implementasi

Tujuan utama adalah untuk menciptakan model data Python yang secara akurat mereplikasi:
1.  **Struktur Pewarisan:** Hubungan **"is-a"** antara `Student` dan `Professor` dengan `Person`.
2.  **Hubungan Agregasi/Asosiasi:** Hubungan **"has-a"** antara `Person` dengan `Address` (1-ke-0..1) dan `Professor` dengan `Student` (1..5-ke-0..*).
3.  **Enkapsulasi:** Penggunaan konvensi Python untuk atribut *protected* (`#staffNumber`) dan *private/derived* (`/salary`).

---

## 2. Proses Pemetaan (Thinking Process)

### A. Kelas Dasar (Superclass) dan Hubungan

| UML Class | Hubungan | Pemetaan ke Python | Catatan Implementasi |
| :--- | :--- | :--- | :--- |
| **Address** | Dasar | `class Address:` | Kelas sederhana untuk menampung detail alamat. Metode `validate()` dan `outputAsLabel()` diimplementasikan sesuai diagram. |
| **Person** | Agregasi | `class Person:` | Kelas dasar. Memiliki atribut `lives_at: Address` dalam konstruktor untuk mewakili hubungan **Agregasi** (1 `Person` *lives at* 0..1 `Address`). |
| **Student** | Pewarisan | `class Student(Person):` | Mewarisi semua atribut dan metode dari `Person`. Menambahkan atribut spesifik (`studentNumber`, `averageMark`). |
| **Professor** | Pewarisan | `class Professor(Person):` | Mewarisi semua atribut dan metode dari `Person`. Menambahkan atribut spesifik. |

### B. Penanganan Atribut Khusus

| Atribut UML | Class | Konvensi Python | Penjelasan |
| :--- | :--- | :--- | :--- |
| `/salary: int` | Professor | `self._salary` dan `@property` | Simbol `/` menunjukkan atribut terderivasi atau *private*. Diimplementasikan sebagai properti baca-saja (`@property`) di Python. |
| `#staffNumber: int`| Professor | `self._staffNumber` | Simbol `#` menunjukkan atribut *protected*. Diimplementasikan dengan konvensi *underscore* tunggal (`_`). |
| `-validate(): bool`| Address | `def validate(self):` | Simbol `-` menunjukkan metode *private*. Namun, dalam Python murni, ini sering diimplementasikan sebagai metode publik atau dengan *underscore* ganda (`__`) untuk *name mangling*. Diputuskan menggunakan metode publik biasa karena sifatnya sebagai validasi data internal. |

### C. Penanganan Asosiasi (Supervises)

Hubungan antara `Professor` (multiplisitas **1..5**) dan `Student` (multiplisitas **0..\***) adalah kunci:

1.  **Pihak Profesor:** Kelas `Professor` membutuhkan atribut untuk menyimpan daftar `Student`.
    * **Kode:** `self.supervised_students: list[Student] = []`
2.  **Batasan Multiplisitas (1..5):** Batasan ini diimplementasikan dalam metode `addSupervisedStudent`.
    * **Kode:** Sebelum menambahkan `Student`, kode memeriksa `if len(self.supervised_students) < 5:`.

---

## 3. Hasil Implementasi Utama

#### Pewarisan
```python
class Student(Person):
    # ...
class Professor(Person):
    # ...
````

#### Agregasi (Person dan Address)

```python
class Person:
    def __init__(..., address: Address):
        self.lives_at: Address = address # Person 'has-a' Address
```

#### Asosiasi dengan Batasan (Professor dan Student)

```python
class Professor:
    def __init__(self, ...):
        self.supervised_students: list[Student] = []

    def addSupervisedStudent(self, student: Student) -> bool:
        # Logika pembatasan (maks 5 mahasiswa)
        if len(self.supervised_students) < 5:
            # ... tambahkan student
```

#### Atribut Protected/Derived

```python
class Professor:
    def __init__(..., salary: int, staffNumber: int, ...):
        self._salary: int = salary # /salary
        self._staffNumber: int = staffNumber # #staffNumber

    @property
    def salary(self) -> int:
        return self._salary
```
