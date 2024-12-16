# Computing Diagonalized Form

You are given a symmetric matrix $A$.

Using `numpy.linalg`, compute:

1) $Q$ and $\Lambda$. Eigen values should be ordered in descending order, and vectors $Q$ should start with nonnegative first coordinate
    
2) $L$ and $D$. Pivots should be ordered in the order that ensures numerical stability of PLU decomposition.
    
3) Check definetness of the matrix, return:
    * `+` if matrix is positive definite 
    * `-` if matrix is negative definite
    * `0+` if matrix is positive semidefinite
    * `0-` if matrix is negative semidefinite
    * `+-` if matrix is not definite

Note that PLU decomposition yields not only matrices $L$ and $U$, but also a permutation matrix $P$. This matrix should be taken into account in your answer