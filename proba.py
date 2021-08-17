from arrangSS import *



def probabilite():

    ordonne =input('l\'experience est ordonne ? \n si oui entrer y: \n si non entrer n: \n')
    if ordonne=="y" or ordonne=="n":
      pass
    else:
      print("entrer y ou n svp")
      probabilite()
 	  	  
    remise = input('avec remise ? \n si oui entrer y: \n si non entrer n: \n')
    if remise =="y" or remise =="n":
      pass
    else:
      print("entrer y ou n svp")
      probabilite()



    global N
    global p
    N = int(input('entrer le nombre N:'))
    p = int(input('entrer le nombre P:'))


    if N >= p:


      if ordonne=="y" and remise=="y" and N>p :
        arrangement2(N,p)

      elif ordonne=="y" and remise=="n" and N > p :
        arrangement(N,p)

      elif ordonne=="y" and remise=="n" and N==p:
        permutation(N)

      elif ordonne=="n" and remise=="n" and N>p:
        combinaison(N,p)

      elif ordonne=="n"  and remise=="y" and N>p:
        N = N+p
        N = N-1
        combinaison(N,p)
      elif N<p:
        print (" try again, N or P is wrong")
        probabilite()

    else:
      print (" impossile n plus que p ")
      probabilite()

probabilite()
