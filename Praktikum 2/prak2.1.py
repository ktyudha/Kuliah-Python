# main_script.py
from convert_to_letter import number_to_letter

def main():
    try:
        nilai_angka = float(input("Masukkan nilai angka: "))
        nilai_huruf = number_to_letter(nilai_angka)
        print(f"Nilai huruf: {nilai_huruf}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
