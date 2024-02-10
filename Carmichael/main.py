from sympy import factor
from sympy import nextprime

#Έλεγχος για το αν κάποια τιμή είναι μεγαλύτερη του 1.Ανσυμβει αυτό  σημαίνει ότι έχει χρησιμοποιηθεί 2 φορές το ίδιο
#νούμερο οπότε δεν είναι ελεύθερη τετράγωνου
def Free_Square ( N):
  factor_dict = dict(factor(N).factors())
  valueOfDict = list(factor_dict.values())#Κρατάμε μόνο τις τιμές από το λεξικό factor_dict
  Free_square = True
  for i in range(len(valueOfDict)):
    if ( valueOfDict[i] != 1 ):
      return  False
      break
    return True

#Ελενχος για το αν κάποια τιμή δεν πλήρη την προϋπόθεση p|N, p-1|N-1
def Carmichael (N):
  factor_dict = dict(factor(N).factors())
  keyOfDict  = list(factor_dict.keys())
  Carmichael = True
  for i in range (len(factor_dict)):
    if (((N-1) % (keyOfDict[i]-1)) !=0  | (N % keyOfDict[i]!=0)) :
      return False
      break
  return True

N = 6553130926752006031481761
#Εμφανιση λίστας με τους συνθέτους αριθμούς αλλά και το πόσες φορές εμφανίζονται
if Free_Square (N) & Carmichael  (N ):
  print('The numbre is Carmichael')
else:
  print('The numbre is not Carmichael')

#Ερευση του επομένου μεγαλύτερου Carmichael
Next_prime = 181#Πήραμε από το 181 καθώς αυτός ήταν ο τελευταίος πρώτος αριθμός που πήραμε από τον τελευταίο παράδειγμα
while True:
  Next_prime=nextprime(Next_prime)
  temp = N * Next_prime
  if Free_Square(temp) & Carmichael(temp):
    print('The next nuber', temp ,'is a Carmichael')
    break
