class Barang:
    def __init__(self, kode, nama, harga):
        self.kode = kode
        self.nama = nama
        self.harga = harga

    def __str__(self):
        return f"{self.kode} | {self.nama} | {self.harga}"

class Keranjang:
    def __init__(self):
        self.barang_list = []
    
    def tambah_barang(self, barang, jumlah):
        """Menambahkan barang ke dalam keranjang"""
        for b in self.barang_list:
            if b['barang'].kode == barang.kode:
                b['jumlah'] += jumlah
                return
        self.barang_list.append({'barang': barang, 'jumlah': jumlah})
    
    def tampilkan_barang(self):
        """Menampilkan daftar barang dalam keranjang"""
        if not self.barang_list:
            print("Keranjang kosong.")
        else:
            print("Daftar Barang dalam Keranjang:")
            print(f"{'Kode':<10} {'Nama':<20} {'Harga':<10} {'Jumlah':<10}")
            for b in self.barang_list:
                barang = b['barang']
                print(f"{barang.kode:<10} {barang.nama:<20} {barang.harga:<10} {b['jumlah']:<10}")
    
    def hitung_total(self):
        """Menghitung total harga keranjang"""
        total = 0
        for b in self.barang_list:
            total += b['barang'].harga * b['jumlah']
        return total
    
    def cetak_struk(self):
        """Mencetak struk belanja"""
        print("\n==== STRUK BELANJA ====")
        for b in self.barang_list:
            barang = b['barang']
            total_harga = barang.harga * b['jumlah']
            print(f"{barang.nama:<20} x {b['jumlah']} = {total_harga}")
        print(f"\nTotal: {self.hitung_total()}")
        print("=======================")

def tampilkan_menu(barang_list):
    """Menampilkan daftar barang yang tersedia"""
    print("\nDaftar Barang yang Tersedia:")
    print(f"{'Kode':<10} {'Nama':<20} {'Harga':<10}")
    for barang in barang_list:
        print(f"{barang.kode:<10} {barang.nama:<20} {barang.harga:<10}")

def main():
    barang1 = Barang(kode="01", nama="aqua 1,5liter", harga=5000)
    barang2 = Barang(kode="02", nama="vit 1,5liter", harga=6000)
    barang3 = Barang(kode="03", nama="roti aoka", harga=4000)
    barang4 = Barang(kode="04", nama="indomie original", harga=3000)
    barang5 = Barang(kode="05", nama="indomie rendang", harga=3500)
    barang6 = Barang(kode="06", nama="permen yupi", harga=1000)
    barang7 = Barang(kode="07", nama="susu ultramilk", harga=5000)
    barang8 = Barang(kode="08", nama="susu beruang", harga=8000)
    barang9 = Barang(kode="09", nama="kopi golda", harga=3500)
    barang10 = Barang(kode="010", nama="telor", harga=2000)
    barang11 = Barang(kode="011", nama="pop mie", harga=6000)
    
    barang_list = [barang1, barang2, barang3, barang4, barang5, barang6, barang7, barang8, barang9, barang10, barang11]

    keranjang = Keranjang()

    while True:
        tampilkan_menu(barang_list)
        
        kode_barang = input("\nMasukkan kode barang yang ingin dibeli (atau 'exit' untuk keluar): ")
        
        if kode_barang.lower() == 'exit':
            break
        
        barang_terpilih = None
        for barang in barang_list:
            if barang.kode == kode_barang:
                barang_terpilih = barang
                break
        
        if barang_terpilih is None:
            print("Kode barang tidak ditemukan, coba lagi.")
            continue
        
        try:
            jumlah = int(input(f"Masukkan jumlah {barang_terpilih.nama} yang ingin dibeli: "))
            if jumlah <= 0:
                print("Jumlah barang harus lebih dari 0.")
                continue
        except ValueError:
            print("Jumlah yang dimasukkan tidak valid, coba lagi.")
            continue

        keranjang.tambah_barang(barang_terpilih, jumlah)

        lanjut = input("Apakah Anda ingin menambah barang lain? (y/t): ")
        if lanjut.lower() != 'y':
            break
    
    keranjang.tampilkan_barang()

    total = keranjang.hitung_total()
    print(f"\nTotal Harga: {total}")

    keranjang.cetak_struk()

if __name__ == "__main__":
    main()