
# coding: utf-8


#####################################################################################
# This configuration file sets various parameters for generation of training
# set & evalutation of DeepLabCut
#####################################################################################


# myconfig.py:

########################################

# Step 1:
Task = 'bounding_box' # 'tanya' # 'pavel'#'standing'#'moving'#'reaching'  'combined'
########################################

# Filename and path to behavioral video:
vidpath = '.'
filename = 'video_2.mp4'#'reachingvideo1.avi'

cropping = False #True


# ROI dimensions / bounding box (only used if cropping == True)
# x1,y1 indicates the top left corner and
# x2,y2 is the lower right corner of the croped region.

x1 = 0
x2 = 640
y1 = 0#277
y2 = 624



# Portion of the video to sample from in step 1. Set to 1 by default.
portion = 1

########################################

# Step 2:
########################################

#bodyparts = ["knee"] #["hand", "Finger1", "Finger2",  "Joystick"]  # Exact sequence of labels as were put by

bodyparts = ['tail tip', 'back right shoulder', 'tail start', 'front left foot tip', 'front left knee', 'chin', 'back left foot tip', 'back right knee', 'left nostril', 'left eye', 'front right ankle', 'end of mane', 'left ear tip', 'front right foot tip', 'front left shoulder', 'right ear tip', 'right eye', 'back right ankle', 'start of mane', 'front right knee', 'front right shoulder', 'back left shoulder', 'front left ankle', 'back left knee', 'back left ankle', 'back right foot tip', 'right nostril']

#['tail tip', 'back right shoulder', 'tail start', 'front left knee', 'front left foot', 'chin', 'back right knee', 'left eye', 'front right ankle', 'nosetip', 'front right shoulder', 'front left shoulder', 'back left foot', 'right eye', 'back right ankle', 'left ear', 'front right knee', 'front right foot', 'back left shoulder', 'neck', 'front left ankle', 'back right foot', 'back left knee', 'right ear', 'back left ankle']

# annotator in *.csv file
Scorers = ['AMT']  # who is labeling?

# Set this true if the data was sequentially labeled and if there is one file per folder (you can set the name of this file below, i.e. multibodypartsfilename)
# Otherwise there should be individual files per bodypart, i.e. in our demo case hand.csv, Finger1.csv etc.
# If true then those files will be generated from Results.txt
multibodypartsfile=False 
multibodypartsfilename="Results.csv"


# When importing the images and the labels in the csv/xls files should be in the same order!
# During labeling in Fiji one can thus (for occluded body parts) click in the origin of the image 
#(i.e. top left corner (close to 0,0)), these "false" labels will then be removed. To do so set the following variable:
#set this to 0 if no labels should be removed!

invisibleboundary=10 # If labels are closer to origin than this number they are set to NaN (not a number). Please adjust to your situation. Units in pixel.

imagetype=".png" # image type of extracted frames (do not change if you used our step1). 
# If you started from already extracted frames in a different format then change the format here (for step2 to 4).

########################################
# Step 3: Check labels / makes plots
########################################

colormap = 'hsv' #set color map, i.e. viridis, cool, hsv
scale = 1  # for plotting
msize=10   #size of labels
alphavalue =.9 #transparency of labels

########################################
# Step 4: Generate Training Files 
########################################

date = 'Oct2' #'May24' #'Aug2' #'May24' #'May03'#''May18'
scorer = 'AMT' #'camila'

# Userparameters for training set. Other parameters can be set in pose_cfg.yaml
Shuffles = range(3) #[1]  # Ids for shuffles, i.e. range(5) for 5 shuffles
TrainingFraction = [0.70]  # [0.95] # Fraction of labeled images used for training

# Which resnet to use
# (these are parameters reflected in the pose_cfg.yaml file)
resnet = 50


# trainingsiterations='1030000'

# For Evaluation/ Analyzing videos
# To evaluate model that was trained most set this to: "-1"
# To evaluate all models (training stages) set this to: "all"

snapshotindex = -1# "all" #
shuffleindex = 0

pcutoff=.1 # likelihood. RMSE will be reported for all pairs and pairs with larger likelihood than pcutoff (see paper). This cutoff will also be used in plots.
plotting=True #If true will plot train & test images including DeepLabCut labels next to human labels. Note that this will be plotted for all snapshots as indicated by snapshotindex

