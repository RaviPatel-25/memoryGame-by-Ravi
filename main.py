from tkinter import*
from PIL import ImageTk, Image
import random

class Game:
	def __init__(self,root):
		self.root = root
		self.root.geometry("1080x2129+0+0")
		self.root.overrideredirect(True)
		self.root.config(bg="orange")
		
		self.btnpressed = []
		self.count = 0
		
		path = "/storage/emulated/0/image finder/"
		self.orange = path + "Orange.png"
		self.strawberry = path + "Strawberry.png"
		self.banana = path + "Banana.png"
		self.pears = path + "Pears.png"
		self.mango = path + "Mango.png"
		self.grapes = path + "Grapes.png"
		self.apple = path + "Apple.png"
		self.watermelon = path + "Watermelon.png"
		self.blank = path + "Blank.jpg"
		
		self.orange = Image.open(self.orange)
		self.strawberry = Image.open(self.strawberry)
		self.banana = Image.open(self.banana)
		self.pears = Image.open(self.pears)
		self.mango = Image.open(self.mango)
		self.grapes = Image.open(self.grapes)
		self.apple = Image.open(self.apple)
		self.watermelon = Image.open(self.watermelon)
		self.blank = Image.open(self.blank)
		
		self.orange = self.orange.resize((150, 150))
		self.strawberry = self.strawberry.resize((150, 150))
		self.banana = self.banana.resize((150, 150))
		self.pears = self.pears.resize((150, 150))
		self.mango = self.mango.resize((150, 150))
		self.grapes = self.grapes.resize((150, 150))
		self.apple = self.apple.resize((150, 150))
		self.watermelon = self.watermelon.resize((150, 150))
		self.blank = self.blank.resize((150, 150))
		
		self.orange = ImageTk.PhotoImage(self.orange)
		self.strawberry = ImageTk.PhotoImage(self.strawberry)
		self.banana = ImageTk.PhotoImage(self.banana)
		self.pears = ImageTk.PhotoImage(self.pears)
		self.mango = ImageTk.PhotoImage(self.mango)
		self.grapes = ImageTk.PhotoImage(self.grapes)
		self.apple = ImageTk.PhotoImage(self.apple)
		self.watermelon = ImageTk.PhotoImage(self.watermelon)
		self.blank = ImageTk.PhotoImage(self.blank)
		
		self.pics = [self.orange, self.strawberry, self.banana, self.pears, self.mango, self.grapes, self.apple, self.watermelon]
		
		self.b1=Button(self.root,bd=10,image=self.blank,bg="white",command=self.check1)
		self.b2=Button(self.root,bd=10,image=self.blank,bg="white",command=self.check2)
		self.b3=Button(self.root,bd=10,image=self.blank,bg="white",command=self.check3)
		self.b4=Button(self.root,bd=10,image=self.blank,bg="white",command=self.check4)
		
		self.b5=Button(self.root,bd=10,image=self.blank,bg="white",command=self.check5)
		self.b6=Button(self.root,bd=10,image=self.blank,bg="white",command=self.check6)
		self.b7=Button(self.root,bd=10,image=self.blank,bg="white",command=self.check7)
		self.b8=Button(self.root,bd=10,image=self.blank,bg="white",command=self.check8)
		
		self.b9=Button(self.root,bd=10,image=self.blank,bg="white",command=self.check9)
		self.b10=Button(self.root,bd=10,image=self.blank,bg="white",command=self.check10)
		self.b11=Button(self.root,bd=10,image=self.blank,bg="white",command=self.check11)
		self.b12=Button(self.root,bd=10,image=self.blank,bg="white",command=self.check12)
		
		self.b13=Button(self.root,bd=10,image=self.blank,bg="white",command=self.check13)
		self.b14=Button(self.root,bd=10,image=self.blank,bg="white",command=self.check14)
		self.b15=Button(self.root,bd=10,image=self.blank,bg="white",command=self.check15)
		self.b16=Button(self.root,bd=10,image=self.blank,bg="white",command=self.check16)
		
	def main(self):
		self.b1.place(x=140,y=500)
		self.b2.place(x=350,y=500)
		self.b3.place(x=560,y=500)
		self.b4.place(x=770,y=500)
		
		self.b5.place(x=140,y=710)
		self.b6.place(x=350,y=710)
		self.b7.place(x=560,y=710)
		self.b8.place(x=770,y=710)
		
		self.b9.place(x=140,y=920)
		self.b10.place(x=350,y=920)
		self.b11.place(x=560,y=920)
		self.b12.place(x=770,y=920)	
		
		self.b13.place(x=140,y=1130)	
		self.b14.place(x=350,y=1130)
		self.b15.place(x=560,y=1130)	
		self.b16.place(x=770,y=1130)
		
	def result(self,btn):
		if self.count ==0:
			self.btnpressed.append(btn)
			self.count+=1
		elif self.count ==1:
			self.btnpressed.append(btn)
			self.count+=1
		
		if self.count==2:
			if self.btnpressed[0]==1 and self.btnpressed[1]==1:
				self.b1['state'] = DISABLED
				self.b11['state'] = DISABLED
				self.count=0
				self.btnpressed=[]
			elif self.btnpressed[0]==2 and self.btnpressed[1]==2:
				self.b2['state'] = DISABLED
				self.b5['state'] = DISABLED
				self.count=0
				self.btnpressed=[]
			elif self.btnpressed[0]==3 and self.btnpressed[1]==3:
				self.b3['state'] = DISABLED
				self.b7['state'] = DISABLED
				self.count=0
				self.btnpressed=[]
			elif self.btnpressed[0]==4 and self.btnpressed[1]==4:
				self.b4['state'] = DISABLED
				self.b6['state'] = DISABLED
				self.count=0
				self.btnpressed=[]
			elif self.btnpressed[0]==5 and self.btnpressed[1]==5:
				self.b8['state'] = DISABLED
				self.b9['state'] = DISABLED
				self.count=0
				self.btnpressed=[]
			elif self.btnpressed[0]==6 and self.btnpressed[1]==6:
				self.b10['state'] = DISABLED
				self.b16['state'] = DISABLED
				self.count=0
				self.btnpressed=[]
			elif self.btnpressed[0]==7 and self.btnpressed[1]==7:
				self.b12['state'] = DISABLED
				self.b14['state'] = DISABLED
				self.count=0
				self.btnpressed=[]
			elif self.btnpressed[0]==8 and self.btnpressed[1]==8:
				self.b13['state'] = DISABLED
				self.b15['state'] = DISABLED
				self.count=0
				self.btnpressed=[]
			else:
				if (self.btnpressed[0]==1 and self.btnpressed[1]==2) or (self.btnpressed[0]==2 and self.btnpressed[1]==1):
					self.b1.config(image=self.blank)
					self.b2.config(image=self.blank)
					self.b5.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==1 and self.btnpressed[1]==3) or (self.btnpressed[0]==3 and self.btnpressed[1]==1):
					self.b1.config(image=self.blank)
					self.b3.config(image=self.blank)
					self.b7.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==1 and self.btnpressed[1]==4) or (self.btnpressed[0]==4 and self.btnpressed[1]==1):
					self.b1.config(image=self.blank)
					self.b4.config(image=self.blank)
					self.b6.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==1 and self.btnpressed[1]==5) or (self.btnpressed[0]==5 and self.btnpressed[1]==1):
					self.b1.config(image=self.blank)
					self.b8.config(image=self.blank)
					self.b9.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==1 and self.btnpressed[1]==6) or (self.btnpressed[0]==6 and self.btnpressed[1]==1):
					self.b1.config(image=self.blank)
					self.b10.config(image=self.blank)
					self.b16.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==1 and self.btnpressed[1]==7) or (self.btnpressed[0]==7 and self.btnpressed[1]==1):
					self.b1.config(image=self.blank)
					self.b12.config(image=self.blank)
					self.b14.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==1 and self.btnpressed[1]==8) or (self.btnpressed[0]==8 and self.btnpressed[1]==1):
					self.b1.config(image=self.blank)
					self.b13.config(image=self.blank)
					self.b15.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				
				elif (self.btnpressed[0]==2 and self.btnpressed[1]==1) or (self.btnpressed[0]==1 and self.btnpressed[1]==2):
					self.b1.config(image=self.blank)
					self.b2.config(image=self.blank)
					self.b11.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==2 and self.btnpressed[1]==3) or (self.btnpressed[0]==3 and self.btnpressed[1]==2):
					self.b2.config(image=self.blank)
					self.b3.config(image=self.blank)
					self.b7.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==2 and self.btnpressed[1]==4) or (self.btnpressed[0]==4 and self.btnpressed[1]==2):
					self.b2.config(image=self.blank)
					self.b4.config(image=self.blank)
					self.b6.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==2 and self.btnpressed[1]==5) or (self.btnpressed[0]==5 and self.btnpressed[1]==2):
					self.b2.config(image=self.blank)
					self.b8.config(image=self.blank)
					self.b9.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==2 and self.btnpressed[1]==6) or (self.btnpressed[0]==6 and self.btnpressed[1]==2):
					self.b2.config(image=self.blank)
					self.b10.config(image=self.blank)
					self.b16.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==2 and self.btnpressed[1]==7) or (self.btnpressed[0]==7 and self.btnpressed[1]==2):
					self.b2.config(image=self.blank)
					self.b12.config(image=self.blank)
					self.b14.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==2 and self.btnpressed[1]==8) or (self.btnpressed[0]==8 and self.btnpressed[1]==2):
					self.b2.config(image=self.blank)
					self.b13.config(image=self.blank)
					self.b15.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
					
				elif (self.btnpressed[0]==3 and self.btnpressed[1]==1) or (self.btnpressed[0]==1 and self.btnpressed[1]==3):
					self.b1.config(image=self.blank)
					self.b3.config(image=self.blank)
					self.b11.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==3 and self.btnpressed[1]==2) or (self.btnpressed[0]==2 and self.btnpressed[1]==3):
					self.b2.config(image=self.blank)
					self.b3.config(image=self.blank)
					self.b5.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==3 and self.btnpressed[1]==4) or (self.btnpressed[0]==4 and self.btnpressed[1]==3):
					self.b3.config(image=self.blank)
					self.b4.config(image=self.blank)
					self.b6.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==3 and self.btnpressed[1]==5) or (self.btnpressed[0]==5 and self.btnpressed[1]==3):
					self.b3.config(image=self.blank)
					self.b8.config(image=self.blank)
					self.b9.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==3 and self.btnpressed[1]==6) or (self.btnpressed[0]==6 and self.btnpressed[1]==3):
					self.b3.config(image=self.blank)
					self.b10.config(image=self.blank)
					self.b16.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==3 and self.btnpressed[1]==7) or (self.btnpressed[0]==7 and self.btnpressed[1]==3):
					self.b3.config(image=self.blank)
					self.b12.config(image=self.blank)
					self.b14.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==3 and self.btnpressed[1]==8) or (self.btnpressed[0]==8 and self.btnpressed[1]==3):
					self.b3.config(image=self.blank)
					self.b13.config(image=self.blank)
					self.b15.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
					
				elif (self.btnpressed[0]==4 and self.btnpressed[1]==1) or (self.btnpressed[0]==1 and self.btnpressed[1]==4):
					self.b4.config(image=self.blank)
					self.b1.config(image=self.blank)
					self.b11.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==4 and self.btnpressed[1]==2) or (self.btnpressed[0]==2 and self.btnpressed[1]==4):
					self.b4.config(image=self.blank)
					self.b2.config(image=self.blank)
					self.b5.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==4 and self.btnpressed[1]==3) or (self.btnpressed[0]==3 and self.btnpressed[1]==4):
					self.b4.config(image=self.blank)
					self.b3.config(image=self.blank)
					self.b7.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==4 and self.btnpressed[1]==5) or (self.btnpressed[0]==5 and self.btnpressed[1]==4):
					self.b4.config(image=self.blank)
					self.b8.config(image=self.blank)
					self.b9.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==4 and self.btnpressed[1]==6) or (self.btnpressed[0]==6 and self.btnpressed[1]==4):
					self.b4.config(image=self.blank)
					self.b10.config(image=self.blank)
					self.b16.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==4 and self.btnpressed[1]==7) or (self.btnpressed[0]==7 and self.btnpressed[1]==4):
					self.b4.config(image=self.blank)
					self.b12.config(image=self.blank)
					self.b14.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==4 and self.btnpressed[1]==8) or (self.btnpressed[0]==8 and self.btnpressed[1]==4):
					self.b4.config(image=self.blank)
					self.b13.config(image=self.blank)
					self.b15.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				
				elif (self.btnpressed[0]==5 and self.btnpressed[1]==1) or (self.btnpressed[0]==1 and self.btnpressed[1]==5):
					self.b1.config(image=self.blank)
					self.b11.config(image=self.blank)
					self.b8.config(image=self.blank)
					self.b9.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==5 and self.btnpressed[1]==2) or (self.btnpressed[0]==2 and self.btnpressed[1]==5):
					self.b2.config(image=self.blank)
					self.b5.config(image=self.blank)
					self.b8.config(image=self.blank)
					self.b9.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==5 and self.btnpressed[1]==3) or (self.btnpressed[0]==3 and self.btnpressed[1]==5):
					self.b3.config(image=self.blank)
					self.b7.config(image=self.blank)
					self.b8.config(image=self.blank)
					self.b9.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==5 and self.btnpressed[1]==4) or (self.btnpressed[0]==4 and self.btnpressed[1]==5):
					self.b4.config(image=self.blank)
					self.b6.config(image=self.blank)
					self.b8.config(image=self.blank)
					self.b9.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==5 and self.btnpressed[1]==6) or (self.btnpressed[0]==6 and self.btnpressed[1]==5):
					self.b8.config(image=self.blank)
					self.b9.config(image=self.blank)
					self.b10.config(image=self.blank)
					self.b16.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==5 and self.btnpressed[1]==7) or (self.btnpressed[0]==7 and self.btnpressed[1]==5):
					self.b8.config(image=self.blank)
					self.b9.config(image=self.blank)
					self.b12.config(image=self.blank)
					self.b14.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==5 and self.btnpressed[1]==8) or (self.btnpressed[0]==8 and self.btnpressed[1]==5):
					self.b8.config(image=self.blank)
					self.b9.config(image=self.blank)
					self.b13.config(image=self.blank)
					self.b15.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
					
				elif (self.btnpressed[0]==6 and self.btnpressed[1]==1) or (self.btnpressed[0]==1 and self.btnpressed[1]==6):
					self.b1.config(image=self.blank)
					self.b11.config(image=self.blank)
					self.b10.config(image=self.blank)
					self.b16.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==6 and self.btnpressed[1]==2) or (self.btnpressed[0]==2 and self.btnpressed[1]==6):
					self.b2.config(image=self.blank)
					self.b5.config(image=self.blank)
					self.b10.config(image=self.blank)
					self.b16.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==6 and self.btnpressed[1]==3) or (self.btnpressed[0]==3 and self.btnpressed[1]==6):
					self.b3.config(image=self.blank)
					self.b7.config(image=self.blank)
					self.b10.config(image=self.blank)
					self.b16.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==6 and self.btnpressed[1]==4) or (self.btnpressed[0]==4 and self.btnpressed[1]==6):
					self.b4.config(image=self.blank)
					self.b6.config(image=self.blank)
					self.b10.config(image=self.blank)
					self.b16.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==6 and self.btnpressed[1]==5) or (self.btnpressed[0]==5 and self.btnpressed[1]==6):
					self.b8.config(image=self.blank)
					self.b10.config(image=self.blank)
					self.b16.config(image=self.blank)
					self.b9.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==6 and self.btnpressed[1]==7) or (self.btnpressed[0]==7 and self.btnpressed[1]==6):
					self.b10.config(image=self.blank)
					self.b12.config(image=self.blank)
					self.b14.config(image=self.blank)
					self.b16.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==1 and self.btnpressed[1]==8) or (self.btnpressed[0]==8 and self.btnpressed[1]==1):
					self.b10.config(image=self.blank)
					self.b16.config(image=self.blank)
					self.b13.config(image=self.blank)
					self.b15.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
					
				elif (self.btnpressed[0]==7 and self.btnpressed[1]==1) or (self.btnpressed[0]==1 and self.btnpressed[1]==7):
					self.b1.config(image=self.blank)
					self.b11.config(image=self.blank)
					self.b12.config(image=self.blank)
					self.b14.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==7 and self.btnpressed[1]==2) or (self.btnpressed[0]==2 and self.btnpressed[1]==7):
					self.b2.config(image=self.blank)
					self.b5.config(image=self.blank)
					self.b12.config(image=self.blank)
					self.b14.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==7 and self.btnpressed[1]==3) or (self.btnpressed[0]==3 and self.btnpressed[1]==7):
					self.b3.config(image=self.blank)
					self.b7.config(image=self.blank)
					self.b12.config(image=self.blank)
					self.b14.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==7 and self.btnpressed[1]==4) or (self.btnpressed[0]==4 and self.btnpressed[1]==7):
					self.b4.config(image=self.blank)
					self.b6.config(image=self.blank)
					self.b12.config(image=self.blank)
					self.b14.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==7 and self.btnpressed[1]==5) or (self.btnpressed[0]==5 and self.btnpressed[1]==7):
					self.b12.config(image=self.blank)
					self.b14.config(image=self.blank)
					self.b8.config(image=self.blank)
					self.b9.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==7 and self.btnpressed[1]==6) or (self.btnpressed[0]==6 and self.btnpressed[1]==7):
					self.b10.config(image=self.blank)
					self.b16.config(image=self.blank)
					self.b12.config(image=self.blank)
					self.b14.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==7 and self.btnpressed[1]==8) or (self.btnpressed[0]==8 and self.btnpressed[1]==7):
					self.b12.config(image=self.blank)
					self.b14.config(image=self.blank)
					self.b13.config(image=self.blank)
					self.b15.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
					
				elif (self.btnpressed[0]==8 and self.btnpressed[1]==1) or (self.btnpressed[0]==1 and self.btnpressed[1]==8):
					self.b1.config(image=self.blank)
					self.b11.config(image=self.blank)
					self.b13.config(image=self.blank)
					self.b15.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==8 and self.btnpressed[1]==2) or (self.btnpressed[0]==2 and self.btnpressed[1]==8):
					self.b2.config(image=self.blank)
					self.b5.config(image=self.blank)
					self.b13.config(image=self.blank)
					self.b15.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==8 and self.btnpressed[1]==3) or (self.btnpressed[0]==3 and self.btnpressed[1]==8):
					self.b3.config(image=self.blank)
					self.b7.config(image=self.blank)
					self.b13.config(image=self.blank)
					self.b15.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==8 and self.btnpressed[1]==4) or (self.btnpressed[0]==4 and self.btnpressed[1]==8):
					self.b4.config(image=self.blank)
					self.b6.config(image=self.blank)
					self.b13.config(image=self.blank)
					self.b15.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==8 and self.btnpressed[1]==5) or (self.btnpressed[0]==5 and self.btnpressed[1]==8):
					self.b8.config(image=self.blank)
					self.b9.config(image=self.blank)
					self.b13.config(image=self.blank)
					self.b15.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==8 and self.btnpressed[1]==6) or (self.btnpressed[0]==6 and self.btnpressed[1]==8):
					self.b10.config(image=self.blank)
					self.b16.config(image=self.blank)
					self.b13.config(image=self.blank)
					self.b15.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				elif (self.btnpressed[0]==8 and self.btnpressed[1]==7) or (self.btnpressed[0]==7 and self.btnpressed[1]==8):
					self.b12.config(image=self.blank)
					self.b14.config(image=self.blank)
					self.b13.config(image=self.blank)
					self.b15.config(image=self.blank)
					self.count=0
					self.btnpressed=[]
				
		pass
		
	def check1(self):
		self.b1.config(image=self.apple)
		self.result(1)
	def check2(self):
		self.b2.config(image=self.orange)
		self.result(2)
	
	def check3(self):
		self.b3.config(image=self.strawberry)
		self.result(3)
		
	def check4(self):
		self.b4.config(image=self.banana)
		self.result(4)
	
	def check5(self):
		self.b5.config(image=self.orange)
		self.result(2)
		
	def check6(self):
		self.b6.config(image=self.banana)
		self.result(4)
	
	def check7(self):
		self.b7.config(image=self.strawberry)
		self.result(3)
		
	def check8(self):
		self.b8.config(image=self.mango)
		self.result(5)
	
	def check9(self):
		self.b9.config(image=self.mango)
		self.result(5)
		
	def check10(self):
		self.b10.config(image=self.grapes)
		self.result(6)
	
	def check11(self):
		self.b11.config(image=self.apple)
		self.result(1)
		
	def check12(self):
		self.b12.config(image=self.watermelon)
		self.result(7)
	
	def check13(self):
		self.b13.config(image=self.pears)
		self.result(8)
		
	def check14(self):
		self.b14.config(image=self.watermelon)
		self.result(7)
	
	def check15(self):
		self.b15.config(image=self.pears)
		self.result(8)
		
	def check16(self):
		self.b16.config(image=self.grapes)
		self.result(6)
		
	
	
root = Tk()
obj = Game(root)
obj.main()
root.mainloop()