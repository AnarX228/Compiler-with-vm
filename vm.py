class VM:
    def __init__(self):
        self.stack = []
        self.memory = {}

    def execute(self, bytecode):
        pc = 0
        while pc < len(bytecode):
            if bytecode[pc] == "PUSHI":
                self.stack.append(int(bytecode[pc + 1]))
                pc += 2
            elif bytecode[pc] == "PUSHB":
                self.stack.append(bool(bytecode[pc + 1]))
                pc += 2
            elif bytecode[pc] == "PUSHL":
                self.stack.append(list(bytecode[pc + 1]))
                pc += 2
            elif bytecode[pc] == "POP":
                if self.stack:
                    self.stack.pop()
                pc += 1
            elif bytecode[pc] == "ADD":
                if len(self.stack) < 2:
                    print("Ошибка: недостаточно элементов в стеке для ADD")
                    return
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a + b)
                pc += 1
            elif bytecode[pc] == "SUB":
                if len(self.stack) < 2:
                    print("Ошибка: недостаточно элементов в стеке для SUB")
                    return
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a - b)
                pc += 1
            elif bytecode[pc] == "MUL":
                if len(self.stack) < 2:
                    print("Ошибка: недостаточно элементов в стеке для MUL")
                    return
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a * b)
                pc += 1
            elif bytecode[pc] == "DIV":
                if len(self.stack) < 2:
                    print("Ошибка: недостаточно элементов в стеке для DIV")
                    return
                b = self.stack.pop()
                a = self.stack.pop()
                if b == 0:
                    print("Ошибка: деление на ноль")
                    return
                self.stack.append(a / b)
                pc += 1
            elif bytecode[pc] == "STORE":
                if self.stack:
                    self.memory[bytecode[pc + 1]] = self.stack[-1]
                pc += 2
            elif bytecode[pc] == "LOAD":
                if bytecode[pc + 1] in self.memory:
                    self.stack.append(self.memory[bytecode[pc + 1]])
                else:
                    print(f"Ошибка: переменная '{bytecode[pc + 1]}' не найдена")
                pc += 2
            elif bytecode[pc] == "EQUALS":
                if len(self.stack) < 2:
                    print("Ошибка: недостаточно элементов в стеке для EQ")
                    return
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a == b)
                pc += 1
            elif bytecode[pc] == "GREATER":
                if len(self.stack) < 2:
                    print("Ошибка: недостаточно элементов в стеке для GREATER")
                    return
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a > b)
                pc += 1
            elif bytecode[pc] == "LESS":
                if len(self.stack) < 2:
                    print("Ошибка: недостаточно элементов в стеке для LESS")
                    return
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a < b)
                pc += 1
            elif bytecode[pc] == "IF":
                if len(self.stack) < 1:
                    print("Ошибка: недостаточно элементов в стеке для IF")
                    return
                b = self.stack.pop()
                if b:
                    self.execute(bytecode[pc+1])
                pc += 2
            elif bytecode[pc] == "PRINT":
                if self.stack:
                    print(self.stack[-1])
                else:
                    print("Ошибка: стек пуст")
                pc += 1