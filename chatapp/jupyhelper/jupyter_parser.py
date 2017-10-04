import json
import shutil
import os, os.path
class jupyter_helpers:
    def __init__(self):
        print("init helpers")

    def jupyter_parse_notebook(self, infile, outfile):
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
            curdir = os.getcwd()
            filetocopy = os.path.abspath(os.path.join(curdir, outfile))
            parentdir = os.path.abspath(os.path.join(curdir,os.pardir))
            parentdir = os.path.abspath(os.path.join(parentdir, os.pardir))
            print(parentdir)
            scriptDir = os.path.abspath(os.path.join(parentdir, "chatscripts"))
            
            shutil.copy(filetocopy, scriptDir)


    