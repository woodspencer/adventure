#!/usr/bin/env python
import libtcodpy as libtcod
import num_lib

class Screen:
	""" Screen for viewing the game
		includes screen properties
		such as frame_rate"""

	height = 50
	width = 80
	limit_fps = 20
	
	libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
	libtcod.console_init_root(width, height, 'Blossom Rogue', False)
	libtcod.sys_set_fps(limit_fps)
	
	def __init__ (self):
		""" Class initialiser """
		pass
		
class Player:
	""" Player Character Object """
	name = 'hero'
	hit_points = 0
	strength  = 0
	dexterity = 0
	endurance = 0

	location_x = Screen.width/2
	location_y = Screen.height/2
	avatar = '@'
	
	def __init__ (self):
		""" Class initialiser """
		pass
	


class Game:
	
	while not libtcod.console_is_window_closed():
		libtcod.console_set_foreground_color(0, libtcod.white)
		libtcod.console_print_left(0, Player.location_x, Player.location_y, libtcod.BKGND_NONE, Player.avatar)
		libtcod.console_flush()
	
		libtcod.console_print_left(0, Player.location_x, Player.location_y, libtcod.BKGND_NONE, ' ')
	
		exit = handle_keys()
		if exit:
			break
			
def handle_keys():
	
	key = libtcod.console_wait_for_keypress(True)

	if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Alt+Enter: toggle fullscreen
		libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
        
	elif key.vk == libtcod.KEY_ESCAPE:
		return True  #exit game
		
	if libtcod.console_is_key_pressed(libtcod.KEY_UP):
		Player.location_y -= 1
	
	elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
		Player.location_y += 1
		
	elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
		Player.location_x -= 1
		
	elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
		Player.location_x += 1
		
if __name__=='__main__':
	Game
