expenses = []
months = {
    1: "Styczeń",
    2: "Luty",
    3: "Marzec",
    4: "Kwiecień",
    5: "Maj",
    6: "Czerwiec",
    7: "Lipiec",
    8: "Sierpień",
    9: "Wrzesień",
    10: "Październik",
    11: "Listopad",
    12: "Grudzień",
}


def show_expenses(month):
    for expense_amount, expense_type, expense_month in expenses:
        if expense_month == month:
            print()
            print(expense_month)
            print(f"{expense_amount} zł - {expense_type}")


def add_expense(month):
    print()
    expense_amount = float(input("Podaj kwotę [zł]: "))
    expense_type = input("Podaj opis wydatku: ")
    expense = (
        expense_amount,
        expense_type,
        month,
    )
    expenses.append(expense)


while True:
    try:
        month = int(input("Wybierz miesiąc [1-12]: "))
        if month < 1 or month > 12:
            print("ZŁY ZNAK")
            break
        else:
            month = months[month]
    except ValueError:
        print("ZŁY ZNAK")
        break

    while True:
        try:
            print()
            print("1.Dodaj wydatek")
            print("2.Pokaż wydatki")
            print("3.Powrót do wyboru miesiąca")
            choice = int(input("Wybierz opcję: "))
        except ValueError:
            print("WYBIERZ NUMER")
        if choice == 1:
            add_expense(month)
        if choice == 2:
            show_expenses(month)
        if choice == 3:
            break
