import math

def problem1():
    SommeMultiples3et5 = 0
    for i in range(1000):
        if i%3 == 0 or i%5 == 0:
            SommeMultiples3et5 = SommeMultiples3et5 + i
    print (SommeMultiples3et5)
    
def problem2():
    Somme = 2
    element1 = 1
    element2 = 2
    element3 = element1 + element2
    
    while element3 < 4000000:
        if element3 % 2 == 0:
            Somme += element3
        element1 = element2
        element2 = element3
        element3 = element1 + element2    
    
    print (Somme)
    
def isPremier(n):
    for i in range(3,math.floor(math.sqrt(n))+1,2):
        if n % i == 0:
            return False
    return True

    
    
def problem3(n):
    maxDiv = 1
    for i in range(3,math.floor(math.sqrt(n)),2):
        if (n%i == 0) & isPremier(i):
            maxDiv = i
    return maxDiv
            
#print (problem3(600851475143)) 
def IndexIn(i,l):
    for j in range(0,len(l)):
        if (l[j] == i):
            return j
    return -1
    
def listeDiviseurs (n):
    div = []
    div1 = []
    q = 0
    for i in range(2,math.floor(n+1)):
        if (n%i == 0) & isPremier(i):
            div.append(i)
            q = n/i
            break
    if q > 0:
        div1 = listeDiviseurs(q)
    return div + div1
    

def problem4(n):
    diviseurs=[]
    for dd in range (2,n+1):
        div = listeDiviseurs(dd)  
        print ('----') 
        index1 = 0  
        for d in div:
            index2 = IndexIn(d,diviseurs[index1:len(diviseurs)])
            if index2 < 0 :
                diviseurs[index1:index1] = [d]
            
            index1 = index2+1 
            print (diviseurs, index1)                    
         
#            else:
#                index1 = index2+1    
   
    print (diviseurs)        
    produit = 1       
    for j in range (0,len(diviseurs)):
        produit *= diviseurs[j]        
    return produit
 
#print (listeDiviseurs(55))  
#print (problem4(20))
    
    
def problem6(n):
    somme1 = 0
    somme2 = 0
    for i in range(0,n+1):
        somme1 = somme1 + i * i
        somme2 = somme2 + i
    somme2 *= somme2
    
    print (somme2 - somme1)
    
#problem6(100)

def problem7(n):
    count = 2
    number = 1
    while (count <= n):
        number+=2
        if isPremier(number):
            count += 1
         
    print (number)
    
#print(isPremier(15))    
problem7(10001)


def problem8(n):
    maxvalue = 0
    List = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
    for i in range(0,List.count-n):
        value = 0
        for j in range(0,n):
            value = value + List[i+j]

        if value > maxvalue :
            maxvalue = value

    print(maxvalue)
