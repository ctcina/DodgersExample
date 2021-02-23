intro = "Welcome to the EOQ Calculator prepared by Tucker Cina "
question = "Enter q to quit or the name of the coffee:"
nocalc= "There are no calculations to display\nLoad a file or perform new calculations\n"
mainmenu= "Main Menu:\nA)dd calculations to an existing file\nL)oad a file and view results\nP)rint current results\n\
R)eset and perform new EOQ calculations\nS)ave current calculations to a file\nQ)uit:\n"

def validate(vString):
    while vString.isalpha():
        vString = input("Non-numeric values are not accepted. Please provide a numeric value:\n")
    while float(vString) < 0:
        vString = input("Negative values are not accepted. Please provide a positive value:\n")
    return vString

def getParam():
    """ This function gets four parameters. 
    demand (D), the unit cost (C), the order cost (K) and the holding cost (h)"""
    
    D=int(validate(input("Please input the demand of coffee you need per year:\n")))   
    C=float(validate(input("Please input the unit cost:\n")))
    K=float(validate(input("Please input the order cost:\n")))
    h=float(validate(input("Please input the holding cost:\n"))) 
    
    return D, C, K, h

def calcEOQ(D, C, K, h):
    """ This function calculates the values of Q, T, and TAC. """
    
    Q = (2*D*K/h)**(1/2)
    TAC = Q*h/2+D*K/Q+D*C
    T = (Q/D)*(365/7)
    
    return Q, TAC, T

def printResults(brandlist):
    """ This function displays the results of the EOQ calculations a user performed on various brands of coffee. """
    
    totalQ = 0
    
    print("*********\n\nThe Result of EOQ Calculations\n\n*********")
    print("{0:20} {1:20} {2:20} {3:20}" .format('Brand', 'Quantity (lbs)', 'Total Cost ($)', 'Cycle Length (in weeks)'))
    
    for row in brandlist:
        print("{0:<20} {1:<20.2f} {2:<20.2f} {3:<20.2f}" .format(row[0], float(row[5]), float(row[6]), float(row[7])))
        totalQ += float(row[5])
    print("*********\n\n")
    print("If you purchase all of the coffee, you will need space to hold {0:.2f} lbs. of coffee.\n\n" .format(totalQ))     
        
def askData(brandlist):
    print(question)
    a= input()
    while (a.lower() !="q"):
        D, C, K, h = getParam()
        Q, TAC, T = calcEOQ(D, C, K, h)
        brandlist.append([a, D, C, K, h, Q, TAC, T])
        a = input(question + "\n")
    printResults(brandlist)    

def load_data(filename='brandlistText'):
    """Load the elements stored in the text file named filename. """
    brandlist = []
    with open(filename) as f:
        for line in f:
            brandlist.append(line.split())
    return brandlist
       
def store_data(brandlist, filename='brandlistText'):
    """Allows the user to store data in a list to the text file named filename. """
    with open(filename, 'w') as f:
        for i in brandlist:
            for j in i:
                f.write(str(j) + ' ')
            f.write('\n')
  
def main():
    print(intro)
    print()
    done= False
    while not done:
        menu = input(mainmenu)        
        if menu.lower() == 'r':
            brandlist = []
            askData(brandlist)
        elif menu.lower() == 'a':
            try:
                askData(brandlist)
            except UnboundLocalError:
                print(nocalc)
        elif menu.lower() == 's':
            try:
                filename= input('Enter file name. Hit enter for the default file (brandlistText)\n')
                if filename: store_data(brandlist, filename)
                else: store_data(brandlist)
            except UnboundLocalError:
                print(nocalc)
                input("Hit enter to go to the main menu")
            except: pass
        elif menu.lower() == 'p':
            try:
                printResults(brandlist)
            except UnboundLocalError:
                print(nocalc)
                input("Hit enter to go to the main menu")
            except: pass
        elif menu.lower() == 'l':
            while True:
                try:
                    filename = input('Enter a file name. Hit enter for the default file (brandlistText)')
                    if filename: brandlist = load_data(filename)
                    else: brandlist = load_data()
                    if brandlist:
                        printResults(brandlist)
                        break
                except FileNotFoundError:
                    print("Please provide a valid filename")
        elif menu.lower() == 'q':
            done = True
    
    
if  __name__ == '__main__':
    main()
