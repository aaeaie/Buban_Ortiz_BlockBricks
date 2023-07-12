class Colors:
	grey_lavender = (176, 161, 171)
	green = (0, 136, 10)
	red = (162, 11, 11)
	pink = (242, 60, 115)   
	yellow = (255, 255, 80)
	purple = (85, 35, 150)
	cyan = (3, 196, 169)
	blue = (13, 64, 216)
	white = (255, 255, 255)
	light_blue = (94, 210, 210)  

	@classmethod
	def get_cell_colors(cls):
		return [cls.grey_lavender, cls.green, cls.red, cls.pink, cls.yellow, cls.purple, cls.cyan, cls.blue]