#Project_8_Roman_To_Decimal_Converter

a = input("What is your name ? ")
print(f"Welcome {a} to Let's Help You to Convert Roman to Decimal")
print("...........................................................")

t = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def romantodecimal(num):
    sum = 0
    for i in range(len(num) - 1):
        left = num[i]
        right = num[i + 1]
        if t[left] < t[right]:
            sum -= t[left]
        else:
            sum += t[left]

    sum += t[num[-1]]
    return sum

roman = input("Enter Roman Number: ")
print(f"The Decimal Number of {roman} is", romantodecimal(roman))
