# add the main project folder to the path
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mouseKeyAuto.main import ElementList

list_obj = ElementList()

list_obj.append_mouse_moveRel((10,50))
list_obj.append_delay(100)
list_obj.append_mouse_moveRel((10,50))
list_obj.append_delay(100)
list_obj.append_mouse_moveRel((10,50))
list_obj.append_delay(100)
list_obj.append_mouse_SingleClick_right()
list_obj.append_mouse_moveRel((10,50))
list_obj.append_delay(100)

list_obj.print_list()

list_obj.execute_list()