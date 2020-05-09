import tcod as libtcod


def main():
    screen_width = 80   #self exlpanatory
    screen_height = 50  #eventually will load these values from a JSON file

    player_x = int(screen_width / 2)    # places the player in the center of the screen
    player_y = int(screen_height / 2)   # int() function is used because py3 doesn't auto truncate division
                                        # int() casts the division result (a float) to an integer

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
        #tells libtcod which font to use
        #reading from 'arial10x10.png', next two parts are telling libtcod which type of file we're reading

    libtcod.console_init_root(screen_width, screen_height, 'roguelike 1st attempt', False)
        #this line creates the screen
        #gives it width and height values, a title, and a boolean value indicating fullscreen or not

    key = libtcod.Key()         #these variables hold our keyboard and mouse input
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed(): #the "game loop", never ends until the screen is closed
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse) #this function captures user input

        libtcod.console_set_default_foreground(0, libtcod.white) #set's the @ color, 0 is the console we're drawing to
        ## libtcod.console_put_char(0, 1, 1, '@', libtcod.BKGND_NONE) #0 is the console, "1, 1" are starting coordinates, '@' prints character symbol, libtcod.BKGND_NONE sets the background to none
        libtcod.console_put_char(0, player_x, player_y, '@', libtcod.BKGND_NONE)
        libtcod.console_flush() #"This is the part the presents everything on screen. Pretty straightforward."

        key = libtcod.console_check_for_keypress()  # This part allows us to exit by hitting Esc
                                                    # The libtcod.console_check_for_keypress() function takes keyboard input and stores it in the 'key' variable
        if key.vk == libtcod.KEY_ESCAPE:            # Then we check if the key pressed was the Esc key
            return True                             # If this is true, the loop exits


if __name__ == '__main__':
    main()