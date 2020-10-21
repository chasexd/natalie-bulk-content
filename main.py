import os


# Goal of the code ->  go about each sub directory and add git setup and push to org
name_of_organization = 'insights-test-org'

dirs = os.listdir('parentdir')
org_dir = os.getcwd()
print("HOLA")
print(name_of_organization)
print(os.getcwd())
os.chdir('parentdir')
print(os.getcwd())
for folder in dirs:
    os.chdir(org_dir+"/"+"parentdir"+"/"+folder)
    os.system('git init')
    os.system('touch 13.py')
    os.system('touch abc.txt')
    os.system('touch xyz.txt')
    os.system('git add .')
    os.system('git commit -am "Initial Commit"')
    os.system("gh repo create " + name_of_organization + "/" + folder + " --public --confirm")
    # print("gh repo create " + name_of_organization + "/" + folder + " --public --confirm")
    os.system("git push -u origin master")
    os.chdir(org_dir)

