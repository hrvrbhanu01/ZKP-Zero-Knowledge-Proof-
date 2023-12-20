import hashlib
import random

def challenge():
  return random.randrange(0,100)


def hashing(secret):
  return hashlib.sha256(secret.encode()).hexdigest()

def proveKnowledge(secret):
  return(hashing(secret))

def verifyKnowledge(hashedSecret, expectedSecret):
  flag=0
  for i in range(0,100):
    hashExpectedSecret = hashing(expectedSecret+str(i))
    if(hashExpectedSecret==hashedSecret):
        flag=1
        break
  if(flag==1):
        return True
  else:
        return False
    

#Amit Prover
secret = "Treasure location is xy"

challengeValue = challenge()
hashedSecret = proveKnowledge(secret+str(challengeValue))

#Sumit Verifier
expectedSecret = "Treasure location is xyz"
if(verifyKnowledge(hashedSecret,expectedSecret)):
  print("Treasure locations are same")
else:
  print("Treasure locations are not same")