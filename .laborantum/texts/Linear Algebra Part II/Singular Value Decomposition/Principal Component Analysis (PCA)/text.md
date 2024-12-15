# Principal Component Analysis (PCA)

### In this notebook you can find:

Download MNIST images dataset. Visualize several first images.

Represent the images in form of vectors and build a matrix
$X$ of shape $N \times M$, where $N$ is number of images
and $M$ is number of pixels.

Select only the images of zeros from this matrix.

For these images, calculate SVD decomposition.

Analyze the singular values, what can you see?

Visualize the first vector from $V$ (take the first
vector and reshape it to the original shape of image)
and then show this image (you can use `imshow` from 
`matplotlib`).

What can you see? What is this?

Plot second vector from matrix $V$. What does this
vector look like?

Find decomposition of all images on 50 first vectors
of $V$ and reconstruct the images based on these
first 50 coefficients.

Are the compressed images still look OK? What has changed?

Return reconstructed images as the answers for this task.

### The task

Do the same for all the other numbers. As the answers, return coefficients for the numbers from the full dataset.

Does the SVD compression work better when we use it for only one class of images?

Can we use the singular values that are built for class $y = 0$ for the
other classes? Does reconstruction for other classes the same as for the
class $y = 0$?

Experiment with different amount of dictionary size. When is the information reconstructed without any visible difference?
