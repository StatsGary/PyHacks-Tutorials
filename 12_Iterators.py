# =============================================================================
# Title             PyHacks - Classes  - Iterators
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      13/07/2021
# =============================================================================
#Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
#All these objects have a iter() method which is used to get an iterator:

#-----------------------CREATE ITERATOR----------------------------------------

#To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
#As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created.
#The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
#The __next__() method also allows you to do operations, and must return the next item in the sequence.
    
class Numbers:
    def __iter__(self):
        self.i = 1
        return self
    def __next__(self):
        iterator = self.i
        self.i +=1
        return iterator
    
    
iter_class = Numbers()
iterate = iter(iter_class)

print(next(iterate))
print(next(iterate))

# This example would go on forever. Now we need the stop iteration method

#-----------------------STOP ITERATOR---------------------------------------- 

class NumbersStopIter:
    def __iter__(self):
        self.i = 1
        return self
    def __next__(self):
        if self.i <= 20:
            iterator=self.i
            self.i += 1
            return iterator
        else:
            raise StopIteration #This will stop when the boolean condition met
            
call_stopped_class = NumbersStopIter()
iter_stopped = iter(call_stopped_class)


# Loop through each item until the end

for i in iter_stopped:
    print(i)