from PIL import Image
path = "C:\\Users\\HP\\Desktop\\Gökçe_Yağmur_BUDAK_21732948\\urban.jpg" # Your image path
pathoutput= "C:\\Users\\HP\\Desktop\\Gökçe_Yağmur_BUDAK_21732948\\urban_output3.jpg"
img = Image.open(path)
img2 = Image.new(img.mode,img.size,color=0)
width,height=img.size
pixel=img.load()
members = [0,0,0,0,1.5,0,0,0,0]
newimg = Image.new("L",(width,height),"white")
for i in range(1,width-1):
    for j in range(1,height-1):
        img2.putpixel((i,j),pixel[i,j])
        img_members=[0,0,0,0,0,0,0,0,0]

        img_members[0] = img.getpixel((i-1,j-1))
        img_members[1] = img.getpixel((i-1,j))
        img_members[2] = img.getpixel((i-1,j+1))
        img_members[3] = img.getpixel((i,j-1))
        img_members[4] = img.getpixel((i,j))
        img_members[5] = img.getpixel((i,j+1))
        img_members[6] = img.getpixel((i+1,j-1))
        img_members[7] = img.getpixel((i+1,j))
        img_members[8] = img.getpixel((i+1,j+1))

        total=(img_members[0]*members[0]+img_members[1]*members[1]+img_members[2]*members[2]+img_members[3]*members[3]+img_members[4]*members[4]+img_members[5]*members[5]+img_members[6]*members[6]+img_members[7]*members[7]+img_members[8]*members[8])
        
        
        img2.putpixel((i,j),int(total*(1.5/9)))

img2.save(pathoutput)
        
