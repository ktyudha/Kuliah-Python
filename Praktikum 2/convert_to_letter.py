# convert_to_letter.py

def number_to_letter(number):
    if not isinstance(number, (int, float)):
        raise ValueError("Input harus berupa angka (int atau float)")
    
    if 0 <= number <= 100:
        if number >= 81:
            return 'A'
        elif number >= 71:
            return 'AB'
        elif number >= 66:
            return 'B'
        elif number >= 61:
            return 'BC'
        elif number >= 56:
            return 'C'
        elif number >= 41:
            return 'D'
        else:
            return 'E'
    else:
        raise ValueError("Nilai angka harus berada dalam rentang 0 hingga 100")
