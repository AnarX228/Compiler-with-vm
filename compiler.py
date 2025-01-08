from tokenizer import *
from vm import *

def compile(source):
    instructions = []
    source = source.replace('\n','')
    commands = source.split(";")

    for command in commands:
        tokens = tokenize(command)
        print(tokens)
        if len(tokens) >= 3 and tokens[0][0] == "ID" and tokens[0][1] == "var" and tokens[1][0] == "ID":
            if tokens[2][0] == "EQUAL":
                values = tokens[3:]

                added_instructions = evalute(values)
                for instruction in added_instructions:
                    instructions.append(instruction)

                instructions.append("STORE")
                instructions.append(tokens[1][1])

        elif len(tokens) >= 3 and tokens[0][0] == "ID" and tokens[0][1] == "if" and tokens[1][0] == "BRACKETS" and tokens[2][0] == "BRACKETS":
            values = tokenize(tokens[tokens[1][1]])

            added_instructions = evalute(values)
            for instruction in added_instructions:
                instructions.append(instruction)

            instructions.append("IF")
            instructions.append(compile(tokens[2][1].split(',')))


        elif len(tokens) >= 2 and tokens[0][0] == "ID":
            if tokens[0][1] == "print":
                values = tokens[1:]
                added_instructions = evalute(values)
                for instruction in added_instructions:
                    instructions.append(instruction)
                instructions.append("PRINT")

    return instructions

def evalute(values):
    instructions = []
    operation = ""
    arguments = 0

    for value in values:
        if value[0] == "ADD" or value[0] == "SUB" or value[0] == "MUL" or value[0] == "DIV":
            operation = value[0]
        elif value[0] == "GREATER" or value[0] == "LESS" or value[0] == "EQUALS":
            operation = value[0]
        elif value[0] == "ID":
            if value[1] == "True" or value[1] == "False":
                instructions.append("PUSHB")
                instructions.append(value[1])
            else:
                instructions.append("LOAD")
                instructions.append(value[1])
                arguments += 1
        elif value[0] == "NUM":
            instructions.append("PUSHI")
            instructions.append(value[1])
            arguments += 1
        elif value[0] == "NUMF":
            instructions.append("PUSHF")
            instructions.append(value[1])
            arguments += 1
        if arguments == 2:
            instructions.append(operation)
            arguments = 1

    return instructions

bytecode = compile("""
                   
                   var number = 10 + 3 - 1 * 2 / 4;
                   if (number == 7)
                   (
                       print True,
                       print number,
                   );

                   """)
print(bytecode)
vm = VM()
vm.execute(bytecode)