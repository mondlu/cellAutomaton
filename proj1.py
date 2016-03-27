def cell_automaton(rule_num, steps):
    
    # generate initial row
    
    initialRow = str('0'*steps + '1' + '0'*steps)  
    
    
    # functions
    def makeNextRow(row):               # makeNextRow should output a string
        binarySets = []
        centerValues = ''
        possibleInputs = ['111','110','101','100','011','010','001','000']
    
        def binaryConversion(rule_num):  # converts rule to binary
            binaryRepresentation = format(rule_num, '#010b')[2:]
            return str(binaryRepresentation)
        
        def binary(row):    # gets the 3-binary inputs 
            i = 0
            while i < len(row)-2:
                binarySets.append(row[i:i+3])
                i = i + 1
        
        binRep = binaryConversion(rule_num) # stores the binary representation as binRep
        binary(row) # calls binary, fills binarySets
    
    
    # loop to construct next line
        for b in binarySets:
            if binRep[possibleInputs.index(b)] == '0': 
                centerValues += '0'
            else:
                centerValues += '1'
        return str('0' + centerValues + '0')
    
    
    
    
    # recurse to generate and print successive rows
    def generateResult(currentRow, i):
        if i <= steps:
            print(currentRow)
            generateResult(makeNextRow(currentRow), i+1)
        else:
            return print('')
            
    
    # output of cell_automaton
    
    return generateResult(initialRow, 0)
    


# test cases
print("Here are some example outputs:")

cell_automaton(139, 20)



cell_automaton(30, 10)


cell_automaton(179, 25)



cell_automaton(222, 20)

print("Want to make your own? Use function cell_automaton (rule, step), with rule and step as any postiive integer")


