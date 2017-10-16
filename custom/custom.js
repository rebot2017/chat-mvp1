
if($(IPython.toolbar.selector.concat(' > #kill-run-all')).length == 0){
  IPython.toolbar.add_buttons_group([
        {
             'label'   : 'run all',
             'icon'    : 'fa fa-play',
             'callback': function(){
                 IPython.notebook.kernel.restart();
                 $(IPython.events).one('kernel_ready.Kernel',
                                       function(){IPython.notebook.execute_all_cells();});
             }
        }
    ], 'kill-run-all');
}

var commit_cell = function(code){
       var nb = Jupyter.notebook

    // create cell at top
    nb.select(0)
    nb.insert_cell_above()

    // select cell below (the one we have created)
    var cell = nb.select(0).get_selected_cell()
    var name = nb.notebook_name
    code = code.replace("{0}", nb.notebook_name)
    code = code.replace("{1}", name.split('.')[0] + ".py")
    // set text in the cell
    cell.set_text(code)

    // execute cell
   console.log("mounted cell. Executing commit hooks.");
    cell.execute()
console.log(cell);
console.log("executed, deleting cell")
$(cell.events).one('finished_execute.CodeCell', function(){setTimeout(function(){Jupyter.notebook.delete_cell(0);},3000);});
}

if($(IPython.toolbar.selector.concat(' > #commit-to-git')).length == 0){
  IPython.toolbar.add_buttons_group([
        {
             'label'   : 'commit',
             'icon'    : 'fa fa-github',
             'callback': function(){
		console.log("update3");
                console.log("update1");
                commit_cell(
`
import sys
if "/home/user/chat-mvp1/chatapp" not in sys.path:
	sys.path.append("/home/user/chat-mvp1/chatapp")
from jupyhelper import jupyter_parser 
jp = jupyter_parser.jupyter_helpers()
jp.jupyter_run("{0}", "{1}")
`
)
             }
        }
    ], 'commit-to-git');
}

var hidePrompt = function(){$(".input_prompt").hide(); console.log($(".input_prompt")); console.log("hideinput");}
$(Jupyter.events).one("kernel_ready.Kernel",hidePrompt);
$(Jupyter.events).one("create.Cell", function(){hidePrompt();});
