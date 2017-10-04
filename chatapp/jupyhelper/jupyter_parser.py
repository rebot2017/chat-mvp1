import json
import shutil
import time
import subprocess
import os, os.path
class jupyter_helpers:
    def __init__(self):
        print("init helpers")

    def jupyter_parse_notebook(self, infile, outfile):
        print("Parsing File: %s"%infile)
        with open(infile, "r") as f:
            jsonF = json.loads(f.read())
            cells = jsonF["cells"]
            evalStr = ""
            for cell in cells:
                if cell["cell_type"] == "code":
                    code = cell["source"]
                    for line in code:
                        if line.find("jupyter_") >= 0:
                            continue
                        else:
                            evalStr+=line
            wfile =  open(outfile, 'w')
            wfile.write(evalStr)
            wfile.close()
            print("file parsed and written to %s."%outfile)
            curdir = os.getcwd()
            filetocopy = os.path.abspath(os.path.join(curdir, outfile))
            parentdir = os.path.abspath(os.path.join(curdir,os.pardir))
            parentdir = os.path.abspath(os.path.join(parentdir, os.pardir))
            scriptDir = os.path.abspath(os.path.join(parentdir, "chatscripts"))
            print("Depositing file in %s"%scriptDir)
            shutil.copy(filetocopy, scriptDir)
            time.sleep(1)
            print("Flushed file, committing")
            os.system("sudo bash /home/user/chat-mvp1/git.sh")
            print("committed to github")
            


    
