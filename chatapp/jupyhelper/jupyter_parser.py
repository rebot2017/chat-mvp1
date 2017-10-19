import json
import shutil
import time
import subprocess
import os, os.path
class jupyter_helpers:
    def __init__(self):
        print("Starting the committing process. Please wait.")

    def jupyter_run(self, infile, outfile):
        self.jupyter_parse_notebook(infile, outfile)
        self.jupyter_copy_script(outfile)
       # self.jupyter_commit()
    
    def jupyter_parse_notebook(self, infile, outfile):
        print("Parsing File: %s"%infile)
        with open(infile, "r") as f:
            jsonF = json.loads(f.read())
            cells = jsonF["cells"]
            evalStr = ""
            for cell in cells:
                if cell["cell_type"] == "code" and "j_ignore" not in cell["metadata"]:
                    code = cell["source"]
                    for line in code:
                        if line.find("jupyter_") >= 0 or line.find("j_ignore_") >= 0:
                            continue
                        else:
                            evalStr+=line
                            if not line.endswith('\n'):
                                evalStr+='\n'
            with open("append.txt", 'r') as f:
                lines = f.readlines()
                for line in lines:
                    evalStr += line
            wfile =  open(outfile, 'w')
            wfile.write(evalStr)
            wfile.close()
            print("file parsed and written to %s."%outfile)
            
    
    def jupyter_copy_script(self, outfile):
        team_num = self.get_curr_folder()
        curdir=os.getcwd()
        filetocopy = os.path.abspath(os.path.join(curdir, outfile))
        parentdir = os.path.abspath(os.path.join(curdir,os.pardir))
        parentdir = os.path.abspath(os.path.join(parentdir, os.pardir))
        scriptDir = os.path.abspath(os.path.join(parentdir, "chatscripts"))
        print("Depositing file in %s"%scriptDir)
        shutil.copy(filetocopy, scriptDir+"/%s_"%team_num+outfile)
        print("Copied File")
    
    def get_curr_folder(self):
        curdir = os.getcwd()
        folders = curdir.split('/')
        team_num = folders[len(folders)-1]
        return team_num


    def jupyter_commit(self):
        time.sleep(1)
        print("committing...")
        team_num = self.get_curr_folder()
        os.system("bash /home/user/chat-mvp1/git.sh "+team_num)
        print("committed to github")
    
    def jupyter_deploy(self, infile, outfile, argument=""):
        TEST_FILE_NAME = "jupyter_test_file.py"
        self.jupyter_parse_notebook(infile, TEST_FILE_NAME)
        print("Written file to %s. Evaluating..."%(TEST_FILE_NAME))
        with open(TEST_FILE_NAME, 'r') as f:
            file_content = f.readlines()
            file_str = ""
            for line in file_content:
                file_str += line
            try:    
                eval(file_str)
                jupyter_run(infile, outfile)
            except SyntaxError as e:
                print("Syntax Errors detected. Please correct them before committing.")
            
