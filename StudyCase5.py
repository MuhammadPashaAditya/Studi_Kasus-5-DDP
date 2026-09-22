from datetime import datetime

# Function untuk menghitung biaya hotel
def hitung_biaya(jenis_kamar, lama_menginap):
    if jenis_kamar == "Standard":
        tarif = 200000
    elif jenis_kamar == "Deluxe":
        tarif = 350000
    else:
        return 0

    total_biaya = tarif * lama_menginap
    return total_biaya

# Input data pemesanan
jenis_kamar = input("Masukkan jenis kamar (Standard/Deluxe): ").strip().title()
tanggal_check_in = input("Masukkan tanggal check-in (DD MM YYYY): ")
tanggal_check_out = input("Masukkan tanggal check-out (DD MM YYYY): ")

# Mengubah tanggal menjadi format datetime
check_in = datetime.strptime(tanggal_check_in, "%d %m %Y")
check_out = datetime.strptime(tanggal_check_out, "%d %m %Y")

# Menghitung lama menginap
lama_menginap = (check_out - check_in).days

# Function
total_biaya = hitung_biaya(jenis_kamar, lama_menginap)

print("\n ===== DETAIL PEMESANAN HOTEL =====")
print("Jenis kamar         :", jenis_kamar)
print("Tanggal Check-in    :", tanggal_check_in)
print("Tanggal Check-out   :", tanggal_check_out)
print("Lama menginap       :", lama_menginap,"malam")
print("Total Biaya         : Rp{:,.0f}".format(total_biaya))