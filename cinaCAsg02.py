import math

print('Welcome to the EOQ Calculator prepared by Tucker Cina')

brand=0
sumPounds=0

while brand!='q'or brand!='Q':
    
    print('Enter q to quit or the name of the coffee')
    x= input()
    brand= str(x)  
    
    if brand=='q' or brand=='Q':
        print("If you purchase all of the coffee you will need space to hold {0:.2f} lbs. of coffee.".format(sumPounds))
        quit()
    else:
        print('Enter the demand (D):')
        x=input()
        demand= int(x)
        print('Enter the unit cost (C):')
        x=input()
        unitCost= float(x)
        print('Enter the order cost (K):')
        x=input()
        orderCost= float(x)
        print('Enter the holding cost (h):')
        x=input()
        holdingCost=float(x)


        Q= math.sqrt((2*demand*orderCost)/holdingCost)

        TAC= (((Q/2)*holdingCost)+((demand*orderCost)/Q)+(demand*unitCost))

        T=(Q/demand)*12


        print("Given D={0}, C={1}, K={2}, h={3}" .format(demand, unitCost, orderCost, holdingCost))
         
        print("You should order{0: .2f} lbs. of {1} every {2:0.1f} months for a total cost of ${3:0.2f}.".format(Q,brand,T,TAC))
        
        sumPounds+=Q