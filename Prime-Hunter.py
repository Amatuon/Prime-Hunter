prime = [] #2,3,5,7,11
prime.append(2)
prime.append(3)

print(prime[0])
print(prime[1])

test = 5
while True:
  isPrime = True

  i = 1
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
      
  test += 2
