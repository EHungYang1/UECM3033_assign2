import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy as sp

def svd(n):
    # keep the non zero elements
    Sr1=Sr.copy()
    Sg1=Sg.copy()
    Sb1=Sb.copy()
    
    Sr1[n:800]=np.zeros_like(Sr[n:800])
    Sg1[n:800]=np.zeros_like(Sg[n:800])
    Sb1[n:800]=np.zeros_like(Sb[n:800])
    
    # change the dimension to (800,1000)  
    Sr1 = sp.linalg.diagsvd(Sr1,800,1000)
    Sg1 = sp.linalg.diagsvd(Sg1,800,1000)
    Sb1 = sp.linalg.diagsvd(Sb1,800,1000)
    
    #dot multiplication
    r_new = np.dot(np.dot(Ur,Sr1),Vr)
    g_new = np.dot(np.dot(Ug,Sg1),Vg)
    b_new = np.dot(np.dot(Ub,Sb1),Vb)
    
    img[:,:,0]= r_new
    img[:,:,1]= g_new
    img[:,:,2]= b_new
    
    #plot the images
    fig2 = plt.figure(n)
    ax1 = fig2.add_subplot(2,2,1)
    ax2 = fig2.add_subplot(2,2,2)
    ax3 = fig2.add_subplot(2,2,3)
    ax4 = fig2.add_subplot(2,2,4)
    ax1.imshow(img)
    ax2.imshow(r, cmap = 'Reds')
    ax3.imshow(g, cmap = 'Greens')
    ax4.imshow(b, cmap = 'Blues')
    plt.show()
    
#original image
img=mpimg.imread('image.jpg')
[r,g,b] = [img[:,:,i] for i in range(3)]
fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img)
ax2.imshow(r, cmap = 'Reds')
ax3.imshow(g, cmap = 'Greens')
ax4.imshow(b, cmap = 'Blues')
plt.show()

#find U, sigma and V for red,green and blue matrix
Ur, Sr, Vr = sp.linalg.svd(r)
Ug, Sg, Vg = sp.linalg.svd(g)
Ub, Sb, Vb = sp.linalg.svd(b)

#find non zero elements in sigma of red, green and blue matrix
nonzero_r=np.count_nonzero(Sr)
nonzero_g=np.count_nonzero(Sg)
nonzero_b=np.count_nonzero(Sb)

print("The number of non zero elements in original sigma of red, green, blue matrices are", nonzero_r,"," ,nonzero_g,"and" ,nonzero_b, )

#low resolution picture of sigma 30
svd(30)

#better resolution picture of sigma 200
svd(200)

