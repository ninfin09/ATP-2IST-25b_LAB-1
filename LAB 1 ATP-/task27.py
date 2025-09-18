# Зчитуємо майбутню суму
f = float(input("enter the desired future value: "))      
# Зчитуємо річну ставку
r = float(input("enter the annual interest rate: "))      
# Зчитуємо кількість років
n = int(input("enter the number of year the money will grow: "))
# Обчислюємо поточну суму
p = f / pow(1 + r, n)           
# Виводимо результат                          
print("you  will need to deposite this amount: {:.2f}.".format(p)) 