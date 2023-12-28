##if ur reading this god please spare my soul, im doing my damn best
#
#              This is all custom screen work that i threw here to find it a ton easier than digging thru gui 
#              and screens file trying to look for one line to tweak a decimal place
#
####################

#if youre looking for how to add the icons next to their names in chat,, the tip is theyre nvl mode instead of ADV, but if u look at line like 1350 in screens.rpy
# u can see where i added the icon argument for positioning, and then u can see how theyre defined in the script
#slay




#####MUSIC PLAYER
init python:

    # Step 1. Create a MusicRoom instance.
    mr = MusicRoom(fadeout=1.0)

    #File path, title, artist
    song_list = [
                ["music/Byte.wav", 'Byte', 'Tocirah'],
                ["music/Stride.mp3", 'Stride', 'ADthsnd'],
                ["music/Dial.wav", 'Dial', 'Tocirah'],
                ["music/Enhance.wav", 'Enhance', 'Tocirah'],
                ["music/Funk.wav", 'Funk', 'Tocirah'],
                ["music/Telepathy.mp3", 'Telepathy', 'ADthsnd'],
                ["music/Jitter.wav", 'Jitter', 'Tocirah'],
                ["music/Sunshine.mp3", 'Sunshine', 'ADthsnd'],
                ["music/Lullaby.wav", 'Lullaby', 'Tocirah'],
                ["music/Whistle.wav", 'Whistle', 'Tocirah']
                ]
    song_description = ""
    song_name = ""
    current_track = ""
    


    for track in song_list:
        mr.add(track[0], always_unlocked = True, action=[SetVariable('current_track', track[0]), SetVariable("song_name",track[1]),SetVariable("song_description",track[2])])


    current_track = song_list[0][0]

    def GetCurrentTrack():
        
        if current_track == None:
            return ["","",""]
        debug_print("current_track - " + str(current_track) )
        return [item for item in song_list if item[0] == current_track][0]

    def GetTrackPos():
        return renpy.music.get_pos()

    def GetTrackDuration():
        return renpy.music.get_duration()





#this is the actual part that makes the mp3 player show, however max had a stupid and was testing out how new screens worked and got too lazy to change it back to a normal name

screen textmiddle:

    default music_is_playing = False #i know this seems contradictory but this is just the default states, plus i triggered music to start once we enter into game immediately
    default music_is_paused = False
    
    drag:
        draggable True
        droppable False
        drag_raise True
        pos(1375,50)
        drag_offscreen (200, 200)

        frame:
            background None
            
            image "gui/musicplayer.png" 

            $ playing = renpy.music.get_playing("music")
            if playing is not None:
                transclude
                $ track_name = track[1]
                $ track_creator = track[2]
            
                text "{size=25}Now Playing...{/size}" yalign 0.095 xalign 0.005
                text "[song_name] - [song_description]" yalign 0.125 xalign 0.065
                
            else:
                text "No Music Playing" xalign 0.5 yalign 0.5
            ##below are the buttons and how we set them up to work with the music rooM! not sure if its correct or not, but it works and thats all i care about at this point
            imagebutton auto "gui/mm_pause_%s.png":
                xpos 128
                ypos 175 
                focus_mask True #focus mask makes it hoverable, its just image buttons like ud see on the  main menu of games!
                action [SetVariable('current_track', renpy.music.get_playing()),
                        mr.TogglePause()]
                hovered [ Play("sound", "audio/click.wav") ]  #plays this sound when clicked

            imagebutton auto "gui/mp_play_%s.png":
                xpos 216 
                ypos 175 
                focus_mask True  
                action [SetVariable('current_track', renpy.music.get_playing()),
                        mr.TogglePause()]
                hovered [ Play("sound", "audio/click.wav") ]
            
            imagebutton auto "gui/mp_skip_%s.png" xpos 309 ypos 175 focus_mask True action mr.Next() hovered [ Play("sound", "audio/click.wav") ]


#displays the players username and online, trying to add the profile photo display here as well 
screen username:
    fixed:
        ypos 960
        xpos 85
        text "{size=30}[username]{/size}" #displays the players username
    fixed:
        ypos 990
        xpos 82
        text "{image=online.png}{size=23}online{/size}" #displays the online icon and the text 'online' next to it. there was no reason to add this other than the fact that i wanted the fonts to change when ppl selected other font options
    fixed:
        ypos 950
        xpos 11
        image Transform("[player_icon]", zoom=0.65) #this was added so that when the players icon changes in game, itll update on the left side too next to your username!

#i put all three of these on the same screen so that its essentially a mini profile and easier to hide all elements at once 



##Custom choice menu for icon select



##Add in custom group chat online list here