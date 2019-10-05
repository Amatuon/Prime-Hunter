from math import sqrt

# 0 for none, 1 for print each prime, 2 for updates on number found
output = 1

#array to hold all prime numbers found so far
prime = [] 
prime.append(2) #initalized so we can optimize for speed
prime.append(3)

#displays our seeding primes for completeness
if output == 1:
  print(prime[0]) 
  print(prime[1])

#array to hold the current scaling factor associated with each prime
factor = []
factor.append(0)
factor.append(0)

#the first number to check the primality of
test = 5

#main loop
while True:
  
  #begins true, numbers are innocent untill proven guilty
  isPrime = True

  #starts at 1 to skip '2' no need to test this because we already filter out all even numbers
  i = 1
  #loop through all 'known' primes
  while i < len(prime):
    
    #couldn't figure out break 2 in python so this is an artifact
    j = i

    loopAgain = True
    #loop though all factors until we hit the test number or exceed it
    while loopAgain:

      #housekeeping
      factor[j] += 1
      loopAgain = False
      
      #we havent overshot yet so continue
      if test > (prime[j] * factor[j]):
        loopAgain = True
      
      #we hit the test number showing that it isn't prime
      if test == (prime[j] * factor[j]):
        isPrime = False
        #stops the search through the 'known' primes
        i = len(prime)
      
      #no need to search higher than this we are garunteed to have hit a factor by this point if one exists
      if prime[j] > sqrt(test):
        i = len(prime)

      #if we are done lower our factor for this prime by 1, this only happens if we have already overshot preventing us from missing a new prime down the road
      if loopAgain == False:
        factor[j] -= 1

    #start again with the next prime
    i += 1
  
  #when a prime is found
  if isPrime == True:
    #add it to the 'known' list and add a factor for it
    prime.append(test)
    factor.append(0)

    #display useful data to end user
    if output == 1:
      print(test)
    elif output == 2:
      scale = 1000
      if int(len(prime) / scale) == len(prime) / scale:
        print(str(len(prime)) + " Found!")

  #no need to test even numbers
  test += 2
