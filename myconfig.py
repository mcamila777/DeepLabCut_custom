# coding: utf-8

<<<<<<< HEAD
############################
# This configuration file sets various parameters for generation of training
# set file & evalutation of results
############################
=======
#####################################################################################
# This configuration file sets various parameters for generation of training
# set & evalutation of DeepLabCut
#####################################################################################
>>>>>>> public/master

# myconfig.py:

########################################
<<<<<<< HEAD
# Step 1:
Task = 'tanya' # 'pavel'#'standing'#'moving'#'reaching'  'combined'
########################################

# Filename and path to behavioral video:
vidpath = '.'
filename = 'video_2.mp4'#'reachingvideo1.avi'

cropping = False #True
=======
# Step 1: Selecting Frames from videos
########################################

Task = 'reaching'

# Filename and path to behavioral video:
vidpath = '.'
filename = 'reachingvideo1.avi'

cropping = True
>>>>>>> public/master

# ROI dimensions / bounding box (only used if cropping == True)
# x1,y1 indicates the top left corner and
# x2,y2 is the lower right corner of the croped region.

x1 = 0
x2 = 640
<<<<<<< HEAD
y1 = 0#277
y2 = 624


=======
y1 = 277
y2 = 624

>>>>>>> public/master
# Portion of the video to sample from in step 1. Set to 1 by default.
portion = 1

########################################
<<<<<<< HEAD
# Step 2:
########################################

#bodyparts = ["knee"] #["hand", "Finger1", "Finger2",  "Joystick"]  # Exact sequence of labels as were put by

bodyparts = ['tail tip', 'back right shoulder', 'tail start', 'front left knee', 'front left foot', 'chin', 'back right knee', 'left eye', 'front right ankle', 'nosetip', 'front right shoulder', 'front left shoulder', 'back left foot', 'right eye', 'back right ankle', 'left ear', 'front right knee', 'front right foot', 'back left shoulder', 'neck', 'front left ankle', 'back right foot', 'back left knee', 'right ear', 'back left ankle']

# annotator in *.csv file
Scorers = ['AMT']  # who is labeling?
=======
# Step 2: Converting frames to pandas array 
########################################

bodyparts = ["hand", "Finger1", "Finger2","Joystick"]  # Exact sequence of labels as were put by
# annotator in *.csv file
Scorers = ['Mackenzie']  # who is labeling?

# Set this true if the data was sequentially labeled and if there is one file per folder (you can set the name of this file below, i.e. multibodypartsfilename)
# Otherwise there should be individual files per bodypart, i.e. in our demo case hand.csv, Finger1.csv etc.
# If true then those files will be generated from Results.txt
multibodypartsfile=False 
multibodypartsfilename="Results.csv"
>>>>>>> public/master

# When importing the images and the labels in the csv/xls files should be in the same order!
# During labeling in Fiji one can thus (for occluded body parts) click in the origin of the image 
#(i.e. top left corner (close to 0,0)), these "false" labels will then be removed. To do so set the following variable:
#set this to 0 if no labels should be removed!
<<<<<<< HEAD
invisibleboundary=10 # If labels are closer to origin than this number they are set to NaN (not a number)

########################################
# Step 3:
########################################

date = 'May24' #'May03'#''May18'
scorer = 'AMT' #'camila'

# Userparameters for training set. Other parameters can be set in pose_cfg.yaml
Shuffles = range(3) #[1]  # Ids for shuffles, i.e. range(5) for 5 shuffles
TrainingFraction = [0.70]  # Fraction of labeled images used for training
=======

invisibleboundary=10 # If labels are closer to origin than this number they are set to NaN (not a number). Please adjust to your situation. Units in pixel.
 
imagetype=".png" # image type of labeled frames

########################################
# Step 3: Check labels / makes plots
########################################

colormap = 'cool' #set color map, i.e. viridis, cool, hsv
scale = 1  # for plotting
msize=10   #size of labels
alphavalue =.6 #transparency of labels

########################################
# Step 4: Generate Training Files 
########################################

date = 'Jan30'
scorer = 'Mackenzie'

# Userparameters for training set. Other parameters can be set in pose_cfg.yaml
Shuffles = [1]  # Ids for shuffles, i.e. range(5) for 5 shuffles
TrainingFraction = [0.95]  # Fraction of labeled images used for training
>>>>>>> public/master

# Which resnet to use
# (these are parameters reflected in the pose_cfg.yaml file)
resnet = 50

<<<<<<< HEAD
# trainingsiterations='1030000'

# For Evaluation/ Analyzing videos
# To evaluate model that was trained most set this to: "-1"
# To evaluate all models (training stages) set this to: "all"

snapshotindex = "all" #-1
shuffleindex = 0
=======
# For Evaluation/ Analyzing videos
# To evaluate the last model that was trained most set this to: -1 
# To evaluate all models (training stages) set this to: "all"  (as string!)

snapshotindex = -1 #"all"
shuffleindex = 0
pcutoff=.1 # likelihood. RMSE will be reported for all pairs and pairs with larger likelihood than pcutoff (see paper). This cutoff will also be used in plots.
plotting=True #If true will plot train & test images including DeepLabCut labels next to human labels. Note that this will be plotted for all snapshots as indicated by snapshotindex
>>>>>>> public/master
