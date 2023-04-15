############### IMPORT MODULES ###############
# In order to allow this application to work #
#   properly, several dependencies must be   #
#                  imported.                 #
##############################################



import glob # import 'glob' to access filepath
import os # import 'os' to access system
import cv2 # import 'cv2' to determine video width
import pyautogui as pag # import 'pyautogui' to manually edit videos
import time # import 'time' for wait times

from datetime import datetime as dt # import 'datetime' to get accurate date for title
from datetime import timedelta as td # import 'datetime' to get accurate date for title
#from googleapiclient.discovery import build # import 'build' to construct service client to Google's API
#from googleapiclient.errors import HttpError # import 'HttpError' for error raising
#from googleapiclient.http import MediaFileUpload # import 'MediaFileUpload' for uploading media to YouTube



############### PRE-REQS ###############
# This section of code is meant to run #
#  any lines of code that needed to be #
#  run first, but also lines of code I #
#  felt should have their own section. #
########################################



print("Searching for old 'piano_practice-mm-dd-yyyy'...") # notify user of old 'piano_practice-mm-dd-yyyy' search

if os.path.exists(f'/Users/matthewbeck/Downloads/piano_practice-{dt.strftime(dt.now() - td(1), "%m-%d-%Y")}.mp4'): # if file from 'piano_practice-mm-yesterday-yyyy' still exists...

    os.remove(f'/Users/matthewbeck/Downloads/piano_practice-{dt.strftime(dt.now() - td(1), "%m-%d-%Y")}.mp4') # ...delete 'piano_practice-mm-yesterday-yyyy'
    print("Deleted old 'piano_practice-mm-dd-yyyy'.") # ...notify user of old 'piano_practice-mm-dd-yyyy' deletion

else: # if file from 'piano_practice-mm-yesterday-yyyy' not found...

    print("No old 'piano_practice-mm-dd-yyyy' found.") # ...pass



############### NAME AND PATH CREATION ###############
# Before the process starts, some constants must be  #
#  defined in order to properly name each .mp4 file, #
#    named 'youTubeTitle', 'timelapseTitle', and     #
#                  'timelapsePath'.                  #
######################################################



##### 'determineConstants' FUNCTION #####

def determineConstants(): # 'determineConstants' function to determine timelapse title

    try: # attempt prompt for 'week'

        week = int(input("What week are you on?\n")) # prompt user for week number (∞)

    except: # if incorrect input entered...

        print("Invalid input entered;") # ...print invalid input error statement
        determineConstants() # ...re-call 'determineConstants' for accurate week and day

    try: # attempt prompt for 'day'

        day = int(input("What day are you on?\n")) # prompt user for day number (1-7)

        if (day <= 7): # if compatible day correctly entered...

            pass # ...pass

        else: # if incorrect day entered...

            print("Invalid day entered;") # ...print incorrect day error statement
            determineConstants() # ...re-call 'determineConstants' for accurate week and day

    except: # if incorrect input entered...

        print("Invalid input entered;") # ...print invalid input error statement
        determineConstants() # ...re-call 'determineConstants' for accurate week and day

    try:  # attempt prompt for 'sessionNumber'

        sessionNumber = int(input("What session number did you complete?\n"))  # prompt user for session number (∞)

    except:  # if incorrect input entered...

        print("Invalid input entered;")  # ...print invalid input error statement
        determineConstants()  # ...re-call 'determineConstants' for accurate week and day

    confirmation = input(f"Confirm week and day '{str(week)}-{str(day)}' and session number '{sessionNumber}' are all correct (Y/N):\n") # confirm date

    if (confirmation == 'Y' or confirmation == 'y'): # if correct timing entered...

        timelapseTitle = f'piano_practice-{str(week)}-{str(day)}.mp4' # ...create timelapse title as 'timelapseTitle'
        timelapsePath = f'/Users/matthewbeck/Downloads/Videos/Piano_Practice/Week_{str(week)}' # ...create timelapse path as 'timelapsePath'

        return sessionNumber, timelapseTitle, timelapsePath  # return constant values 'sessionNumber', 'timelapseTitle', and 'timelapsePath' from 'determineConstants' function

    elif (confirmation == 'N' or confirmation == 'n'): # if incorrect timing entered...

        determineConstants() # ...re-call 'determineConstants' for accurate week and day

    else: # if incorrect input entered...

        print("Invalid input entered;") # ...print invalid input error statement
        determineConstants() # ...re-call 'determineConstants' for accurate week and day

##### DETERMINE CONSTANTS #####

print("Determining constants...") # notify user constants are being determined

premiereTitle = f'piano_practice-{dt.now().strftime("%m-%d-%Y")}' # create title for 'Adobe Premiere Pro' file as 'premiereTitle'

sessionNumber, timelapseTitle, timelapsePath = determineConstants() # call 'determineConstants' function to determine 'sessionNumber', 'timelapseTitle', and 'timelapsePath' values

youTubeTitle = f"Piano Practice {sessionNumber}- 'The Ultimate Price' from Violet Evergarden, by Evan Call" # create title for video as 'youTubeTitle'

youTubePath = f'/Users/matthewbeck/Downloads/{premiereTitle}.mp4' # create path for video as 'youTubePath'

print("Determined constants.") # notify user all constants determined



############### IMPORT VIDEO FROM ANDROID ###############
#   Once the file names are created, the actual video   #
# must be pulled from the Android phone. In order to do #
#   this, Android Debug Bridge (ADB) and a customized   #
#  .command file is utilized to find and download the   #
#       file to the computers 'Downloads' folder.       #
#########################################################



##### FIND AND ASSIGN VIDEO #####

os.system("/Users/matthewbeck/Desktop/Projects/Video_Automator/get_android_mp4.command") # run script to retrieve recorded file from phone to 'Downloads' folder

print("You may now safely unplug your Android device.") # notify user of safe phone removal

videoFile = cv2.VideoCapture(max(glob.glob('/Users/matthewbeck/Downloads/*.mp4'), key=os.path.getctime)) # create file path to video as 'videoFile'



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



########## 'editVideo' FUNCTION ##########

def editVideo(degrees): # 'editVideo' function to edit video based on video width

    ##### OPEN APP PANEL #####

    pag.moveTo(920, 1049, duration=0) # move mouse to bottom of screen
    pag.moveTo(925, 1049, duration=1) # 'shake' mouse to pop up app menu

    ##### CREATE FILE IN ADOBE PREMIERE #####

    pag.click(925, 1049) # click 'Adobe Premiere Pro'
    time.sleep(30) # wait 30 seconds to allow 'Adobe Premiere Pro' to load
    pag.click(72, 198) # click 'New Project' button
    time.sleep(5) # wait 5 seconds to allow 'New Project' menu to open
    pag.press('enter') # create new project as 'Untitled'
    pag.click(1030, 550) # delete old 'Untitled' project

    ##### IMPORT VIDEO TO FILE #####

    pag.click(165, 10) # click 'File' in top laptop menu
    pag.click(165, 580) # click 'Import' option in 'File' menu
    time.sleep(5) # wait 5 seconds for 'Finder' window to load
    pag.click(625, 300) # click imported video from phone in 'Downloads' folder
    pag.click(1185, 575) # click 'Import' button to import video

    ##### DRAG VIDEO TO TIMELINE #####

    time.sleep(5) # wait 5 seconds for video file to load in 'Media Browser'
    pag.moveTo(155, 755) # move mouse to hover over video in 'Media Browser'
    pag.mouseDown(button='left') # click and hold mouse over video
    pag.moveTo(460, 755, 0.5) # drag video to 'Timeline'
    pag.mouseUp(button='left') # drop video in 'Timeline'
    pag.click(720, 790) # select video by clicking it

    ##### APPLY DENOISE EFFECT #####

    pag.click(25, 80) # re-click effects panel
    pag.click(1380, 250) # click 'Regular Effects' folder in 'Effects' panel
    pag.moveTo(1445, 270) # move mouse to hover over 'DeNoise' effect
    pag.mouseDown(button='left') # click and hold mouse over 'DeNoise' effect
    pag.moveTo(720, 790, 0.5) # drag 'DeNoise' effect over video in 'Timeline'
    pag.mouseUp(button='left') # drop 'DeNoise' effect over video

    ##### INCREASE SOUND BY 10 DECIBELS #####

    pag.rightClick(720, 790) # right click video in 'Timeline'
    pag.moveTo(760, 810) # hover mouse over options
    pag.scroll(-100) # scroll past all options
    pag.click(760, 530) # select 'Audio Gain'
    pag.write("10") # write '10' for 10 decibels
    pag.press('enter') # enter '10' to close 'Audio Gain' option

    ##### TILT VIDEO BY -4 DEGREES #####

    pag.click(280, 265) # click 'Rotation' in 'Effect Controls'
    pag.write("-") # write '-' to subvert weird glitch
    pag.click(280, 265) # click 'Rotation' in 'Effect Controls'
    pag.write(f"{degrees}") # rotate/tilt video by 'degrees' degrees
    pag.press('enter') # enter 'degrees' degrees to close 'Rotation' option

    ##### SCALE VIDEO BY 113.5 TIMES #####

    pag.click(280, 200) # click 'Scale' in 'Effect Controls'
    pag.write("113.5") # write '113.5' to scale video 113%
    pag.press('enter') # enter '113.5' to close 'Scale' option

    ##### EXPORT VIDEO FOR YOUTUBE #####

    pag.click(290, 45) # click 'Export' in top 'Adobe Premiere Pro' menu
    time.sleep(5) # wait 5 seconds for 'Export' window to load
    pag.click(445, 140) # select original video name
    pag.press('delete') # press 'delete' to remove original name
    pag.write('VE') # write 'VE' for 'Video_Editor' as a stand-in name
    pag.doubleClick(1630, 945) # double-click 'Export' button to export video

    ##### RENAME 'VE.mp4' TO 'piano_practice-mm-dd-yyyy' #####

    time.sleep(1500) # wait 1500 seconds (25 minutes) for video to complete exporting process

    os.rename('/Users/matthewbeck/Downloads/VE.mp4', youTubePath) # rename 'VE.mp4' to 'youTubePath'

##### DETERMINE VIDEO RESOLUTION SCRIPT #####

print(f"Video resolution width: {str(videoFile.get(cv2.CAP_PROP_FRAME_WIDTH))}px.") # display video resolution information

print(f"Screen resolution: {pag.size()}") # display screen resolution information

##### PORTRAIT MODE EDIT #####

if (videoFile.get(cv2.CAP_PROP_FRAME_WIDTH) <= 1080): # if resolution indicates 'rawVideo' is in portrait mode...

    editVideo(86) # call 'editVideo' function to edit video and rotate it 86 degrees

##### LANDSCAPE MODE EDIT #####

elif (videoFile.get(cv2.CAP_PROP_FRAME_WIDTH) >= 1920): # if 'rawVideo' resolution is normal...

    editVideo(-4) # call 'editVideo' function to edit video and tilt it -4 degrees



############### EDIT AND EXPORT 'piano_practice-w-d' ###############
#              After editing and exporting the edited              #
#    'piano_practice-mm-dd-yyyy' video, this section of code is    #
#     utilized to edit the video down into a roughly 35-second     #
#                            timelapse.                            #
####################################################################



##### SELECT EDIT OPTION #####

pag.click(235, 45) # select 'Edit' in top 'Adobe Premiere Pro' menu

##### APPLY POSTERIZE TIME EFFECT #####

time.sleep(5) # wait 5 seconds for 'Edit' screen to load
pag.click(720, 790) # select video by clicking it
pag.moveTo(1445, 290) # move mouse to hover over 'Posterize Time' effect
pag.mouseDown(button='left') # click and hold mouse over 'Posterize Time' effect
pag.moveTo(720, 790, 0.5) # drag 'Posterize Time' effect over video in 'Timeline'
pag.mouseUp(button='left') # drop 'Posterize Time' effect over video

##### ADJUST FRAME RATE #####

pag.click(280, 410) # click 'Frame Rate' in 'Effect Controls'
pag.write('1') # write '1' to change 'Frame Rate' from '24' to '1'
pag.press('enter') # enter '1' to close 'Frame Rate' option

##### ADJUST SPEED TO 10000 PERCENT #####

pag.rightClick(720, 790) # right click video in 'Timeline'
pag.moveTo(760, 810) # hover mouse over options
pag.scroll(-100) # scroll past all options
pag.click(760, 475) # select 'Speed/Duration'
pag.hotkey('ctrl', 'v') # bypass wierd clicking glitch to select 'Speed'
pag.typewrite("00") # write '00' to go from '100' to '10000' percent speed
pag.press('enter') # enter '10000' to close 'Speed' option
pag.press('enter') # enter '10000' to close 'Speed/Duration' option

##### RENDER SELECTION #####

time.sleep(5) # wait for 'Speed/Duration' menu to close
pag.click(320, 10) # click 'Sequence' in top laptop menu
pag.click(320, 120) # click 'Render Selection' in 'Sequence' menu

##### MUTE VIDEO x1 #####

time.sleep(170) # wait 180 seconds (3 minutes) for sequence to complete loading
pag.click(590, 820) # click 'Mute' button in 'Timeline'

##### EXPORT VIDEO FOR TIMELAPSE x1 #####

pag.click(290, 45) # click 'Export' in top 'Adobe Premiere Pro' menu
time.sleep(5) # wait 5 seconds for 'Export' window to load
pag.click(445, 140) # select original video name
pag.press('delete') # press 'delete' to remove original name
pag.write('VE') # write 'VE' for 'Video_Editor' as a stand-in name
pag.doubleClick(1630, 945) # double-click 'Export' button to export video

##### MUTE VIDEO x2 #####

time.sleep(10) # wait 10 seconds for menu to go away
pag.click(590, 820) # click 'Mute' button in 'Timeline'

##### EXPORT VIDEO FOR TIMELAPSE x2 #####

pag.click(290, 45) # click 'Export' in top 'Adobe Premiere Pro' menu
time.sleep(5) # wait 5 seconds for 'Export' window to load
pag.click(445, 140) # select original video name
pag.press('delete') # press 'delete' to remove original name
pag.write('VE') # write 'VE' for 'Video_Editor' as a stand-in name
pag.doubleClick(1630, 945) # double-click 'Export' button to export video

##### REFACTOR 'VE.mp4' TO 'piano_practice-w-d' #####

time.sleep(600) # wait 600 seconds (10 minutes) for 'piano_practice-w-d' to complete exporting process

os.rename('/Users/matthewbeck/Downloads/VE.mp4', f'/Users/matthewbeck/Downloads/{timelapseTitle}') # rename 'VE.mp4' to 'timelapsePath'



############### UPLOAD 'piano_practice-mm-dd-yyyy' TO YOUTUBE ###############
#    Upon finishing the editing process, the file can then be uploaded to   #
#                     YouTube via Google's YouTube API.                     #
#   NOTE: Currently, there is no efficient way (that I have found) to send  #
#       large 4GB+ files via automation; further testing is required.       #
#############################################################################



#os.system(f'python /Users/matthewbeck/Desktop/Projects/Video_Automator/video_uploader.py --file={youTubePath} [--title={youTubeTitle}]\n[--description={youTubeDescription}] [--category="10"]\n[--keywords="piano,violet evergarden,practice"]\n[--privacyStatus=unlisted]')
# run terminal command to call 'video_uploader.py' to upload video to YouTube, deprecated

#try: # attempt to upload video to YouTube

#    youtube = build("youtube", "v3", developerKey="") # establish legitimate connection to Google's API

#    request = youtube.videos().insert( # request video upload

#        part = "snippet,status", # retrieve snippet and status parts of YouTube resource to return

#        body = { # declare main 'piano_practice-mm-dd-yyyy' parameters

#            "snippet": { # assign previous constants to 'piano_practice-mm-dd-yyyy'

#                "title": f"{youTubeTitle}", # assign title based on 'youTubeTitle'

#                "description": f"{youTubeDescription}", # assign 'piano_practice-mm-dd-yyyy' based on 'youTubeDescription'

#                "tags": ["piano", "violet evergarden", "practice"], # declare key words

#                "categoryId": 10 # set category to '10' (music)
#            },

#            "status": { # declare privacy status parameter

#                "privacyStatus": "unlisted" # set privacy status to unlisted
#            }
#        },

#        media_body = MediaFileUpload(youTubePath, mimetype="video/mp4") # upload 'piano_practice-mm-dd-yyyy' to YouTube with 'youTubePath'
#    )

#    response = request.execute()

#    print(response)

#except HttpError as error: # if video fails to upload via Google's API...

#    print("An error occurred: %s" % error) # ...raise exception error


############### HOUSEKEEPING ###############
#     Once the video has completed its     #
#    downloading, editing, and uploading   #
#   processes, these lines of code 'clean  #
#    up' the file and then turns off the   #
#                 computer.                #
############################################



videoFile.release() # close video preview

cv2.destroyAllWindows() # close cv2 window

os.system()

os.system("pmset sleepnow") # make computer fall asleep
