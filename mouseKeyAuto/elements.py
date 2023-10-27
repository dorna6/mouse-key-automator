import mouseKeyAuto.utils as utl


# SECTION: common element class
class Element():
    def __init__(self,
                 type:utl.ElementType,
                 data:dict):
        self.type = type
        self.ex_data_dict = data
    
    def get_type(self):
        return self.type
    
    def get_data(self):
        return self.ex_data_dict

    

# SECTION: element - mouse move abs class
class Element_MouseMoveAbs(Element):
    def __init__(self, abs_position):
        super().__init__(type = utl.ElementType.MOUSE_MOVE_ABS,
                         data = {
                             'abs_position': abs_position
                             })



# SECTION: element - mouse move rel class
class Element_MouseMoveRel(Element):
    def __init__(self, rel_position):
        super().__init__(type = utl.ElementType.MOUSE_MOVE_REL,
                         data = {
                             'rel_position': rel_position
                             }) 
        
        
        
# SECTION: element - mouse click right class
class Element_MouseClickRight(Element):
    def __init__(self, num_of_clicks):
        super().__init__(type = utl.ElementType.MOUSE_CLICK_RIGHT,
                         data = {
                             'num_of_clicks': num_of_clicks
                             })



# SECTION: element - mouse click left class
class Element_MouseClickLeft(Element):
    def __init__(self, num_of_clicks):
        super().__init__(type = utl.ElementType.MOUSE_CLICK_LEFT,
                         data = {
                             'num_of_clicks': num_of_clicks
                             })        
        
        

# SECTION: element - delay class
class Element_Delay(Element):
    def __init__(self, time_millis):
        super().__init__(type = utl.ElementType.DELAY,
                         data = {
                             'time_millis': time_millis
                             })         
        
        
        
        
