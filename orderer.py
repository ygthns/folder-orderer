import os,glob,itertools,os.path,sys

directory =input("Where would you like to put it in an order? Write your path between single quotes please(E.g '/Users/ygthns/Desktop/deneme'): ")

#In order to check if there is such a path or not
if(os.path.isdir(directory)==False):
    print("There is no such a directory in mentioned path")
    sys.exit()

#creating variables
file_list=[]
base_names=list()
full_list=[]

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
file_list.sort()

print(file_list)
#The main process
for i in range(file_len):

    os.chdir(directory) #Change the working directory
    if(os.path.isdir(base_names[i])==False):
        os.system('mkdir '+base_names[i]) #Creates a new folder


    new_directory=(directory+'/'+base_names[i])
    os.chdir(new_directory)
    if(os.path.isfile(file_list[i])==False):
        os.chdir(directory)
        os.system('mv '+file_list[i]+' '+base_names[i]) #Move the first file to newly created folder
    else:
        os.chdir(directory)
print("Mission accomplished, please check your directory. There might be some minor errors for directories which contains '.' between words!")

  #  if (base_names[i]==base_names[i+1]):
   #     os.system('mv '+file_list[i+1]+' '+base_names[i]) #Move the other files to folder ,that we mentioned above, which have the same names.



