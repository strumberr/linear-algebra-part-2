# Carnivores and Herbivores Populations

There are two populations, carnivores ($c$) and herbivores ($h$) existing in a biosystem (suppose they can be negative in terms that $c$ and $h$ are the deviations from the equilibrium state).

Population of carnivores changes over time according to the following equation:
$$\dot c = c + h$$

Thus, the more there is prey -- the better carnivores feel and the more there are carnivores -- the faster they breed.

Population of herbivores changes over time according to the following equation:

$$\dot h = - 2c - h$$

The more there are herbivores -- the less herbs are there in the forest (and thus less food), and the more there are carnivores, the more the herbivores are condumed.

In the initial moment of time there are $100$ extra carnivores and $100$ extra herbivores. Find:

* Write out system of DE in matrix form:
$$
\frac{\partial }{\partial t}
\begin{bmatrix}
c \\
h
\end{bmatrix} = 
A
\begin{bmatrix}
c \\
h
\end{bmatrix}$$

* Write out eigen values and vectors of matrix $A$ in DE and check that these eigenvalues and eigenvectors recosntruct the original matrix $A$ 
* Write out the general solution of the DE using eigen values and eigen vectors (if $t$ is numpy array of shape $1 \times N$, the function should output populations of shape $2 \times N$ for every moment of time)
* Write out the general solution of the DE using matrix exponent
* Find coefficients for general solution corresponding to intial conditions
* Plot populations of carnivores and herbivores over time
* Are there initial conditions when both populations eventually reach equilibrium?
* Are there initial conditions that eventually will lead to catastrophe?
* Think about an example of matrix $A$ when both populations eventually fade regardless of the initial conditions. Build that matrix
* Think about an example of matrix $A$ when both populations eventually reach equilibrium. Build such matrix
