# main.py
# pip install pygame
# pip3 install pygame
# python3 -m pip install pygame
# C:\Python38\python.exe -m pip install pygame
import pygame
import math
import random
# เซ็ตอัพเริ่มต้นให้ pygame ทำงาน
pygame.init()

# ปรับขนาดหน้าจอหลัก
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Covid-19') #set ชื่อเกม
icon = pygame.image.load('icon.png') # โหลดภาพเข้ามาใน pygame
pygame.display.set_icon(icon) #สั่งเซ็ตเป็น icon
background = pygame.image.load('background.png')

###############Player###############
# 1 - player - uncle.png

psize = 128 #ความกว้างของภาพ Player

pimg = pygame.image.load('uncle.png')
px = 100	#400-(psize/2)	#จุดเริ่มต้นแกน x (แนวนอน)
py = HEIGHT - psize 	#จุดเริ่มต้นแกน y (แนวตั้ง)
pxchange = 0 
def Player(x,y):
	screen.blit(pimg,(x,y)) #blit  คือ วางภาพในหน้าจอ


###############Enemy###############
# 2 - enemy - virus.png
esize = 64
eimg = pygame.image.load('virus.png')
ex = 50
ey = esize
eychange = 3
def Enemy(x,y):
	screen.blit(eimg,(x,y))

###############Mask###############
# 3 - mask - mask.png
msize = 32
mimg = pygame.image.load('mask.png')
mx = 100
my = HEIGHT - psize
mychange = 5
mstate = 'ready'

def fire_mask(x,y):
	global mstate
	mstate = 'fire'
	screen.blit(mimg,(x,y))

############## collision ##############
def isCollision(ecx,ecy,mcx,mcy):
	# isCollision ชนกันหรือไม่? หากชนกัน ให้คืนค่า True
	distance = math.sqrt(math.pow(ecx - mcx,2)+math.pow(ecy - mcy,2))
	print(distance)
	if distance < 48:
		return True
	else:
		return False

############### Game Loop ###############
running = True #บองให้โปรแกรมทำงาน

clock = pygame.time.Clock() # game clock 
FPS = 60 #frame rate
while running:
	screen.blit(background,(0,0))
	for event in pygame.event.get():
		# รันลูปแล้วเช็คว่ามีการกดปิดเกมหรือไม่ [x]
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				pxchange = -10
			if event.key == pygame.K_RIGHT:
				pxchange = 10

			if event.key == pygame.K_SPACE:
				if mstate == 'ready':
					mx = px + 20  # ขยับหน้ากาก ชิดมือ ด้านขวา
					fire_mask(mx,my)

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				pxchange = 0

	############# run player ############
	# px,py จุดเริ่มต้น 		
	Player(px,py)
	'''
	### ทำให้ player ขยับซ้ายขวา เมื่อชนของจอ
	if px <= 0:
		# หากชนขอบจอซ้าย ให้ปรับค่า pxchange เป็น +1
		pxchange = 1
		px += pxchange # px = px+1
	elif px >= WIDTH - psize:
		# WIDTH (ความกว้างของหน้าจอ - ความกว้างplayer)
		# หากชนขอบจอขวา ให้ปรับค่า pxchange เป็น +1
		pxchange = -1
		px += pxchange
	else:
		# หากอยู่ระหว่างหน้าจอจะทำการบวก/ลบ ตาม pxchange
		px += pxchange
	'''
	### ทำให้ player ขยับซ้ายขวา เมื่อชนของจอ
	if px <= 0:
		# หากชนขอบจอซ้าย ให้ปรับค่า pxchange เป็น +1
		px = 0
		px += pxchange # px = px+1
	elif px >= WIDTH - psize:
		# WIDTH (ความกว้างของหน้าจอ - ความกว้างplayer)
		# หากชนขอบจอขวา ให้ปรับค่า pxchange เป็น +1
		px = WIDTH - psize
		px += pxchange
	else:
		# หากอยู่ระหว่างหน้าจอจะทำการบวก/ลบ ตาม pxchange
		px += pxchange
	

	############### run enemy ############
	#for i in range(5):
	Enemy(ex,ey)
	ey += eychange
	###########fire mask #############
	if mstate == 'fire':
		fire_mask(mx,my)
		my = my - mychange # my -= mychange

	# เช็คว่า mask ชน ขอบหรือยัง? ถ้าชน เปลี่ยน state เป็น ready
	if my <= 0:
		my = HEIGHT - psize
		mstate = 'ready'

	# เช็คว่าชนกันหรือไม่
	collision = isCollision(ex,ey,mx,my)
	if collision:
		my = HEIGHT - psize
		mstate = 'ready'
		ey = 0
		ex = random.randint(0 + esize,WIDTH - esize)


	print(px)
	pygame.display.update()
	#pygame.display.flip()
	#pygame.event.pump()
	screen.fill((0,0,0))
	clock.tick(FPS)