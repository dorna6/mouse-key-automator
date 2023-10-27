# add the main project folder to the path
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from pynput.mouse import Button, Controller

# mouse = Controller()
# print ("Current position: " + str(mouse.position))

import mouseKeyAuto.elements as elms

a1 = elms.Element_MouseMoveAbs((100,100))
data = a1.get_data()
print(data)