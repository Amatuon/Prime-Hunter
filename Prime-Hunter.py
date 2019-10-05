prime = [] #2,3,5,7,11
prime.append(2)

test = 3
while True:
  isPrime = True

  i = 0
  while i < len(prime):
    factor = 0
    loopAgain = True
    while loopAgain:
      loopAgain = False
      factor += 1
      if test > (prime[i] * factor):
        loopAgain = True
      if test == (prime[i] * factor):
        isPrime = False
        i = len(prime)
    i += 1
  
  if isPrime == True:
    prime.append(test)
    print(test)
  
  test += 1
