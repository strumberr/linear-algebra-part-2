# Solving Inverse Problems with SVD

I have encoded a message (in form of an image of size $20 \times 20$) in the following way:

1) flattened the image to get a vector $\mathbf x$
2) created a raytracing matrix $A$
3) calculated $\mathbf b = A \mathbf x$

Unfortunately, there is some noise in $\mathbf b$
due to which reconstructing the initial image will be tough.

You are given matrix $A$
and a vector $\mathbf b$.

Write a program that reconstructs $\mathbf x$.

Output images that correspond to $\mathbf x$
for every $16$ singular vectors.

Plot all the images in the result. What is written on the image?

How the reconstruction process runs? What is happening with the result? Why does it happen? Can you understand, what was the original message? Can you understand, what was the emoji?

Visualize components from the matrix $V$. What can you say about the structure of the singular values? Which of the singular values carry the important information for reconstruction?

Which of the vectors correspond to the low-frequency information? What does the high-frequency information correspond to? Why cannot we reconstruct the complete original image?