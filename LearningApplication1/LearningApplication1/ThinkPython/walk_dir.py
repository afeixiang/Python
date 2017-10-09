'''
Given a dircetory and list all files that contained in the directory and subdirectories.
'''
import os

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)

walk('\\\\anglicare-sa.org.au\\files\\frank.wang\\My Documents\\Learning\\Python\\LearningApplication1\\LearningApplication1')