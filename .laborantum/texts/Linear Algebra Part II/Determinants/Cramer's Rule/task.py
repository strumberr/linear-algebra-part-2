import json
import numpy as np
import os

from pathlib import Path

home_dir = Path(__file__).parent.resolve()

answer = {
    "task1": {
        "det_A_terms": sorted([
### YOUR CODE HERE ###
        ]),
        "det_A_1_terms": sorted([
### YOUR CODE HERE ###
        ]),
        "det_A_2_terms": sorted([
### YOUR CODE HERE ###
        ]),
        "x": np.array(
### YOUR CODE HERE ###
        ),
        "cofactors": np.array(
### YOUR CODE HERE ###
        ),
        "inverse": np.array(
### YOUR CODE HERE ###
        )
    },
    "task2": {
        "det_A_terms": sorted([
### YOUR CODE HERE ###
        ]),
        "det_A_1_terms": sorted([
### YOUR CODE HERE ###
        ]),
        "det_A_2_terms": sorted([
### YOUR CODE HERE ###
        ]),
        "x": np.array(
### YOUR CODE HERE ###
        ),
        "cofactors": np.array(
### YOUR CODE HERE ###
        ),
        "inverse": np.array(
### YOUR CODE HERE ###
        )
    },
    "task3": {
        "det_A_terms": sorted([
### YOUR CODE HERE ###
        ]),
        "det_A_1_terms": sorted([
### YOUR CODE HERE ###
        ]),
        "det_A_2_terms": sorted([
### YOUR CODE HERE ###
        ]),
        "x": np.array(
### YOUR CODE HERE ###
        ),
        "cofactors": np.array(
### YOUR CODE HERE ###
        ),
        "inverse": np.array(
### YOUR CODE HERE ###
        )
    }
}

json.dump(
    answer, 
    open(home_dir/Path('.answer.json'), "w+"))