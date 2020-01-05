ch=int(input("Enter '1' to convert from Fahrenheit to Celcius or '2' to convert from Celcius to Fahrenheit \n"))
temp=float(input("Enter temperature: "))
if ch==1:
    a=(temp-32)*5/9
    print("The value in celcius is ",a)
elif ch==2:
    b=(temp*9/5)+32
    print("The value in Fahrenheit is ",b)
else:
    print("Invalid choice")
    
    
               
         
          
