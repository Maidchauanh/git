from random import randint 
import random
import pygame 
class Drop:
	def __init__(self,surface,color,x,y,width,height,gravity):
		self.surface=surface
		self.color=color
		self.x=x
		self.y=y
		self.width=width
		self.height=height
		self.time=0
		self.gravity=gravity
		self.a=10
	def fall(self):
		self.y =int(self.y + self.gravity*0.5*self.time**2)
		if self.y>600:
			self.y=-1*randint(300,1500)
			self.time=0.03
		self.time+=0.01
		pygame.draw.rect(self.surface,self.color,(self.x,self.y,self.width,self.height))
white=(255,255,255)
purple=(128,0,128)
pygame.init()
screen=pygame.display.set_mode((900,600))
pygame.display.set_caption("Purple rain")
run=True
drops=[]
widths=[i for i in range(1,5)]
heights=[i for i in range(15,40,4)]
gravities=[i for i in range(2,20,4)]
size=list(zip(widths,heights,gravities))
clock=pygame.time.Clock()
#making the rain drops
for i in range(800):
	x=randint(10,890)
	y=-1*randint(300,1500)
	width,height,g=random.choice(size)
	raindrop=Drop(screen,purple,x,y,width,height,g)	
	drops.append(raindrop)
#mainloop
while run :
	clock.tick(30)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
   	screen.fill(white)
	for d in drops:
		d.fall()
    	pygame.display.update()
pygame.quit()