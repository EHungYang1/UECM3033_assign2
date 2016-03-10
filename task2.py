import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy.linalg as sp

def image_svd(n):
    img=mpimg.imread('image.jpg')
    [r,g,b] = [img[:,:,i] for i in range(3)]
    r_1,r_2,r_3 = sp.svd(r)
    g_1,g_2,g_3 = sp.svd(g)
    b_1,b_2,b_3 = sp.svd(b)
    r2_nonzero=(r_2!=0).sum()
    g2_nonzero=(g_2!=0).sum()
    b2_nonzero=(b_2!=0).sum()
    print("The number of non zero elements in decompose sigma of red, green, blue matrices are", r2_nonzero,"," ,g2_nonzero,"and" ,b2_nonzero, "respectively.")
    
    r_2[n:800]=np.zeros_like(r_2[n:800])
    g_2[n:800]=np.zeros_like(g_2[n:800])
    b_2[n:800]=np.zeros_like(b_2[n:800])
    
    # change the dimension to (800,1000) 
    r_2=sp.diagsvd(r_2,800,1000)
    g_2=sp.diagsvd(g_2,800,1000)
    b_2=sp.diagsvd(b_2,800,1000)
    
    #dot multiplication
    r_new=np.dot(r_1, np.dot(r_2,r_3))
    g_new=np.dot(g_1, np.dot(g_2,g_3))
    b_new=np.dot(b_1, np.dot(b_2,b_3))

    img[:,:,0]=r_new
    img[:,:,1]=g_new
    img[:,:,2]=b_new
    
    #plot the images
    fig = plt.figure(2)
    ax1 = fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,2,3)
    ax4 = fig.add_subplot(2,2,4)
    
    ax1.imshow(img)
    ax2.imshow(r, cmap = 'Reds')
    ax3.imshow(g, cmap = 'Greens')
    ax4.imshow(b, cmap = 'Blues')
    plt.show()
    
    #original image
    img=mpimg.imread('image.jpg')
    [r,g,b]=[img[:,:,i] for i in range(3)]
    fig=plt.figure(1)    
    ax1 =  fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,2,3)
    ax4 = fig.add_subplot(2,2,4)
    ax1.imshow(img)
    ax2.imshow(r, cmap = 'Reds')
    ax3.imshow(g, cmap = 'Greens')
    ax4.imshow(b, cmap = 'Blues')
    plt.show()
    
#low resolution picture of sigma 30    
image_svd(30)

#better resolution picture of sigma 200
image_svd(200)

