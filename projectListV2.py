#this is project list V2. This was inspired from Day's till SAT which is also to be know as v1. All v1 can do is tell you how many days till the SAT there are (of today there are 36)
#   This script however will contain multiple projects with multiple due dates, the ability to create new projects, and a way of keeping track of progress in the form of snapchat streaks.
#       This functionaity is made with with using the shelve module to keep track of dates using the time module (this is done by pluging in the date of the due date into the Time_struct module and then converting that into seconds. These seconds are subtracted my the the current date of acsess. this difference is divided by 38000 (or 24*60*60) to get how many days till a project is due)
#           and the shelve module to keep track of the lists of of projects that are present. (in the form [['project name',dueDateInSeconds,workStreak],_other project_])

import time, shelve

projectListV2Data = shelve.open('projectListV2Data')
data = projectListV2Data['projectData']

projectList = data

currentTime = time.time()

def TimeTill(projectListValue):
    '''
    input current time of project intereated over (the second term in a nested list ie projects[i][1])
    output day difference between today and project due date
        this is done by subtracting the seconds till the due date by the current time by seconds and then dividing by 24*60*60

    '''
    return int(((projectListValue[1]-currentTime))/86400)

def snapchatStreaks(projectListStreakValue):        #to be used with the third value in a nested list {projectList[i][2]}
    '''
    input streak value of a project List
    output your streak and question whether or not to add to your streak
        This will output the user's current streak and ask a question. if the user replies YES, a +1 will be added
            if no or anything else is added(like just hiting new line) the streak will be set to 0
                emoji functionality planned
    '''
    streak = projectListStreakValue
    print('test, your snapstreak is,',projectListStreakValue)

    print('have you worked on the project?(keep tab open while you are working(type "yes" exactly))')
    addToStreak = input()
    if addToStreak == 'yes':       #ADD A .UPERCASE OR SOMETHING CAUSE THIS IS DISGUSTING
        streak += 1
        print('You have a streak of',streak)
    elif addToStreak != 'yes':
        print('streak of',projectListStreakValue,'lost')
        print('streak now',0,)
        streak = 0
    return streak



def questionaire(baseProjectList):
    '''
    input baseProjectList
    output TimeTill function, and ability to add to streaks
        this will say how many days till a project is due and then ask if the user has worked on it (snapchat streaks)
    '''

    print(TimeTill(baseProjectList),'days left till,',baseProjectList[0],'is due')
    #snapchatStreaks(baseProjectList[2])
    streak = snapchatStreaks(baseProjectList[2])
    return streak


for i in range(len(projectList)):
    projectList[i][2] = questionaire(projectList[i])


projectListV2Data['projectData'] = projectList
projectListV2Data.close()

#TODO make a shelve file i can call/edti/save projectList toself.
	#doing on feb 23 Fri 23 Feb 2018 07:19:52 PM PST <--cool	DONE!will
#TODO allow the User to add new projects from within the script     using ffnfkllnaslkfnl
#TODO make days SAT into a function that takes seconds and returns the due date.    done
#debating wheather or not to delete projects once they go negative
    #I think ill do it, so if project sec is less than current sec del
    #ill focus on this later, first i need to...... Editior! i need to work on the editor to allow it to
        #make, view, and del projects. i see no reason to not give it the ability to edit streaks
