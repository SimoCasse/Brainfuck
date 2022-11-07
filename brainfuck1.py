class BrainfuckMachine:

    class BracketMismatch(Exception):
        pass

    class HeadOverflow(Exception):
        pass

    def __init__(self, tape_length):
        self.tape = [0] * tape_length
        self.head = 0
        self.code = None
        self.code_index = 0

    def run(self):
        while True:
            if self.code_index >= len(self.code):
                break
            self.use_function(self.code[self.code_index])

    def move_head(self, amount):
        self.head += amount
        if self.head >= len(self.tape) or self.head < 0:
            raise self.HeadOverflow

    def grow_tape(self):
        self.tape[self.head] += 1
        if self.tape[self.head] > 255:
            self.tape[self.head] = 0

    def lower_tape(self):
        self.tape[self.head] -= 1
        if self.tape[self.head] < 0:
            self.tape[self.head] = 255

    def last_bracket(self):
        i = 0
        while True:
            self.code_index += 1
            if self.code_index >= len(self.code):
                raise self.BracketMismatch
            elif self.code[self.code_index] == '[':
                i += 1
            elif self.code[self.code_index] == ']':
                if i == 0:
                    break
                else:
                    i -= 1

    def initial_bracket(self):
        i = 0
        while True:
            self.code_index -= 1
            if self.code_index < 0:
                raise self.BracketMismatch
            elif self.code[self.code_index] == ']':
                i += 1
            elif self.code[self.code_index] == '[':
                if i == 0:
                    break
                else:
                    i -= 1

    def use_function(self, command):
        
     match(command):
    
             case '>':
                    self.move_head(1)
                    self.code_index += 1
            
             case '<':
                    self.move_head(-1)
                    self.code_index += 1
             
             case '+':
                self.grow_tape()
                self.code_index += 1
            
             case '-':
                self.lower_tape()
                self.code_index += 1
            
             case '[':
                if self.tape[self.head] == 0:
                    self.last_bracket()
                self.code_index += 1
            
             case  ']':
                if self.tape[self.head] != 0:
                    self.initial_bracket()
                self.code_index += 1