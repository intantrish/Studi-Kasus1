# ==============================================================================
#                     IMPLEMENTASI CLASS DIAGRAM UNIVERSITAS
# ==============================================================================

class Address:
    """Representasi dari Alamat (Digunakan oleh Person)."""
    
    def __init__(self, street: str, city: str, state: str, postalCode: int, country: str):
        self.street: str = street
        self.city: str = city
        self.state: str = state
        self.postalCode: int = postalCode
        self.country: str = country

    def validate(self) -> bool:
        """Metode untuk memvalidasi alamat (placeholder)."""
        # Logika validasi yang sebenarnya akan lebih kompleks
        return bool(self.street and self.city and self.postalCode > 0)

    def outputAsLabel(self) -> str:
        """Mengeluarkan alamat dalam format label."""
        return f"{self.street}, {self.city}, {self.state}, {self.postalCode}, {self.country}"
    
    def __str__(self):
        return self.outputAsLabel()

class Person:
    """Class dasar (Superclass) untuk Person."""
    
    def __init__(self, name: str, phoneNumber: str, emailAddress: str, address: Address):
        self.name: str = name
        self.phoneNumber: str = phoneNumber
        self.emailAddress: str = emailAddress
        # Asosiasi 0..1 lives at 1
        self.lives_at: Address = address

    def purchaseParkingPass(self) -> None:
        """Metode untuk membeli izin parkir (placeholder)."""
        print(f"[{self.name}] telah membeli izin parkir.")

    def __str__(self):
        return (f"Nama: {self.name}, Email: {self.emailAddress}, "
                f"Alamat: {self.lives_at}")

class Student(Person):
    """Subclass Student, mewarisi dari Person."""
    
    def __init__(self, name: str, phoneNumber: str, emailAddress: str, address: Address, studentNumber: int, averageMark: int):
        # Memanggil konstruktor superclass
        super().__init__(name, phoneNumber, emailAddress, address)
        self.studentNumber: int = studentNumber
        self.averageMark: int = averageMark
        self._seminars_taken: list[str] = [] # List untuk menyimpan seminar

    def isEligibleToEnroll(self, required_mark: int) -> bool:
        """Memeriksa apakah mahasiswa memenuhi syarat untuk mendaftar."""
        return self.averageMark >= required_mark

    def getSeminarsTaken(self) -> list[str]:
        """Mengembalikan daftar seminar yang diambil."""
        return self._seminars_taken
    
    # Metode helper untuk mempermudah demo
    def addSeminar(self, seminar_name: str) -> None:
        self._seminars_taken.append(seminar_name)

    def __str__(self):
        base_info = super().__str__()
        return (f"Mahasiswa | {base_info}, NIM: {self.studentNumber}, "
                f"Rata-rata Nilai: {self.averageMark}")

class Professor(Person):
    """Subclass Professor, mewarisi dari Person."""
    
    def __init__(self, name: str, phoneNumber: str, emailAddress: str, address: Address, salary: int, staffNumber: int, yearsOfService: int, numberOfClasses: int):
        # Memanggil konstruktor superclass
        super().__init__(name, phoneNumber, emailAddress, address)
        self._salary: int = salary # Atribut private/protected: /salary
        self._staffNumber: int = staffNumber # Atribut protected: #staffNumber
        self.yearsOfService: int = yearsOfService
        self.numberOfClasses: int = numberOfClasses
        # Asosiasi 1..5 supervises 0..*
        self.supervised_students: list[Student] = []

    # Implementasi untuk atribut /salary: int
    @property
    def salary(self) -> int:
        return self._salary
    
    # Implementasi untuk atribut #staffNumber: int
    @property
    def staffNumber(self) -> int:
        return self._staffNumber

    def addSupervisedStudent(self, student: Student) -> bool:
        """Menambahkan mahasiswa yang diawasi, mematuhi batasan 1..5."""
        if len(self.supervised_students) < 5:
            self.supervised_students.append(student)
            return True
        else:
            print(f"GAGAL: Prof. {self.name} sudah mencapai batas pengawasan (5 mahasiswa).")
            return False

    def __str__(self):
        base_info = super().__str__()
        supervised_count = len(self.supervised_students)
        return (f"Professor | {base_info}, Staf No: {self.staffNumber}, "
                f"Gaji: {self.salary}, Kelas: {self.numberOfClasses}, "
                f"Mengawasi: {supervised_count} Mahasiswa")

# ==============================================================================
#                                ENTRY POINT (main)
# ==============================================================================

def main():
    print("--- DEMO IMPLEMENTASI CLASS DIAGRAM SISTEM UNIVERSITAS ---")

    # 1. Buat Objek Address
    addr_prof = Address("123 Ilmu Street", "Bandung", "Jawa Barat", 40000, "Indonesia")
    addr_stud = Address("456 Data Lane", "Jakarta", "DKI Jakarta", 10000, "Indonesia")
    
    print("\n[A] Alamat & Validasi")
    print(f"Alamat Professor: {addr_prof.outputAsLabel()}")
    print(f"Alamat Valid? {addr_prof.validate()}")

    # 2. Buat Objek Professor (Memenuhi Asosiasi 1..5)
    prof = Professor(
        name="Dr. Budi Santoso", 
        phoneNumber="0811223344", 
        emailAddress="budi.santoso@uni.ac.id", 
        address=addr_prof,
        salary=15000000, 
        staffNumber=5001, 
        yearsOfService=10, 
        numberOfClasses=3
    )

    # 3. Buat Objek Student (Mewarisi Person)
    student1 = Student(
        name="Ani Wijaya", 
        phoneNumber="0855667788", 
        emailAddress="ani.wijaya@std.uni.ac.id", 
        address=addr_stud,
        studentNumber=190101, 
        averageMark=85
    )
    student2 = Student("Bima Sakti", "0899887766", "bima.sakti@std.uni.ac.id", addr_stud, 190102, 72)
    student1.addSeminar("Machine Learning")

    print("\n[B] Data Person dan Mahasiswa")
    print(prof)
    print(student1)
    print(f"Seminar Ani: {student1.getSeminarsTaken()}")
    print(f"Ani eligible to enroll (min 80)? {student1.isEligibleToEnroll(80)}")
    
    # 4. Demonstrasi Asosiasi Professor supervises Student
    print("\n[C] Demonstrasi Supervisi")
    prof.addSupervisedStudent(student1)
    prof.addSupervisedStudent(student2)
    prof.purchaseParkingPass()

    print("\n[D] Status Akhir Professor")
    print(prof)

if __name__ == "__main__":
    main()
```
