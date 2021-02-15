
while True:
  N=input()
  if N=="0":
    break
  N=list(N)
  NN=N
  N="".join(N)
  NN.reverse()
  NN="".join(NN)
  if N==NN:
    print("yes")
  else:
    print("no")
  #print(N)