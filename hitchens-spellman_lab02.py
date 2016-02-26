#2.3
expr = input ("Please enter an expression of the form 'number+number': ") #Define the expression

sign = expr.find ("+") #Define the sign

first = expr [:sign] #Define the first number

second = expr [sign+1:] #Define the second number

sum = int (first) + int(second) #Define the sum of both numbers

print (first,"+",second,"=",sum) #Print the complete expression

#2.4
expr = input ("Please enter an expression of the form 'number+number': ") #Define the expression

sign = expr.find ("+") #Define the sign

if sign >= 0: #If a "+" sign is found

    first = expr [:sign] #Define the first number

    second = expr [sign+1:] #Define the second number

    sum = int (first) + int(second) #Define the sum of both numbers

    print (first,"+",second,"=",sum) #Print the complete expression

else: #If a "+" sign is not found
    
    print ("Error: invalid expression") #Print an error message

#2.6
while (True): #Loop the program
    
    expr = input ("Please enter an expression of the form 'number+number': ") #Define the expression

    sign = expr.find ("+") #Define the sign

    if sign >= 0: #If a "+" sign is found

        first = expr [:sign] #Define the first number

        second = expr [sign+1:] #Define the second number

        sum = int (first) + int(second) #Define the sum of both numbers

        print (first,"+",second,"=",sum) #Print the complete expression

    else: #If a "+" sign is not found
    
        print ("Error: invalid expression") #Print an error message

#2.7
while (True): #Loop the program
    
    expr = input ("Please enter an expression of the form 'number+number' or type 'end' to exit the program: ") #Define the expression

    sign = expr.find ("+") #Define the sign

    if expr == ("end"): #If the user wants to end the program

        print ("Goodbye") #Print an ending message

        break #End the loop

    elif sign >= 0: #If a "+" sign is found

        first = expr [:sign] #Define the first number

        second = expr [sign+1:] #Define the second number

        sum = int (first) + int(second) #Define the sum of both numbers

        print (first,"+",second,"=",sum) #Print the complete expression

    else: #If a "+" sign is not found
    
        print ("Error: invalid expression") #Print an error message

#3.1
while (True): #Loop the program
    
    expr = input ("Please enter an expression of the form 'number+number', type 'last' to see the last three expressions completed, or type 'end' to exit the program: ") #Define the expression

    sign = expr.find ("+") #Define the sign

    if expr == ("end"): #If the user wants to end the program

        print ("Goodbye") #Print an ending message

        break #End the loop

    elif sign >= 0: #If a "+" sign is found

        first = expr [:sign] #Define the first number

        second = expr [sign+1:] #Define the second number

        sum = int (first) + int(second) #Define the sum of both numbers

        print (first,"+",second,"=",sum) #Print the complete expression

    elif expr == ("last"): #If the user wants to see the last expression

        print(first,"+",second,"=",sum) #Print the last expression

    else: #If a "+" sign is not found
    
        print ("Error: invalid expression") #Print an error message

#3.3
while (True): #Loop the program
    
    expr = input ("Please enter an expression of the form '(number+number)', type 'last' to see the last three expressions completed, or type 'end' to exit the program: ") #Define the expression

    sign = expr.find ("+") #Define the sign

    bracket1 = expr.find ("(") #Defining the opening bracket

    bracket2 = expr.find(")") #Defining the closing bracket

    if expr == ("end"): #If the user wants to end the program

        print ("Goodbye") #Print an ending message

        break #End the loop

    elif sign >= 0 and expr.startswith ("(") and expr.endswith (")"): #If a "+" sign is found and the input starts and ends with brackets

        first = expr [bracket1+1:sign] #Define the first number

        second = expr [sign+1:bracket2] #Define the second number

        sum = int (first) + int(second) #Define the sum of both numbers

        print ("(",first,"+",second,")","=",sum) #Print the complete expression

    elif expr == ("last"): #If the user wants to see the last expression

        print("(",first,"+",second,")","=",sum) #Print the last expression

    else: #If a "+" sign is not found
    
        print ("Error: invalid expression") #Print an error message
