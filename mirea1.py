import sys

def main(argv:list):
    move = ""
    input_data = list()

    imput = "data/input.txt" if "--input" in argv else ""
    output = "data/output.txt" if "--output" in argv else ""
    
    for i in range(len(argv)):
        
        if argv[i]=="--input" and i+1 < len(argv) and not argv[i+1].startswith("-"):
            imput = argv[i+1]
        elif argv[i]=="--output" and i+1 < len(argv) and not argv[i+1].startswith("-"):
            output = argv[i+1]
            
        if "-sum" in argv: move = "+"
        if "-mul" in argv: move = "*"
        if "-avg" in argv: move = "avg"
    
    
    if "--input" not in argv:
        input_data = list(map(float, input().split())) 
    else:
        with open(imput, 'r') as f:
            input_data = list(map(float, f.read().split())) 

    
    if not move: 
        print("Error: no operation"); return

   
    if move == "+": result = sum(input_data)
    elif move == "*":
        result = 1.0
        for x in input_data: result *= x
    elif move == "avg": result = sum(input_data) / len(input_data)

    # Вывод
    if "--output" in argv:
        with open(output, 'w') as f:
            f.write(str(result))
    else:
        print(result)

if name == "main":
    main(sys.argv)