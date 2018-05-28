import os

path = r"E:\job bcs"

##########MARKDOWN RUNABLE CODE#######################
def md(path):
    for dirpath, dirnames, filenames in os.walk(path):
        print("## Parent dir: ({})[{}]" .format(os.path.basename(dirpath), dirpath))
        for i in filenames:
            print("Files: ({})[{}]" .format(i, os.path.join(dirpath,i)))
        for x in dirnames:
            print("Folders: ({})[{}]" .format(x, os.path.join(dirpath,x)))
        print()

###########HTML RUNABLE CODE#############
def html(path):
    for dirpath, dirnames, filenames in os.walk(path):
        print("<h2> Parent dir: <a href= \"{}\"> {} </a> </h2>".format(dirpath, os.path.basename(dirpath)))
        for i in filenames:
            print("<h4> Files: <a href= \"{}\"> {} </a> </h4>".format(os.path.join(dirpath,i), i))
        print
        for x in dirnames:
            print("<h4> Folders: <a href= \"{}\"> {} </a> </h4>".format(os.path.join(dirpath,x), x))
        print()

