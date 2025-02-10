### Uncorupt numbers by Multiplying them

## It does this by mul(x,y)


#Set up
import re
import sys

if __name__ == '__main__':
    #if len(sys.argv) == 1:
    #    print(f'Usage: {sys.argv[0]} <mem.txt>')
    #    sys.exit(1)
    mem_path = "example1.txt"

    try: ##Error  path checking
        with open(mem_path, 'r') as f:
            mem = f.read()
    except FileNotFoundError:
        print(f"Error: File '{mem_path}' not found.")
        sys.exit(1)
    
    #mem_clean = re.findall(r'do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\)', mem) #cleaning
    
    sum_mul = 0
    do_sum = True
    for x in re.finditer(r'do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\)', mem):

        match x[0]:
            case 'do()':
                do_sum = True
            case 'don\'t()':
                do_sum = False
            case _:
                if do_sum:
                    sum_mul += int(x[1]) * int(x[2])
    
    
    #for x, y in mem_clean:
    #    sum_mul += int(x) * int(y) #Summing

#Read   
    print(f"File content: {mem}")
    #print(f"Matched values: {mem_clean}")    
    print(f'Sum of multiplication: {sum_mul}')

