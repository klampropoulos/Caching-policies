
import random,numpy,sys
import os
import matplotlib.pyplot as plt

## Tested on PYTHON 3.6

### value==key==size_of_object ,for simplicity

class LRUCache:
        def __init__(self, capacity ):
            self.total_capacity = capacity                 
            self.tm = 0                     #timestamp                              
            self.hits=0
            self.requests=0
            self.misses=0
            self.lru={}              #dictionary-cache
            

        def get(self, value):
            self.requests +=1
            key_=str(value)
            if key_ in self.lru:
               
                self.lru[key_]=self.tm
                self.tm += 1
                self.hits +=1
                return value
            return -1

        def getHitratio(self):
            if(self.requests!=0):
                return ((self.hits/self.requests))
            return -1

        def getMissratio(self):
            return float((self.requests-self.hits) / self.requests)

        def set(self,value):
            self.misses +=1
            key_=str(value)
            
            while value > self.total_capacity :
                # find the LRU entry
                                                                                                 
                old_key = min(self.lru.keys(), key=lambda k:self.lru[k])
              #  print("working! , old key"+old_key)
                self.lru.pop(old_key)
                self.total_capacity +=int(old_key)
            self.lru[key_] = self.tm
         #   print(self.lru.keys())
            self.tm += 1
            
            self.total_capacity -=value
            
def main():

        ## Preprocessing find the values
        misses_ratio = []
        hit_ratio = []
      #  print("hello")
        if len(sys.argv) >= 2 :
            total_capacity=sys.argv[1]
            total_capacity=int(total_capacity)
        else :
            total_capacity=input("Please give the capacity of the cache!:\t")
            total_capacity=int(total_capacity)
     #   print(total_capacity)
        
    
        #### Creating the object  
        cache=LRUCache(total_capacity)
        
        ##### Starting Producing random numbers and filling the caches
        type_of_input=input("Please give the type of input:(1->almost_random),(0->zipf distribution) :\t")
        random.seed(20)
        if(int(type_of_input)==0):
            for j in range(100000):
              
                number=numpy.random.zipf(2)
                if number < total_capacity :
                   
                    hit_or_miss=cache.get(number)
           #         print("hit or miss")
            #        print(hit_or_miss)
                    if(hit_or_miss==-1):
                        cache.set(number)

            print("LRU-zipf distribution")  
            print("Total Requests:\t"+str(cache.requests))
            print("Misses:\t"+str(cache.misses))   
            print("Hits:\t"+str(cache.hits))
            print("Miss ratio:\t"+str(cache.getMissratio()))
            print("Hit ratio:\t"+str(cache.getHitratio()))
        elif(int(type_of_input)==1):
            for j in range(1000):
                for i in range(100):
                    number=random.randint(1,(total_capacity/2)-1)
                    hit_or_miss=cache.get(number)
           #         print("hit or miss")
            #        print(hit_or_miss)
                    if(hit_or_miss==-1):
                        cache.set(number)


            print("LRU-random input")
            print("Total Requests:\t"+str(cache.requests))
            print("Misses:\t"+str(cache.misses))   
            print("Hits:\t"+str(cache.hits))
            print("Miss ratio:\t"+str(cache.getMissratio()))
            print("Hit ratio:\t"+str(cache.getHitratio()))
        else:
            print("Invalid input choice!Goodbye!")
main()
