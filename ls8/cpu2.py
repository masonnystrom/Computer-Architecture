"""CPU functionality."""

import sys

LDI = 0b10000010 
PRN = 0b01000111 # Print
HLT = 0b00000001  # Halt
MUL = 0b10100010  # Multiply
ADD = 0b10100000  # Addition
SUB = 0b10100001 # Subtraction
DIV = 0b10100011 # Division
PUSH = 0b01000101 # Stack Push
POP = 0b01000110 # Stack Pop
SP = 7 # Stack pointer

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.reg = [0] * 8
        self.ram = [0] * 256
        self.reg[7] = 0xF4
        self.pc = 0
        self.halted = False

    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, val, address):
        self.ram[address] = val

    def load(self, filename):
        """Load a program into memory."""
        address = 0
        with open(filename) as fp:
            for line in fp:
                comment_split = line.split("#")
                num = comment_split[0].strip()
                if num == '':  # ignore blanks
                    continue
                val = int(num, 2)
                self.ram_write(val, address)
                address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        while not self.halted:
            instruction_to_execute = self.ram_read(self.pc)
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)
            self.execute_instruction(instruction_to_execute, operand_a, operand_b)

    def execute_instruction(self, instruction, operand_a, operand_b):
        if instruction == HLT:
            self.halted = True
            self.pc += 1
        elif instruction == LDI:
            self.reg[operand_a] = operand_b
            self.pc += 3
        elif instruction == PRN:
            print(self.reg[operand_a])
            self.pc += 2
        elif instruction == MULT:
            print(self.reg[operand_a])
            self.pc *= 3