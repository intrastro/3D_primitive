from tkinter import *
import time
import math

size_x_c = 500
size_y_c = 200

class vol:
  dist = 50
  x = 0
  y = 0
  z = 0

  t = 0

  rx = 0
  ry = 0
  rz = 0
  length = 0
  a = 0
  b = 0
  c = 0

  p_l = [0, 0]
  p_l_c = [0, 0]
  
  def __init__(self, list_xyz): 
    self.rx = list_xyz [0] 
    self.ry = list_xyz [1] 
    self.rz = list_xyz [2]
    self.x = list_xyz [0]
    self.y = list_xyz [1]
    self.z = list_xyz [2] 
    

  def spin_z (self, alpha):
    #self.dist = ((self.x)**(2) + (self.y)**(2) + (self.z)**(2))**(1/2)
    
    self.a = alpha
    self.t = self.x * math.cos (self.a) - self.y * math.sin (self.a)
    self.y = self.x * math.sin (self.a) + self.y * math.cos (self.a)
    self.x = self.t
    
    self.length = ((self.x)**(2) + (self.y)**(2) + (self.z)**(2))**(1/2)
    
    #self.x = self.rx * (self.dist / self.length)
    #self.y = self.ry * (self.dist / self.length)
    

    self.p_l = [self.x, self.y]
    self.p_l_c = [self.x + size_x_c, self.y + size_y_c]

  def spin_y (self, alpha):
    #self.dist = ((self.x)**(2) + (self.y)**(2) + (self.z)**(2))**(1/2)
    
    self.b = alpha
    self.t = self.z * math.cos (self.b) - self.x * math.sin (self.b)
    self.x = self.z * math.sin (self.b) + self.x * math.cos (self.b)
    self.z = self.t

    self.length = ((self.x)**(2) + (self.y)**(2) + (self.z)**(2))**(1/2)
    
    #self.z = self.z * (self.dist / self.length)
    #self.x = self.z * (self.dist / self.length)

    self.p_l = [self.x, self.y]
    self.p_l_c = [self.x + size_x_c, self.y + size_y_c]

  def spin_x (self, alpha):
    #self.dist = ((self.x)**(2) + (self.y)**(2) + (self.z)**(2))**(1/2)

    self.c = alpha
    self.t = self.y * math.cos (self.c) - self.z * math.sin (self.c)
    self.z = self.y * math.sin (self.c) + self.z * math.cos (self.c)
    self.y = self.t

    self.length = ((self.x)**(2) + (self.y)**(2) + (self.z)**(2))**(1/2)

    #self.z = self.z * (self.dist / self.length)
    #self.y = self.y * (self.dist / self.length)

    self.p_l = [self.x, self.y]
    self.p_l_c = [self.x + size_x_c, self.y + size_y_c]
    

    

class Example(Frame):
    points = [0 for i in range(8)]
    points[0] = vol ([ 50,  50,  50])
    points[1] = vol ([ 50,  50, -50])
    points[2] = vol ([-50,  50, -50])
    points[3] = vol ([-50, -50, -50])
    points[4] = vol ([ 50, -50, -50])
    points[5] = vol ([ 50, -50,  50])
    points[6] = vol ([-50, -50,  50])
    points[7] = vol ([-50,  50,  50])
    
    
    def __init__(self, parent):
        self.canvas = Canvas (parent)
        Frame.__init__(self, parent)   
        self.parent = parent
        self.parent.title("Simple")
        self.pack(fill=BOTH, expand=1)

        self.bind_all("<Key>", self.linespin)        

    def linespin(self, e):
        local_points = list ()       
        for y in range (len (self.points)):
            local_points.append (self.points[y].p_l_c)
            
        local = [0 for i in range(6)]
        local [0] = [local_points [0], local_points [1], local_points [2], local_points [7]]
        local [1] = [local_points [2], local_points [3], local_points [6], local_points [7]]
        local [2] = [local_points [3], local_points [4], local_points [5], local_points [6]]
        local [3] = [local_points [4], local_points [1], local_points [0], local_points [5]]
        local [4] = [local_points [7], local_points [6], local_points [5], local_points [0]]
        local [5] = [local_points [1], local_points [2], local_points [3], local_points [4]]

        a = list ()
        for z in range(0, len (local)):
          #print ("z=" + str (z))
          reallen = len (local [z])
          for y in range(0, len (local [z])):
            #print ("y=" + str (y))
            #print (str (local[z][y]))
            local[z].extend (local[z][y])
          for y in range(0, reallen):
            del local [z][0]
      
        key = e.keysym

        if key == "Right":             
          for y in range (0, len (self.points)):
            self.points[y].spin_y (-0.2)
        elif key == "Left":             
          for y in range (0, len (self.points)):
            self.points[y].spin_y (0.2)
        elif key == "Up":             
          for y in range (0, len (self.points)):
            self.points[y].spin_x (-0.2)              
        elif key == "Down":             
          for y in range (0, len (self.points)):
            self.points[y].spin_x (0.2)
        else:
          for y in range (0, len (self.points)):
            self.points[y].spin_z (-0.2)
        
        i = 0
        
        self.canvas.delete ("all")
        while (i < 1):
            self.canvas.create_line (size_x_c, size_y_c, size_x_c, size_y_c + 1)
            #print (points)
            for y in range (0, len (local)):
              for z in range (0, len (local [y]), 2):
                self.canvas.create_line(local [y][z % len (local [y])], local [y][(z + 1) % len (local [y])] ,
                                        local [y][(z + 2) % len (local [y]) ], local [y][(z + 3)% len (local [y])])

            self.canvas.pack(fill=BOTH, expand=1)

            i = i + 1            

        
        print (str ((((self.points[2].x) - (self.points[3].x))**2 +
               ((self.points[2].y) - (self.points[3].y))**2 +
               ((self.points[2].z) - (self.points[3].z))**2)**(1/2)))
        
        print (str ((((self.points[3].x) - (self.points[4].x))**2 +
               ((self.points[3].y) - (self.points[4].y))**2 +
               ((self.points[3].z) - (self.points[4].z))**2)**(1/2)))
        




root = Tk()
root.geometry("1000x800")
app = Example(root)
root.mainloop()  
