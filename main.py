class Calculator:
    def __init__(self,log_file="history.txt"):
        self.log_file = log_file

    def _save_to_history(self,record : str):
        with open(self.log_file,"a")as f:
            f.write(record + "\n")

    def add(self,a:float,b:float)->float:
        result = a+b
        self._save_to_history(f"{a} + {b} = {result}")
        return result
    
    def subtract(self,a:float,b:float)->float:
            result = a-b
            self._save_to_history(f"{a} - {b} = {result}")
            return result

    def multiply(self,a:float,b:float)->float:
            result = a*b
            self._save_to_history(f"{a} * {b} = {result}")
            return result

    def divide(self,a:float,b:float)->float:
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = a/b
            self._save_to_history(f"{a} / {b} = {result}")
            return result

    def showHistory(self):
        try:
            with open(self.log_file,"r") as f:
                print("Saved History:")
                print(f.read())
        except FileNotFoundError:
                print("\nNo history found.")


calculator = Calculator()

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Show History")
    print("6. Exit")

    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"Result: {calculator.add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {calculator.subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {calculator.multiply(num1, num2)}")
        elif choice == '4':
            try:
                print(f"Result: {calculator.divide(num1, num2)}")
            except ZeroDivisionError as e:
                print(e)

    elif choice == '5':
        calculator.showHistory()

    elif choice == '6':
        print("Exiting the calculator.")
        break

    else:
        print("Invalid input. Please try again.")