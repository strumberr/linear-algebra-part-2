# Diagonalising Bilinear Forms

For the following bilinear forms:

1) Write out symmetric matrix $A$ that corresponds to the bilinear form $\mathbf x^T A \mathbf x$ in form of `numpy.ndarray`
1) Diagonalize the bilinear form using Normal Jordan Form
    (Canonical Decomposition) of matrix $A$, as an answer, write out:
    
    1) Characteristical polynome coefficients of the matrix $A$ ($\det A - \lambda I$), from the one that corresponds to the largest power of $\lambda$ to the one that corresponds to the smallest one. Example: for polynome $\lambda^2 + 2 \lambda + 3$, the answer will be `[1, 2, 3]`.
    
    2) Matrix of eigen values $\Lambda$ and matrix of eigen vectors $Q$, the eigen values should be ordered
    in descending order. 
    
        Vectors that make up matrix $Q$ should start from nonnegative value and first coordinates for similar
        eigen values should be ordered in descending order.
    
        You can check yourself: $Q$ and $\Lambda$ should recombine in matrix $A$
    
    3) Write out matrix $C$ which will be used in change of coordinates $\mathbf y = C \mathbf x$ to diagonalize $A$.
    
    4) Write out coefficients $d_1, d_2, \dots, d_N$ in diagonal form of $A$ in new variables $\mathbf y$:
    $$\mathbf x^T A \mathbf x = d_1 y_1^2 + d_2 y_2^2 + \dots + d_N y_N^2$$
    
    5) From the eigen values found above, write:
        * `+` if matrix is positive definite 
        * `-` if matrix is negative definite
        * `0+` if matrix is positive semidefinite
        * `0-` if matrix is negative semidefinite
        * `+-` if matrix is not definite

1) Diagonalize the bilinear form using LDL decomposition of matrix $A$, write out:
    
    1) Matrix of pivots $D$ and lower triangular matrix $L$
    
        The pivots should be ordered
        in descending order.
        
        Matrix $L$ should have $1$ on main diagonal.

        You can check yourself: $L$ and $D$ should recombine into $A$.

    3) Write out matrix $C$ which will be used in change of coordinates $\mathbf y = C \mathbf x$ to diagonalize $A$.

    4) Write out coefficients $d_1, d_2, \dots, d_N$ in diagonal form of $A$ in new variables $\mathbf y$:
    $$\mathbf x^T A \mathbf x = d_1 y_1^2 + d_2 y_2^2 + \dots + d_N y_N^2$$

    5) Based on the pivots found above, write:
        * `+` if matrix is positive definite 
        * `-` if matrix is negative definite
        * `0+` if matrix is positive semidefinite
        * `0-` if matrix is negative semidefinite
        * `+-` if matrix is not definite

3) Write out all upper-left determinants:
    
    1) Write all terms that make the determinants (in descending order)

    2) Based on the determinants found above, write:
        * `+` if matrix is positive definite 
        * `-` if matrix is negative definite
        * `0+` if matrix is positive semidefinite
        * `0-` if matrix is negative semidefinite
        * `+-` if matrix is not definite

You may use `numpy` library to compute the answers,
but make sure that you understand, how every algorithm
works inside.

The bilinear forms:

1. $
    \begin{bmatrix}
        3 & 1 \\
        1 & 3
    \end{bmatrix}$

1. $\begin{bmatrix}
    -6 & -2 \\
    -2 & -9
    \end{bmatrix}$

<!-- 1. $\frac{1}{3}
    \begin{bmatrix}
    7 & -2 & -1\\
    -2 &  7 & -1\\
    -1 & -1 &  4
    \end{bmatrix}$ -->

1. $\begin{bmatrix}
    2 & 1 & 1\\
    1 & 2 & 1\\
    1 & 1 & 2
    \end{bmatrix}$

<!-- 3. $\begin{bmatrix}
    -5 & 1 & -2 \\
    1 & -5 & -2 \\
    -2 & -2 & -2
    \end{bmatrix}$ -->