from datetime import date

my_family = {
    "Claudia Sibila Z.": date(1959, 6, 6),
    "Alfredo Arnaiz F.C.": date(1963, 6, 13),
    "Alfredo Arnaiz S.": date(1990, 11, 29),
    "Camila Arnaiz S.": date(1993, 10, 8),
}


def calculate_days():
    while True:
        f_member = input("Enter a member family name: ").strip()

        if not f_member:
            break
        
        if f_member in my_family:
            age_in_days = (date.today() - my_family[f_member]).days
            print(f'{f_member} is {age_in_days} days old')
        else:
            print(f'{f_member} is not in the family')
