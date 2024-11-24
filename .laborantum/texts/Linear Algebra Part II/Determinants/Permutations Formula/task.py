import json
import os
from pathlib import Path

home_dir = Path(__file__).parent.resolve()

matrix_cycle = [1, 2, 3, 4]


result = []

n = len(matrix_cycle)

for i in range(n):

    matrix_cycle = matrix_cycle[1:] + [matrix_cycle[0]]
    # result.append(matrix_cycle)
    
    result.append(" ".join(map(str, matrix_cycle)))

print(result)

reversed_matrix_cycle = matrix_cycle[::-1]
n = len(reversed_matrix_cycle)

for i in range(n):
    
    reversed_matrix_cycle = reversed_matrix_cycle[1:] + [reversed_matrix_cycle[0]]
    # result.append(reversed_matrix_cycle)
    result.append(" ".join(map(str, reversed_matrix_cycle)))

print(result)


answer = {
        "2x2": {
            "+": sorted([
                "1 2",
                "2 1"
            ]),
            "-": sorted([
            ])
        },
        "3x3": {
            "+": sorted([
                "1 2 3",
                "2 3 1",
                "3 1 2"
                
            ]),
            "-": sorted([
                "2 1 3",
                "1 3 2",
                "3 2 1"
            ])
        },
        "4x4": {
            "+": sorted([
                "2 3 4 1", "3 4 1 2", "4 1 2 3", "1 2 3 4"
                
            ]),
            "-": sorted([
                "2 3 4 1", "3 4 1 2", "4 1 2 3", "1 2 3 4", "3 2 1 4", "2 1 4 3", "1 4 3 2", "4 3 2 1"
            ])
        }
    }

json.dump(
    answer, 
    open(home_dir/Path(".answer.json"), "w+"))