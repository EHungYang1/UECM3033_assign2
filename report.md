UECM3033 Assignment #2 Report
========================================================

- Prepared by: E Hung Yang
- Tutorial Group:T3

--------------------------------------------------------

## Task 1 --  $LU$ Factorization or SOR method

The reports, codes and supporting documents are to be uploaded to Github at: 

https://github.com/EHungYang1/UECM3033_assign2

Explain your selection criteria here.
SOR method is more preferred in solving linear system when the matrix is sparse matrix. In numerical analysis, a sparse matrix is a matrix in which most of the elements are zero. If the nonzeros is greater than half of the length of matrix A then i will use LU method. 

Explain how you implement your `task1.py` here.
I refer to lecture notes. First i add in the iteration limit of 10(so that there will not have infinite loop) and omega as 1.03(assuming in SOR method). LU mehod is by using the A=LU => Ax=LUx=b. It also define as Ly=b and Ux=y. Then i add in np.array and astype to make A and b as a matrix and converting them to float. Then put in np.linalg.solve(A,b) to solve the matrix. 
---------------------------------------------------------

## Task 2 -- SVD method and image compression

<p><img alt="image.jpg" src="image.jpg"></p>

<p><img alt="image_30.jpg" src="image_30.jpg"></p>

How many non zero element in $\Sigma$?
800 non zero elemetns for three colors.

Put here your lower and better resolution pictures. Explain how you generate
these pictures from `task2.py`.

What is a sparse matrix?
In numerical analysis, a sparse matrix is a matrix in which most of the elements are zero. In contrast,a matrix where many elements are nonzero is called dense

At first, i created a svd function. Then i read the image and the image is then compressed by keeping the first 30 non zero elements as $\Sigma$ and set other non zero elements to zero. Repeat the process by using green and blue matrix. Then put in n=30 for lower resolution and n=200 for better resolution.

-----------------------------------

<sup>last modified: change your date here</sup>
