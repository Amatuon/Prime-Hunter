from math import sqrt

prime = [] #2,3,5,7,11
prime.append(2)
prime.append(3)

print(prime[0])
print(prime[1])

factor = []
factor.append(0)
factor.append(0)

test = 5
while True:
  isPrime = True

  i = 1
  while i < len(prime):
    j = i
    loopAgain = True
    while loopAgain:
      factor[j] += 1
      loopAgain = False
      if test > (prime[j] * factor[j]):
        loopAgain = True
      if test == (prime[j] * factor[j]):
        isPrime = False
        i = len(prime)
      if prime[j] > sqrt(test):
        i = len(prime)
      if loopAgain == False:
        factor[j] -= 1
    i += 1
  
  if isPrime == True:
    prime.append(test)
    factor.append(0)


    # 0 for none, 1 for print each prime, 2 for updates on number found
    output = 1

    if output == 1:
      print(test)
    elif output == 2:
      scale = 1000
      if int(len(prime) / scale) == len(prime) / scale:
        print(str(len(prime)) + " Found!")

  test += 2
