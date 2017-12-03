import sys

def run():
	pygame.init()
	screen = pygame.display.set_mode((1200, 800))
	pygame.display.set_caption("break aliens")

	while true:
		for event in pygame.event.get():
			if event.type == pygame.QUIT;
				sys.exit()

		pygame.display.flip()

run()
