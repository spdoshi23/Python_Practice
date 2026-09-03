secret_pin = 4321
while True:
    pin = int(input("Enter your pin: "))
    if pin == secret_pin:
        print("Access granted")
        break
    else:
        print("Access denied") 



#                ALTERNATE WAY
secret_pin = 4321                            #initialization
pin = int(input("Enter your pin: "))
while pin!= 4321:                            #condition
    print("Access denied")
    pin = int(input("Enter your pin: "))     #update
print("Access granted")