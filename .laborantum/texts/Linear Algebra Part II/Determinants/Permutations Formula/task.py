import json
import os
from pathlib import Path

home_dir = Path(__file__).parent.resolve()

answer = {
        "2x2": {
            "+": sorted([
### YOUR CODE HERE ###
            ]),
            "-": sorted([
### YOUR CODE HERE ###
            ])
        },
        "3x3": {
            "+": sorted([
### YOUR CODE HERE ###
            ]),
            "-": sorted([
### YOUR CODE HERE ###
            ])
        },
        "4x4": {
            "+": sorted([
### YOUR CODE HERE ###
            ]),
            "-": sorted([
### YOUR CODE HERE ###
            ])
        }
    }

json.dump(
    answer, 
    open(home_dir/Path('.answer.json'), "w+"))