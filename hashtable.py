class HashTable:

  def __init__(self):
    self.max = 5
    self.arr = [[] for i in range(self.max)]
  
  def get_hash(self, key):
    sum = 0
    for c in key:
      sum = sum + ord(c)
    return sum % self.max
  
  def __setitem__(self, key, value):
    h = self.get_hash(key)
    pair = (key, value)
    for idx, element in enumerate(self.arr[h]):
      if len(element)==2 and element[0]==key:
        self.arr[h][idx] = pair
        return
    self.arr[h].append(pair)

  def __getitem__(self, key):
    h = self.get_hash(key)
    for element in self.arr[h]:
      if len(element)==2 and element[0]==key:
        return element[1]

  def __delitem__(self, key):
    h = self.get_hash(key)
    for idx, element in enumerate(self.arr[h]):
      if len(element)==2 and element[0]==key:
        del self.arr[h][idx]
        

if __name__=="__main__":
  
  h = HashTable()
  h["go"] = "back"
  h["c++"] = "backend"
  h["python"] = "script"
  h["angular"] = "frontend"
  h["react"] = "front"

  print(h.arr)
  print(h["python"])
  del h["go"] 
  print(h.arr)

