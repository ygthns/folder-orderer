import os,glob,itertools,os.path,sys

directory =input("Where would you like to put it in an order? Write your path between single quotes please(E.g '/Users/ygthns/Desktop/deneme'): ")

#In order to check if there is such a path or not
#if(os.path.isdir(directory)==False):
 #   print("There is no such a directory in mentioned path")
  #  sys.exit()

#creating variables
file_list=[]
base_names=list()
full_list=[]
x=0
os.chdir(directory)
os.system('pwd')

full_list=os.listdir(directory)
if '.DS_Store' in full_list:
   full_list.remove('.DS_Store')
for f in full_list:

    if(os.path.isdir(f)==False):
        file_list.append(f)
file_len=(len(file_list))



for i in range(file_len):
    base_names.append(os.path.splitext(file_list[i])[0])

#To sort files in an order.
base_names.sort()
#file_list.sort(key=os.path.getctime)
file_list.sort()

for i in file_list:
    #first_name=('"'+directory+'/'+i+'"')
    #new_name=('"'+directory+'/MHS_'+'{}'.format(x)+'_'+i+'"')
    my_dest ="image_" + str(x) + '_' + ".jpg"
    my_source =directory + i
    my_dest =directory + my_dest
    print(my_source)
    print(my_dest)
    os.rename(my_source,my_dest)
    x=x+1


#for file in os.listdir("/Users/ygthns/Desktop/rename"):
#	os.rename(file, f"/Users/ygthns/Desktop/rename/old_{file}")

'''
import os
# Function to rename multiple files
def main():
   i = 0
   path="/Users/ygthns/Desktop/rename/"
   for filename in os.listdir(path):
      my_dest ="MHS_" + str(i) + ".jpg"
      my_source =path + filename
      my_dest =path + my_dest
      # rename() function will
      # rename all the files
      os.rename(my_source, my_dest)
      i += 1
# Driver Code
if __name__ == '__main__':
   # Calling main() function
   main()
   '''