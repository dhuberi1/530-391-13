def read(): 
  f = open("input", 'r') 
  
  # read a 
  line = f.readline()
  split = line.split()
  print(split)
  a = float(split[2])
  print(a)  


  # read b 
  line = f.readline()
  split = line.split()
  print(split)
  a = float(split[2])
  print(b)  

  # read c 
  line = f.readline()
  split = line.split()
  print(split)
  c = float(split[2])
  print(c)  
  
  #clean up 
  f.close()

  #return a, b, c
  return [a, b, c]
