############### IMPORT MODULES ###############
# In order to allow this application to work #
#   properly, several dependencies must be   #
#                  imported.                 #
##############################################



import os  # import 'os' to access system
import pyautogui as pag  # import 'pyautogui' to manually edit videos
import time  # import 'time' for wait times

from datetime import datetime as dt  # import 'datetime' to get accurate date for title
from datetime import timedelta as td  # import 'datetime' to get accurate date for title



############### PRE-REQS ###############
# This section of code is meant to run #
#  any lines of code that needed to be #
#  run first, but also lines of code I #
#  felt should have their own section. #
########################################



print("Searching for old 'piano_practice-mm-dd-yyyy'...")  # notify user of old 'piano_practice-mm-dd-yyyy' search

if os.path.exists(
        f'/Users/matthewbeck/Downloads/piano_practice-{dt.strftime(dt.now() - td(1), "%m-%d-%Y")}.mp4'):  # if file from 'piano_practice-mm-yesterday-yyyy' still exists...

    os.remove(
        f'/Users/matthewbeck/Downloads/piano_practice-{dt.strftime(dt.now() - td(1), "%m-%d-%Y")}.mp4')  # ...delete 'piano_practice-mm-yesterday-yyyy'
    print("Deleted old 'piano_practice-mm-dd-yyyy'.")  # ...notify user of old 'piano_practice-mm-dd-yyyy' deletion

else:  # if file from 'piano_practice-mm-yesterday-yyyy' not found...

    print("No old 'piano_practice-mm-dd-yyyy' found.")  # ...pass



############### NAME AND PATH CREATION ###############
# Before the process starts, some constants must be  #
#  defined in order to properly name each .mp4 file, #
#    named 'youTubeTitle', 'timelapseTitle', and     #
#                  'timelapsePath'.                  #
######################################################



##### 'determineWeek' FUNCTION #####

def determineWeek():  # 'determineWeek' function for determining 'week'

    global week # let 'week' be global var

    try: # attempt prompt for 'week'

        week = int(input("What week are you on?\n")) # prompt user for 'week' number (∞)
        return week # return 'week' value

    except: # if incorrect input entered...

        print("Invalid input entered;") # ...print invalid input error statement
        determineWeek() # ...re-call 'determineWeek' for accurate 'week'

##### 'determineDay' FUNCTION #####

def determineDay():  # 'determineWeek' function for determining 'day'

    global day # let 'day' be global var

    try: # attempt prompt for 'day'

        day = int(input("What day are you on?\n")) # prompt user for 'day' number (1-7)

        if (day <= 7): # if compatible 'day' correctly entered...

            return day # return 'day' value

        else: # if incorrect 'day' entered...

            print("Invalid day entered;") # ...print incorrect day error statement
            determineDay() # ...re-call 'determineDay' for accurate 'day'

    except: # if incorrect input entered...

        print("Invalid input entered;") # ...print invalid input error statement
        determineDay() # ...re-call 'determineDay' for accurate 'day'

##### 'determineSessionNumber' FUNCTION #####

def determineSessionNumber():  # 'DetermineSessionNumber' function for determining 'SessionNumber'

    global sessionNumber # let 'sessionNumber' be global var

    try: # attempt prompt for 'SessionNumber'

        sessionNumber = int(input("What session are you on?\n")) # prompt user for 'SessionNumber' number (∞)
        return sessionNumber # return 'sessionNumber' value

    except: # if incorrect input entered...

        print("Invalid input entered;")  # ...print invalid input error statement
        determineSessionNumber()  # ...re-call 'determineSessionNumber' for accurate 'SessionNumber'

##### 'promptConstants' FUNCTION #####

def promptConstants():

    confirmation = input(f"Confirm week and day '{str(week)}-{str(day)}' and session number '{sessionNumber}' are all correct (Y/N):\n")  # confirm

    if (confirmation == 'Y' or confirmation == 'y'):  # if correct timing entered...

        timelapseTitle = f'piano_practice-{str(week)}-{str(day)}.mp4'  # ...create timelapse title as 'timelapseTitle'
        timelapsePath = f'/Users/matthewbeck/Downloads/Videos/Piano_Practice/Week_{str(week)}'  # ...create timelapse path as 'timelapsePath'

        return timelapseTitle, timelapsePath  # return constant values 'sessionNumber', 'timelapseTitle', and 'timelapsePath' from 'determineConstants' function

    elif (confirmation == 'N' or confirmation == 'n'):  # if incorrect timing entered...

        promptConstants()  # ...re-call 'determineConstants' for accurate week and day

    else:  # if incorrect input entered...

        print("Invalid input entered;")  # ...print invalid input error statement
        promptConstants()  # ...re-call 'determineConstants' for accurate week and day

##### DETERMINE CONSTANTS #####

print("Determining constants...")  # notify user constants are being determined

week = determineWeek() # assign 'determineWeek' value to 'week'

day = determineDay() # assign 'determineDay' value to 'day'

sessionNumber = determineSessionNumber() # assign 'determineSessionNumber' value to 'SessionNumber'

premiereTitle = f'piano_practice-{dt.now().strftime("%m-%d-%Y")}'  # create title for 'Adobe Premiere Pro' file as 'premiereTitle'

timelapseTitle, timelapsePath = promptConstants()  # call 'determineConstants' function to determine 'sessionNumber', 'timelapseTitle', and 'timelapsePath' values

youTubeTitle = f"Piano Practice {sessionNumber}- 'The Ultimate Price' from Violet Evergarden, by Evan Call"  # create title for video as 'youTubeTitle'

youTubePath = f'/Users/matthewbeck/Downloads/{premiereTitle}.mp4'  # create path for video as 'youTubePath'

print("Determined constants.")  # notify user all constants determined



############### IMPORT VIDEO FROM ANDROID ###############
#   Once the file names are created, the actual video   #
# must be pulled from the Android phone. In order to do #
#   this, Android Debug Bridge (ADB) and a customized   #
#  .command file is utilized to find and download the   #
#       file to the computers 'Downloads' folder.       #
#########################################################



##### FIND AND ASSIGN VIDEO #####

os.system("/Users/matthewbeck/Desktop/Projects/Video_Automator/get_android_mp4.command")  # run script to retrieve recorded file from phone to 'Downloads' folder

print("You may now safely unplug your Android device.")  # notify user of safe phone removal



############### EDIT AND EXPORT 'piano_practice-mm-dd-yyyy' ###############
#   Below is the code used to edit the recorded video imported from the   #
#  Android device. In order to actually control Adobe Premiere Pro with a #
#     computer, I tried several methods, only one of which eventually     #
#   working; first, I tried learning excalibur, only to find out that it  #
#    was deprecated, and would no longer work; next, I tried writing an   #
#     Applescript, only to find that it was not compatible with Adobe     #
# Premiere Pro; after that, I tried to use terminal commands, but I could #
# not find a reliable way to get terminal to interact with Adobe Premiere #
#    Pro's many buttons; finally, what ended up working, was using the    #
#    pyautogui module to manually press every button I would press when   #
#   performing my usual video edits. Some sacrifices had to be made, but  #
#                this method proved acceptable in the end.                #
###########################################################################



##### OPEN APP PANEL #####

pag.moveTo(920, 1049, duration=0)  # move mouse to bottom of screen
pag.moveTo(925, 1049, duration=1)  # 'shake' mouse to pop up app menu

##### CREATE FILE IN ADOBE PREMIERE #####

pag.click(925, 1049)  # click 'Adobe Premiere Pro'
time.sleep(30)  # wait 30 seconds to allow 'Adobe Premiere Pro' to load
pag.click(39, 72)  # maximize window size
time.sleep(1)  # wait 1 second for window to expand
pag.click(70, 160)  # click 'New Project' button
time.sleep(5)  # wait 5 seconds to allow 'New Project' menu to open
pag.press('enter')  # create new project as 'Untitled'
pag.click(1033, 547)  # replace old 'Untitled' project

##### IMPORT VIDEO TO FILE #####

pag.click(165, 10)  # click 'File' in top laptop menu
pag.click(165, 580)  # click 'Import' option in 'File' menu
time.sleep(5)  # wait 5 seconds for 'Finder' window to load
pag.click(609, 287)  # click imported video from phone in 'Downloads' folder
pag.click(1185, 575)  # click 'Import' button to import video

##### DRAG VIDEO TO TIMELINE #####

time.sleep(5)  # wait 5 seconds for video file to load in 'Media Browser'
pag.moveTo(122, 748)  # move mouse to hover over video in 'Media Browser'
pag.mouseDown(button='left')  # click and hold mouse over video
pag.moveTo(847, 808, 0.5)  # drag video to 'Timeline'
pag.mouseUp(button='left')  # drop video in 'Timeline'
pag.click(929, 790)  # select video by clicking it

##### APPLY DENOISE EFFECT #####

time.sleep(20)  # wait 20 seconds for video file to load in 'Timeline'
pag.click(25, 80)  # re-click effects panel
pag.click(1380, 250)  # click 'Regular Effects' folder in 'Effects' panel
pag.moveTo(1445, 270)  # move mouse to hover over 'DeNoise' effect
pag.mouseDown(button='left')  # click and hold mouse over 'DeNoise' effect
pag.moveTo(720, 790, 0.5)  # drag 'DeNoise' effect over video in 'Timeline'
pag.mouseUp(button='left')  # drop 'DeNoise' effect over video

##### EXPORT VIDEO FOR YOUTUBE #####

pag.click(290, 45)  # click 'Export' in top 'Adobe Premiere Pro' menu
time.sleep(5)  # wait 5 seconds for 'Export' window to load
pag.click(445, 140)  # select original video name
pag.press('delete')  # press 'delete' to remove original name
pag.write('VE')  # write 'VE' for 'Video_Editor' as a stand-in name
pag.doubleClick(1630, 945)  # double-click 'Export' button to export video

##### RENAME 'VE.mp4' TO 'piano_practice-mm-dd-yyyy' #####

time.sleep(1200)  # wait 1200 seconds (20 minutes) for video to complete exporting process

os.rename('/Users/matthewbeck/Downloads/VE.mp4', youTubePath)  # rename 'VE.mp4' to 'youTubePath'



############### EDIT AND EXPORT 'piano_practice-w-d' ###############
#              After editing and exporting the edited              #
#    'piano_practice-mm-dd-yyyy' video, this section of code is    #
#     utilized to edit the video down into a roughly 35-second     #
#                            timelapse.                            #
####################################################################



##### SELECT EDIT OPTION #####

pag.click(235, 45)  # select 'Edit' in top 'Adobe Premiere Pro' menu

##### APPLY POSTERIZE TIME EFFECT #####

time.sleep(5)  # wait 5 seconds for 'Edit' screen to load
pag.click(720, 790)  # select video by clicking it
pag.moveTo(1445, 290)  # move mouse to hover over 'Posterize Time' effect
pag.mouseDown(button='left')  # click and hold mouse over 'Posterize Time' effect
pag.moveTo(720, 790, 0.5)  # drag 'Posterize Time' effect over video in 'Timeline'
pag.mouseUp(button='left')  # drop 'Posterize Time' effect over video

##### ADJUST FRAME RATE #####

pag.click(280, 410)  # click 'Frame Rate' in 'Effect Controls'
pag.write('1')  # write '1' to change 'Frame Rate' from '24' to '1'
pag.press('enter')  # enter '1' to close 'Frame Rate' option

##### ADJUST SPEED TO 10000 PERCENT #####

pag.rightClick(720, 790)  # right click video in 'Timeline'
pag.moveTo(760, 810)  # hover mouse over options
pag.scroll(-100)  # scroll past all options
pag.click(760, 475)  # select 'Speed/Duration'
pag.hotkey('ctrl', 'v')  # bypass weird clicking glitch to select 'Speed'
pag.typewrite("00")  # write '00' to go from '100' to '10000' percent speed
pag.press('enter')  # enter '10000' to close 'Speed' option
pag.press('enter')  # enter '10000' to close 'Speed/Duration' option

##### RENDER SELECTION #####

time.sleep(5)  # wait for 'Speed/Duration' menu to close
pag.click(320, 10)  # click 'Sequence' in top laptop menu
pag.click(320, 120)  # click 'Render Selection' in 'Sequence' menu

##### MUTE VIDEO x1 #####

time.sleep(170)  # wait 180 seconds (3 minutes) for sequence to complete loading
pag.click(590, 820)  # click 'Mute' button in 'Timeline'

##### EXPORT VIDEO FOR TIMELAPSE x1 #####

pag.click(290, 45)  # click 'Export' in top 'Adobe Premiere Pro' menu
time.sleep(5)  # wait 5 seconds for 'Export' window to load
pag.click(445, 140)  # select original video name
pag.press('delete')  # press 'delete' to remove original name
pag.write('VE')  # write 'VE' for 'Video_Editor' as a stand-in name
pag.doubleClick(1630, 945)  # double-click 'Export' button to export video

##### MUTE VIDEO x2 #####

time.sleep(10) # wait 10 seconds for menu to go away
pag.click(590, 820) # click 'Mute' button in 'Timeline'

##### EXPORT VIDEO FOR TIMELAPSE x2 #####

pag.click(290, 45)  # click 'Export' in top 'Adobe Premiere Pro' menu
time.sleep(5)  # wait 5 seconds for 'Export' window to load
pag.click(445, 140)  # select original video name
pag.press('delete')  # press 'delete' to remove original name
pag.write('VE')  # write 'VE' for 'Video_Editor' as a stand-in name
pag.doubleClick(1630, 945)  # double-click 'Export' button to export video

##### CLOSE ADOBE PREMIERE PRO #####

time.sleep(600) # wait 600 seconds (10 minutes) for 'piano_practice-w-d' to complete exporting process
pag.click(18, 44) # close 'Adobe Premiere Pro' window
pag.click(840, 540) # disregard saving warning

##### REFACTOR 'VE.mp4' TO 'piano_practice-w-d' #####

os.rename('/Users/matthewbeck/Downloads/VE.mp4',
          f'/Users/matthewbeck/Downloads/{timelapseTitle}')  # rename 'VE.mp4' to 'timelapsePath'



############### UPLOAD 'piano_practice-mm-dd-yyyy' TO YOUTUBE ###############
#    After 'piano_practice-mm-dd-yyyy' and 'piano_practice-w-d' are done    #
# editing, this section of instructions uploads 'piano_practice-mm-dd-yyyy' #
# to YouTube as the Google Cloud API cannot handle my larger-than-5GB file  #
#                  sizes that are typical of this process.                  #
#############################################################################



##### OPEN 'Google Chrome' #####

time.sleep(5) # wait for 'Adobe Premiere Pro' to completely shut down
pag.click(525, 1020) # open 'Google Chrome'
time.sleep(5) # wait 5 seconds for 'Google Chrome' to load
pag.moveTo(135, 0, duration=0) # move mouse to top of screen
pag.moveTo(136, 0, duration=1)  # 'shake' mouse to pop up 'Google Chrome' menu
pag.click(135, 0) # click 'file'
time.sleep(1) # wait 1 second for 'file' to load
pag.click(135, 40) # click 'New Tab'
time.sleep(3) # wait 3 seconds for 'New Tab' to load
pag.click(66, 75) # click to expand 'Google Chrome' window
time.sleep(3) # wait 3 seconds for window to expand
pag.click(215, 95) # click on 'studio.youtube.com'

##### CREATE NEW 'piano_practice-mm-dd-yyyy' VIDEO #####

time.sleep(5) # wait 5 seconds for 'studio.youtube.com' to load
pag.click(1558, 111) # click on 'CREATE'
time.sleep(3) # wait 3 seconds for 'CREATE' options bar to load
pag.click(1558, 152) # click on 'Upload Videos'
time.sleep(3) # wait 3 seconds for page to open
pag.click(842, 681) # click on 'SELECT FILES'
time.sleep(1) # wait 1 seconds for page
pag.click(720, 430) # click on 'piano_practice-mm-dd-yyyy'
pag.hotkey('ctrl', 'v') # bypass weird clicking glitch to click on 'piano_practice-mm-dd-yyyy'
pag.click(720, 430) # click on 'piano_practice-mm-dd-yyyy' to avoid glitch
pag.click(1190, 720) # open 'piano_practice-mm-dd-yyyy'

##### EDIT 'piano_practice-mm-dd-yyyy' NAME #####

time.sleep(5) # wait 5 seconds for 'piano_practice-mm-dd-yyyy' to load
pag.click(895, 294) # open 'REUSE DETAILS'
time.sleep(3) # wait 5 seconds for 'REUSE DETAILS' to load
pag.click(645, 435) # click previous 'piano_practice-mm-dd-yyyy'
time.sleep(3) # wait 3 seconds for previous 'piano_practice-mm-dd-yyyy' to load
pag.click(1148, 830) # click on 'REUSE'
pag.click(558, 367) # click on previous 'piano_practice-mm-dd-yyyy' name
pag.hotkey('ctrl', 'v') # bypass weird clicking glitch to select 'piano_practice-mm-dd-yyyy'
pag.click(521, 365) # click on previous 'piano_practice-mm-dd-yyyy' name to avoid glitch

for i in range(len(str(sessionNumber - 1))): # loop to delete previous session number

    time.sleep(1)  # built-in pause
    pag.press('delete') # press 'delete' n times to remove original 'piano_practice-mm-dd-yyyy' session number

pag.typewrite(str(sessionNumber)) # write 'sessionNumber' for current 'piano_practice-mm-dd-yyyy'
time.sleep(1) # built-in pause
pag.scroll(-1000) # scroll all the way to the bottom of the page
time.sleep(1) # built-in pause
pag.click(420, 760) # click 'No it's not made for kids'

for i in range(3): # loop to press 'NEXT' button

    time.sleep(1)  # built-in pause
    pag.click(1280, 975) # click on 'NEXT'

pag.click(470, 550) # click 'Public' to upload as public video
pag.click(1280, 975) # click on 'PUBLISH'

##### POWER OFF COMPUTER #####

os.system("pmset sleepnow") # make computer fall asleep
