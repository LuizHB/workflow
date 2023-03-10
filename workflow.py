import os
readmefile=open('readme.md','w')
dir_ignore=['.git','.github']
dit={}

for dirname, dirnames, filenames in os.walk('.'):  
    #leaving the exceptional folders
    if any(dir_ignore_name in dirname for dir_ignore_name in dir_ignore):
        continue    
    #renaming folder names
    for subdirname in dirnames:
        print(subdirname)
        if ".git" not in subdirname:
            new_dirname=subdirname.replace(' ','_')
            os.rename(subdirname,new_dirname)
    for filename in filenames:
        if '.git' not in dirname:
            dir_name=dirname[2:]
            new_name=filename
            #rename all filenames to camelcase
            if filename.endswith('.py') or filename.endswith('.Py'):
                print("yes")
                new_name=filename.replace('_',' ').title().replace(' ','').replace('.Py','.py')
                print(new_name)
                os.rename(os.path.join(dirname,filename),os.path.join(dirname,new_name))
            if dir_name not in dit and dir_name != '':
                dit[dir_name]=[new_name]
            elif dir_name in dit and dir_name != '':
                dit[dir_name].append(new_name)
        
print(dit)
# write relative link and names to readme.md
for key,value in dit.items():
    readmefile.write(' ## [{}]({})\n'.format(key,key))
    for i in value:
        readmefile.write('*  [{}]({}/{})\n'.format(i,key,i))
readmefile.close()
