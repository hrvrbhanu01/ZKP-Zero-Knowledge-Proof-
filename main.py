import hashlib

def hashing(secret):
  return hashlib.sha256(secret.encode()).hexdigest()

def proveKnowledge(secret):
  return(hashing(secret));

def verifyKnowledge(hashedSecret, expectedSecret):
  hashExpectedSecret = hashing(expectedSecret)
  if(hashExpectedSecret==hashedSecret):
    return True
  else:
      return False
    

#Amit Prover
secret = "Treasure location is xyz"
hashedSecret = proveKnowledge(secret)


#Sumit Verifier
expectedSecret = "Treasure location is xyz"
if(verifyKnowledge(hashedSecret,expectedSecret)):
  print("Treasure locations are same")
else:
  print("Treasure locations are not same")