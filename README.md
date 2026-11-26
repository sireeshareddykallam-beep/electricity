# electricity
# Progressive Electricity Billing System

## Project Overview

The Progressive Electricity Billing System is a Python-based application that calculates household electricity bills based on electricity consumption.

It uses multiple consumption slabs, fixed charges, surcharges, and rebates to calculate the final bill. It also compares electricity bills across different months and identifies unusual increases.

## Objectives

- Calculate electricity bills based on consumed units.
- Apply progressive electricity slab rates.
- Add fixed monthly charges.
- Calculate applicable surcharges.
- Apply rebates for eligible households.
- Compare bills across multiple months.
- Identify unusual increases in electricity bills.

## Electricity Tariff Structure

| Consumption Slab | Rate Per Unit |
|---|---:|
| 0–100 units | ₹2 |
| 101–200 units | ₹3 |
| 201–300 units | ₹5 |
| Above 300 units | ₹7 |

## Additional Charges

- Fixed Charge: ₹50
- Surcharge: 5% of energy charges
- Rebate: 10% of energy charges for consumption up to 100 units
- Unusual Increase: More than 30% compared with the previous month's bill.

*Note: All tariff values are sample values used for this academic project.*

## Technologies Used

- Python 3
- Variables and Data Types
- Functions
- Conditional Statements
- For Loops
- Lists
- Mathematical Operations

## Project Structure

```text
Progressive-Electricity-Billing/
│
├── electricity_billing.py
│
└── README.md
```

## How to Run the Project

1. Install Python 3 on your computer.
2. Download or clone this GitHub repository.
3. Open the project folder in Visual Studio Code.
4. Open the terminal.
5. Execute the following command:

```bash
python electricity_billing.py
```

6. Enter the number of months.
7. Enter the month name and electricity units consumed.
8. View the calculated electricity bills.
9. Check the monthly comparison and unusual increase warnings.

## Expected Output

The application displays:

- Monthly electricity consumption.
- Energy charges.
- Fixed charges.
- Surcharge amounts.
- Applicable rebates.
- Final electricity bill.
- Monthly bill comparisons.
- Warnings for unusual bill increases.

## Advantages

- Automates electricity bill calculations.
- Provides accurate slab-wise calculations.
- Makes monthly bill comparisons easier.
- Identifies unusual bill increases.
- Saves time and reduces manual calculation errors.

## Future Enhancements

- Store monthly electricity records in a database.
- Generate PDF electricity bills.
- Display monthly usage graphs.
- Add a graphical user interface.
- Support multiple household accounts.
- Export monthly reports to Excel.

## Conclusion

The Progressive Electricity Billing System provides a simple and efficient way to calculate household electricity bills. It uses progressive tariff slabs, fixed charges, surcharges, and rebates while helping users monitor monthly electricity expenses and identify unusual increases.

---

**Project Name:** Progressive Electricity Billing System

**Programming Language:** Python 3

**Project Type:** Electricity Bill Management System
