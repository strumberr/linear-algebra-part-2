# Constructing a Matrix

You are given a set of eigen values and corresponding generalized eigen vectors in the form of Jordan Chain: $$\lambda_1, \lambda_2, \dots, \lambda_N$$ 
and
$$
\begin{matrix}
\mathbf x_1^1, \mathbf x_1^2, \dots \mathbf x^{\alpha_1}_1 \\
\vdots \\
\mathbf x_k^1, \mathbf x_k^2, \dots \mathbf x_k^{\alpha_k} \\
\end{matrix}
$$
$$M \mathbf x^m_k = \mathbf x^{m - 1}_k$$
Thus, every eigen $\lambda_k$ value can have a Jordan Chain of length $\alpha_k$.

Write a function that builds matrix with such eigen values and generalized eigen vectors.

Eigenvalues eigenvectors in matrices $J$ and $S$ should appear in the order they appear in input lists.

Your function should return: Jordan Matrix $J$, matrix 
of eigenvectors $S$ and the resulting matrix $A$.