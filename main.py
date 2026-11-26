
# Progressive Electricity Billing System

FIXED_CHARGE = 50
SURCHARGE_RATE = 0.05
REBATE_RATE = 0.10
REBATE_LIMIT = 100
INCREASE_LIMIT = 30


def calculate_energy_charge(units):
    charge = 0

    if units <= 100:
        charge = units * 2

    elif units <= 200:
        charge = (100 * 2) + ((units - 100) * 3)

    elif units <= 300:
        charge = (100 * 2) + (100 * 3) + ((units - 200) * 5)

    else:
        charge = (100 * 2) + (100 * 3) + (100 * 5) + ((units - 300) * 7)

    return charge


def calculate_bill(units):
    energy_charge = calculate_energy_charge(units)

    fixed_charge = FIXED_CHARGE
    surcharge = energy_charge * SURCHARGE_RATE

    if units <= REBATE_LIMIT:
        rebate = energy_charge * REBATE_RATE
    else:
        rebate = 0

    total_bill = (
        energy_charge
        + fixed_charge
        + surcharge
        - rebate
    )

    return total_bill, energy_charge, surcharge, rebate


def main():
    months = []
    bills = []

    n = int(input("Enter number of months: "))

    for i in range(n):
        print("\nMonth", i + 1)

        month = input("Enter month name: ")
        units = float(input("Enter electricity units consumed: "))

        if units < 0:
            print("Invalid units!")
            return

        total, energy, surcharge, rebate = calculate_bill(units)

        months.append(month)
        bills.append(total)

        print("\n----- ELECTRICITY BILL -----")
        print("Month:", month)
        print("Units consumed:", units)
        print("Energy charge: Rs.", round(energy, 2))
        print("Fixed charge: Rs.", FIXED_CHARGE)
        print("Surcharge: Rs.", round(surcharge, 2))
        print("Rebate: Rs.", round(rebate, 2))
        print("Final bill: Rs.", round(total, 2))

    print("\n===== MONTHLY BILL COMPARISON =====")

    for i in range(len(bills)):
        print(months[i], ": Rs.", round(bills[i], 2))

        if i > 0:
            previous = bills[i - 1]
            current = bills[i]

            if previous > 0:
                increase = ((current - previous) / previous) * 100

                print("Change:", round(increase, 2), "%")

                if increase > INCREASE_LIMIT:
                    print("WARNING: Unusual bill increase detected!")

                elif increase < 0:
                    print("Bill decreased.")

                else:
                    print("Normal bill change.")


if __name__ == "__main__":
    main()
