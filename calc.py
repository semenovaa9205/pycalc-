

def calc(x, y, operation):
        match  operation:
           case "+":
            return x+y
           case"-":
            return x-y
           case "*":
            return x*y
           case"/":
            return x/y
           case _:
            print('вы ввели что-то нето')


while True:
      try:
            x = float(input("введдите 1 число"))
            y = float(input("введите 2 число"))
            operation = input('введите знак оператции(+,-,*,/)')
            rez = calc(x, y, operation)
            print(rez)
      except ValueError:
        print("вы ввели не число!")

      
      answer=input("хотите продоллжить?(y/n)")
      if answer!="y":
            break


        
        