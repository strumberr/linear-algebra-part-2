import json
import os
from pathlib import Path
import itertools

home_dir = Path(__file__).parent.resolve()

matrix_cycle = [1, 2, 3]


all_permutations = list(itertools.permutations(matrix_cycle))

positive_permutations = []
negative_permutations = []

for perm in all_permutations:

    inversions = sum(1 for i in range(len(perm)) for j in range(i + 1, len(perm)) if perm[i] > perm[j])
    if inversions % 2 == 0:
        positive_permutations.append(" ".join(map(str, perm)))
    else:
        negative_permutations.append(" ".join(map(str, perm)))

print(positive_permutations)
print(negative_permutations)



answer = {
        "2x2": {
            "+": sorted([
                "1 2",
                "2 1"
            ]),
            "-": sorted([
                ""
            ])
        },
        "3x3": {
            "+": sorted([
                "1 2 3",
                "2 3 1",
                "3 1 2"
                
            ]),
            "-": sorted([
                '1 3 2', 
                '2 1 3', 
                '3 2 1'
            ])
        },
        "4x4": {
            "+": sorted([
                '1 2 3 4', 
                '1 3 4 2', 
                '1 4 2 3', 
                '2 1 4 3', 
                '2 3 1 4', 
                '2 4 3 1', 
                '3 1 2 4', 
                '3 2 4 1', 
                '3 4 1 2', 
                '4 1 3 2', 
                '4 2 1 3', 
                '4 3 2 1'
            ]),
            
            "-": sorted([
                '1 2 4 3', 
                '1 3 2 4', 
                '1 4 3 2', 
                '2 1 3 4', 
                '2 3 4 1', 
                '2 4 1 3', 
                '3 1 4 2', 
                '3 2 1 4', 
                '3 4 2 1', 
                '4 1 2 3', 
                '4 2 3 1', 
                '4 3 1 2'
            ])
        }
    }

json.dump(
    answer, 
    open(home_dir/Path(".answer.json"), "w+"))