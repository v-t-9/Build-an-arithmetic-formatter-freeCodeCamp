def arithmetic_arranger(problems, show_answers=False):
    res = ""
    first = ""
    second = ""
    dashes = ""
    sol = ""
    if len(problems) > 5:
        return f'Error: Too many problems.'
    
    symb = [j for i in problems for j in i]
  
    if "*" in symb or "/" in symb:
        return f"Error: Operator must be '+' or '-'."
    
    op = [i.split() for i in problems]
    for i in op:
        if i[0].isnumeric() == False or i[2].isnumeric() == False:
            return f'Error: Numbers must only contain digits.'
        if len(i[0]) > 4 or len(i[2]) > 4:
            return f'Error: Numbers cannot be more than four digits.'
   
    for i in op:
       
        n1 = i[0].strip()
        sym = i[1].strip()
        n2 = i[2].strip()
        if len(n1) > len(n2):
            spaces = len(n1)+2
        else:
            spaces = len(n2)+2
           

        num1 = f'{n1:>{spaces}}'
        num2 =f'{sym} {n2:>{(spaces-2)}}'
        dashes += f'{"-"* spaces}'
        if i != op[-1]:
            first += num1 + "    "
            second += num2 + "    "
            dashes += "    "
        else:
            first += num1 
            second += num2 
            dashes = dashes

        res = f'{first}\n{second}\n{dashes}'
        
        if show_answers == True:
            if sym == "+":
                sol += f'{str(int(i[0]) + int(i[2])):>{spaces}}'
            if sym == "-":
                sol += f'{str(int(i[0]) - int(i[2])):>{spaces}}'
           
            if i != op[-1]:
                sol += "    "
            else:
                sol = sol
            res = f'{first}\n{second}\n{dashes}\n{sol}'


    
    return res

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
#print(f'\n{arithmetic_arranger(["3 + 855", "988 - 40"], True)}'
print(f'\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')
