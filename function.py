def arrangement(N,p):
    Z = N-p
    z = 1
    n = 1
    for i in range(1,Z+1):
      z = z*i
    for i in range(1,N+1):
      n = n*i
    R = n/z
    print (R)
    exit()
def arrangement2(N,p):
    R = N**p
    print (R)
    exit()
def combinaison(N,p):
    Z = N-p
    z = 1
    n = 1
    P = 1
    for i in range(1,Z+1):
      z = z*i
    for i in range(1,N+1):
      n = n*i
    for i in range(1,p+1):
      P = P*i
    m = P*z
    R = n/m
    print (R)
    exit()
def permutation(N):
    R = 1
    for i in range(1,N+1):
      R = R*i
    print (R)
    exit()

