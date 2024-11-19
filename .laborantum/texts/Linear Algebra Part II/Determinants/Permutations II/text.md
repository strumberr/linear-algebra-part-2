# Permutations II

Write a program that calculates the determinant of a matrix and all the products leading to this value using permutation formula:

$$\det A = \sum_{\sigma \in P_N} \mathrm{sign} (\sigma) \prod_{i=1}^N a_{\sigma_i}$$

To get the list of all possible permutations, use `itertools.permutations`.

To check for the sign of a pertmutation, check lengths of all cycles in every permutation.