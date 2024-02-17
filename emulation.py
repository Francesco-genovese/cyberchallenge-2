#!/bin/env python3

import sys

# Se vuoi leggere/scrivere da file decommenta qua
fin = open("input.txt", "r")  # File di input fornito dalla piattaforma
fout = open("output.txt", "w")  # File di output fornito dalla piattaforma

# Se vuoi leggere/scrivere da linea di comando decommenta qua
# fin = sys.stdin  # File di input fornito dalla piattaforma
# fout = sys.stdout  # File di output fornito dalla piattaforma

def emulate(code):
    variables = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0}
    labels = {}
    i = 0

    while i < len(code):
        tokens = code[i].split()
        op = tokens[0]

        if op == 'lab':
            label_name = tokens[1]
            labels[label_name] = i
        elif op == 'jmp':
            if len(tokens) == 2:  # Jump to label directly
                label_name = tokens[1]
                if label_name in labels:
                    i = labels[label_name] - 1  # Decremento perché verrà incrementato dopo il loop
            elif len(tokens) == 4:  # Jump to label based on variable
                var = tokens[1]
                num = variables.get(var, 0)
                label_name = tokens[3]
                if num == int(tokens[2]) and label_name in labels:
                    i = labels[label_name] - 1  # Decremento perché verrà incrementato dopo il loop

        else:
            var = tokens[1]
            num = int(tokens[2])

            if var in variables:
                if op == 'add':
                    variables[var] += num
                elif op == 'sub':
                    variables[var] -= num
                elif op == 'mul':
                    variables[var] *= num

        i += 1

    return sum(variables.values())

# Leggi da file di input
with open("input.txt", "r") as fin:
    N = int(fin.readline().strip())
    code = [fin.readline().strip() for _ in range(N)]

# Esegui la simulazione
result = emulate(code)

# Scrivi su file di output
with open("output.txt", "w") as fout:
    fout.write(str(result) + "\n")
