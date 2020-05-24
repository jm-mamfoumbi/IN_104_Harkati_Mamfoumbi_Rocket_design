import tkinter as tk
import main

class Drawer:
	def __init__(self, window):
		self.rockets = []
		self.boxes = []
		self.r_index = -1
		self.cursor_pos = 100
		self.shift = 0
		self.frame = tk.Frame(window, bg='#AA4AEE')
		self.frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
		self.canvas = tk.Canvas(self.frame, bg='gray95')
		self.canvas.pack(side = tk.RIGHT, fill = tk.BOTH, expand = True)
		
	''' load rocket into the display sreen in order to be displayed '''
	def load_rockets(self, rocket_list):
		if (rocket_list == []):
			self.rockets.clear()
			self.r_index = -1
		elif (len(rocket_list) == 1):
			self.rockets.insert(0,rocket_list[0])
			self.r_index = 0
		else:
			self.rockets.clear()
			self.rockets = rocket_list
			self.r_index = 0
	
	''' Add a rocket to the display screen by giving its properties '''
	def add_rocket(self, name, info, spec):
		if(spec[9] == 0):
			spec = spec[:9]
			spec.insert(0,1)
		else:
			spec.insert(0,2)

		new_rocket = main.Rocket(name, info, spec)
		self.rockets.insert(0, new_rocket)
		self.cursor_pos = 100
		self.r_index = 0
		self.draw()
	
	''' Check if the mouse is in on a displayed on the screen rocket '''
	def mouse(self, x, y) :
		init = 100;
		x = x + self.shift;
		for i in range(0, len(self.boxes)):
			if (x > init and x < init + self.boxes[i][0] and y > 600 - self.boxes[i][1] and y < 600):
				self.select(i)
				break
			init += self.boxes[i][0]
	
	''' Establish where in the display screen space is situated the selected rocket '''
	def set_cursor(self):
		self.cursor_pos = 100
		for i in range(0, self.r_index):
			self.cursor_pos += self.boxes[i][0];
	
	
	''' The rocket of index *index* become the selected rocket '''
	def select(self, index):
		if (index >= 0 and index < len(self.rockets)):
			self.r_index = index
			self.set_cursor()
			self.draw()
	
	''' The rocket next - in the direction *direction* - to the selected rocket become the new selected rocket '''
	def select_next(self, direction):
		if (self.r_index > -1):
			self.r_index = (direction + self.r_index) % len(self.rockets)
			self.set_cursor()
			self.draw()
		
	''' Delete from the display screen the current selected rocket '''
	def delete_selected(self):
		if(self.r_index > -1):
			self.rockets.pop(self.r_index)
			if (self.r_index == len(self.rockets)):
				self.r_index -= 1
			self.set_cursor()
			self.draw()
			
	''' Delete all rocket displayed in the display screen '''
	def delete_all(self):
		if(self.r_index > -1):
			self.rockets.clear()
			self.r_index = -1
			self.set_cursor()
			self.draw()
	
	''' Draw a rocket of properties data in position (x,y) '''
	def draw_rocket(self, x, y, data, selected, factor):
		s1_x1 = x ; s1_y1 = y - int(factor *  data[3])
		s1_x2 = x + int(factor * data[4]) ; s1_y2 = y
		
		ds1s2 = (float(factor) * data[4] - float(factor) * data[6])/2
		
		s2_x1 = x + ds1s2 ; s2_y1 = s1_y1 - int(factor * data[5])
		s2_x2 = x - ds1s2 + int(factor * data[6]) ; s2_y2 = s1_y1
		
		mid = (s1_x2 + s1_x1)/2
		h = y - int(factor * data[2])
		
		self.canvas.create_rectangle(s1_x1 - self.shift,s1_y1,s1_x2- self.shift,s1_y2, fill='ivory3', width=1, outline='gray8')
		if (int(data[5] != 0)) :
			self.canvas.create_rectangle(s2_x1- self.shift,s2_y1,s2_x2- self.shift,s2_y2, fill='SkyBlue3', width=1, outline='gray8')
			self.canvas.create_line(s2_x1- self.shift,s2_y1,mid - self.shift, h, width=1, fill='gray8')
			self.canvas.create_line(s2_x2- self.shift,s2_y1,mid - self.shift, h, width=1, fill='gray8')
		else :
			self.canvas.create_line(s1_x1- self.shift, s1_y1, mid - self.shift, h, width=1, fill='gray8')
			self.canvas.create_line(s1_x2- self.shift, s1_y1, mid - self.shift, h, width=1, fill='gray8')
			
		if (selected):
			board = self.boxes[self.r_index]
			self.canvas.create_rectangle(x - 25 - self.shift, y + 25 - board[1], x - 25 + board[0] - self.shift,y + 25, outline='red');
			self.canvas.create_text(x + 5 - self.shift, y + 35, text=self.rockets[self.r_index].get_name())
	
	''' Draw all the rockets loaded in order to be drawn '''
	def draw(self):
		self.boxes.clear()
		self.canvas.delete("all")
		
		self.shift = 0 if self.cursor_pos < 500 else self.cursor_pos - 500
		
		space = 100
		factor = 5
		for i in range(0, len(self.rockets)):
			ri = self.rockets[i];
			name = ri.get_name();
			spec = ri.get_spec();
			data = [name, spec[0], spec[1], spec[4], spec[5], spec[10], spec[11]] if not ri.one_stage() else [name, spec[0], spec[1], spec[4], spec[5], 0, 0]
			selected = True if i == self.r_index else False
			
			self.boxes.append((50 + factor * max(data[4], data[6]), 50 + factor * data[2]));
			self.draw_rocket(space, 600, data, selected, factor)
				
			space = space + self.boxes[len(self.boxes) - 1][0]
		
		self.canvas.create_rectangle(75 - self.shift , 650, space - self.shift, 660, fill='LightBlue4')
		
	''' Accessor to the tk.frame of the display screen '''
	def get_frame(self):
		return self.frame
	
	''' Accessor to the loaded rockets '''
	def get_list(self):
		return self.rockets
	
	''' Accessor to the currently selected rocket'''
	def get_selected(self):
		if (self.r_index > -1):
			return self.rockets[self.r_index]
		else: return None
