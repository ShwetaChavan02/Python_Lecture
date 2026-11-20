# Try, Except, Else and Finally
# Withdrawal Program

balance = 20000

try:
    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive")

    if amount > balance:
        raise ValueError("Insufficient balance")

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("An unexpected error occurred:", e)

else:
    balance -= amount
    print("Withdrawal successful...")
    print("Remaining balance:", balance)

finally:
    print("Thank you for using our banking service.")
    print("Transaction process completed.")
