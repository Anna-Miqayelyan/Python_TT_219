import random
import time

def new_file(name):
    with open(name,'w')as f:
       for _ in range(100):
           line=' '.join(str(random.randint(1,100))for _ in range(20))
           f.write(line+'\n')
           
def read_file(name):
    with open(name,'r') as f:
        
        lines=f.readlines()
    read_lines=[list(map(int,line.split()))for line in lines]
    return read_lines

def filter_file(input_name,output_name):
    data=read_file(input_name)
    with open(output_name,'w') as f:
        for line in data:
            filtered=list(filter(lambda x:x>40,line))
            f.write(' '.join(map(str,filtered))+'\n')
            #print(filtered)
def generator(name):
    with open(name,'r') as f:
        for line in f:
            yield list(map(int,line.split()))
            
def time_decorator(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(f"Time of execution {func.__name__}:{end-start:.4f} seconds")
        return result
    return wrapper

@time_decorator
def main():
    name="just.txt"
    new_file(name)
    print("File contents: ")
   # print(read_file(name))
    
    filtered_name = "filtered_just.txt"
    filter_file(name, filtered_name)
    print(f"Filtered data saved to {filtered_name}.")

    print("Displaying from the generator:")
    gen = generator(filtered_name)
    for i, line in enumerate(gen):
        print(line)
        if i >= 4:  
            break

if __name__ == "__main__":
    main()

    
