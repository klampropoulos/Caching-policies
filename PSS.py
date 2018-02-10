
import random,numpy,sys
import os
import matplotlib.pyplot as plt

## Tested on PYTHON 3.6
#Implementation comments:the below code is an attempt to emulate the Pyramidal Selection Scheme 
#we use 1 dictionlist where every dictionary represent a different sub-cache with different sizes .
#in every dictionary the key represent also the size of the object e.g size('9')==9 and the value is timestamp of the entry
#in every dictionary only objects with specific size are elligible ,meaning in second cache size objects  range from 2 to 3 ,third 4 to 7 .etc
     ##### IMPORTANT ########
### value==key==size_of_object ,for simplicity

class PSSCache:
        def __init__(self, capacity,caches_number,capacities,tm ):
            self.total_capacity = capacity
            self.capacities=capacities       #list of capacity for every cache
            self.tm = tm                     #list of timestamps for every cache-list
            self.moments=0                   #global timestamp
            self.hits=0
            self.requests=0
            self.misses=0
            self.dictlist=[]                 #list that contains dictionaries-caches
            self.n_caches=caches_number 

        def create_diction(self):
            self.dictlist = [dict() for x in range(self.n_caches)] 
            
            return self.dictlist



        def get(self, value,index_cache):
            self.requests +=1
            key_=str(value)
            if key_ in self.dictlist[index_cache]:
               
                self.dictlist[index_cache][key_]=self.tm[index_cache]
                self.tm[index_cache] += 1
                self.moments +=1
                self.hits +=1
                return value
            return -1



        def find_location(self,number):
            for i in range(self.n_caches+1):
                pos=i
                if(number < 2**i) :
                    break
            #print("number \t"+ str(number)+ "belongs to cache-list :"+str(pos))
            return pos

        def getHitratio(self):
            if(self.requests!=0):
                return ((self.hits/self.requests))
            return -1
        def getMissratio(self):
            return float((self.requests-self.hits) / self.requests)

        def set(self,value,index_cache):
            self.misses +=1
            key_=str(value)
            
            while value > self.capacities[index_cache] :
                # find the LRU entry
            #    print(self.dictlist[index_cache].keys())                                           
                                                             ######below expression contains min(  delta time * size (k)) PSS algorithm###########
                old_key = min(self.dictlist[index_cache].keys(), key=lambda k:(self.moments-self.dictlist[index_cache][k]*int(k)))
             #   print("working! , old key"+old_key)
                self.dictlist[index_cache].pop(old_key)
                self.capacities[index_cache] +=int(old_key)
            self.dictlist[index_cache][key_] = self.tm[index_cache]
         #   print(self.dictlist[index_cache].keys())
            self.tm[index_cache] += 1
            self.moments +=1
            self.capacities[index_cache] -=value
            
def main():

        ## Preprocessing find the values
        misses_ratio = []
        hit_ratio = []
        #print("hello")
        if len(sys.argv) >= 2 :
            total_capacity=sys.argv[1]
            total_capacity=int(total_capacity)
        else :
            total_capacity=input("Please give the capacity of the cache(power of 2)!:\t")
            total_capacity=int(total_capacity)
        #print(total_capacity)
        
        n_caches=int(numpy.log2(total_capacity))
        capacities=[]
        tm=[]
        for i in range(n_caches):
            capacities.append(2**i)
            tm.append(0)

        #### Creating the object  
        cache=PSSCache(total_capacity,n_caches,capacities,tm) 
        if type(n_caches) is int :
            lis=cache.create_diction()
            
       # print(capacities)



        type_of_input=input("Please give the type of input:(1->almost_random),(0->zipf distribution) :\t")
        ##### Starting Producing random numbers and filling the caches

        random.seed(20)
        if(int(type_of_input)==0):
            for j in range(100000):
                
                
              
                number=numpy.random.zipf(2)
                if number < total_capacity/2 :
                    index_cache=cache.find_location(number)
                    hit_or_miss=cache.get(number,index_cache)
                    if(hit_or_miss==-1):
                        cache.set(number,index_cache)
               
            
            print("PSS-zipf input")
            print("Total Requests:\t"+str(cache.requests))
            print("Misses:\t"+str(cache.misses))   
            print("Hits:\t"+str(cache.hits))
            print("Miss ratio:\t"+str(cache.getMissratio()))
            print("Hit ratio:\t"+str(cache.getHitratio()))
        elif(int(type_of_input)==1):
            for j in range(1000):
                for i in range(100):
                
              
                    number=random.randint(1,(total_capacity/2)-1)
                   
                    index_cache=cache.find_location(number)
                    hit_or_miss=cache.get(number,index_cache)
                    if(hit_or_miss==-1):
                        cache.set(number,index_cache)
               
            
            print("PSS-random input")
            print("Total Requests:\t"+str(cache.requests))
            print("Misses:\t"+str(cache.misses))   
            print("Hits:\t"+str(cache.hits))
            print("Miss ratio:\t"+str(cache.getMissratio()))
            print("Hit ratio:\t"+str(cache.getHitratio()))
        else:
            print("Invalid input choice!Goodbye!")
main()
