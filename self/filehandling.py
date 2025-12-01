"""#in read mode
vignesh=open('vignesh.txt',mode ='r')
print(vignesh.read())
vignesh.close()"""

"""#in write mode
vignesh=open('vignesh.txt',mode ='w')
vignesh.write('I am in Banglore')
vignesh.close()"""

#in append mode
vignesh=open('vignesh.txt',mode ='a')
vignesh.write('for learning full stack')
vignesh.close()



