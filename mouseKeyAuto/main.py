import mouseKeyAuto.elements as elms
import mouseKeyAuto.utils as utl
import pynput 
import time


# SECTION: element list class
class ElementList():
    def __init__(self):
        self.element_list = [] # init empty element list
      
    def get_list(self):
        return self.element_list
    
    def print_list(self):
        i=0
        for line in self.element_list:
            print(f'[{i}], {line.get_type():32}, {line.get_data()}')
            i=i+1
            
    def append_mouse_moveAbs(self,abs_pos):
        ielem = elms.Element_MouseMoveAbs(abs_pos)
        self.element_list.append(ielem)
        
    def append_mouse_moveRel(self,rel_pos):
        ielem = elms.Element_MouseMoveRel(rel_pos)
        self.element_list.append(ielem)

    def append_mouse_SingleRightClick(self):
        ielem = elms.Element_MouseClickRight(1)
        self.element_list.append(ielem)
        
    def append_mouse_SingleClick_right(self):
        ielem = elms.Element_MouseClickRight(1)
        self.element_list.append(ielem)
 
    def append_mouse_SingleClick_left(self):
        ielem = elms.Element_MouseClickLeft(1)
        self.element_list.append(ielem)

    def append_mouse_DoubleClick_left(self):
        ielem = elms.Element_MouseClickLeft(2)
        self.element_list.append(ielem)

    def append_delay(self,time_millis):
        ielem = elms.Element_Delay(time_millis)
        self.element_list.append(ielem)



# SECTION: execute secion
    def execute_list(self):
        
        for line in self.element_list:
            itype = line.get_type()
            
            if itype == utl.ElementType.MOUSE_MOVE_ABS:
                # read parameters
                idata = line.get_data()
                abs_pos = idata['abs_position']
                
                # execution 
                mouse = pynput.mouse.Controller()    
                mouse.position(abs_pos)

            elif itype == utl.ElementType.MOUSE_MOVE_REL:
                # read parameters
                idata = line.get_data()
                rel_pos = idata['rel_position']
                
                # execution
                mouse = pynput.mouse.Controller()    
                mouse.move(rel_pos[0], rel_pos[1])
            
            elif itype == utl.ElementType.MOUSE_CLICK_RIGHT:
                # read parameters
                idata = line.get_data()
                num_of_clicks = idata['num_of_clicks']
                
                # execution
                mouse = pynput.mouse.Controller()    
                mouse.click(pynput.mouse.Button.right, num_of_clicks)
            
            elif itype == utl.ElementType.MOUSE_CLICK_LEFT:
                # read parameters
                idata = line.get_data()
                num_of_clicks = idata['num_of_clicks']
                
                # execution
                mouse = pynput.mouse.Controller()    
                mouse.click(pynput.mouse.Button.left, num_of_clicks)
            
            elif itype == utl.ElementType.DELAY:
                    # read parameters
                idata = line.get_data()
                time_millis = idata['time_millis']
                
                # execution
                time.sleep(time_millis/1000)
            

            
        





















