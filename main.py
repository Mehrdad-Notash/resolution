import cv2, glob
import numpy as np
import resolution

fileA = glob.glob("data/source/*")
fileB = glob.glob("data/target/*")  #name of file in A,B must to be same!


def __name__ == "__main__":    
    #a =np.zeros((306,720,1280,3))
    #b =np.zeros((306,720,1280,3))  #->image size맞게 조정
    for filename in fileA:
        a[i] = cv2.imread(filename)
        b[i] = cv2.imread("data/target/"+filename[12:])
    
    a = (a - 127.5) 
    a = a / 127.5
    b = (b - 127.5) 
    b = b / 127.5
    a = a[:,:,:,::-1]
    b = b[:,:,:,::-1]
    #a,b에 순서대로 프레임이들어간다고 가정
    


    #print('Loaded', dataset[0].shape, dataset[1].shape)
    image_shape = (512,512,3) #make 512 512 images

    d_model = resolution.define_discriminator(image_shape)
    g_model = resolution.define_generator(image_shape)
    gan_model = resolution.define_gan(g_model, d_model, image_shape)

    train(d_model, g_model, gan_model, a, b)






