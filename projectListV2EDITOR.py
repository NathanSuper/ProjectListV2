#This is the editor for the shelve file relating to projectListV2.py

import shelve,time

projectListV2Data = shelve.open('projectListV2Data')
data = projectListV2Data['projectData']

def timeTillDateInSeconds():
    '''
    Input    a day a month a year
    Output    seconds since unix epoc using given variables

    This is a function that will plug in the given variables of day month and year into the time_struct and convert into seconds since epoc
    This is to be used in subtraction from current time divided by 60*60*24 to get days aproximate days till something is due
    '''
    print('year?,ex 1997')
    year = int(input())
    print('month? (1-12)')
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    for i in range(len(months)):
           print('   '*i,months[i],i+1)
    month = int(input())
    print('day?')
    day = int(input())

    #local variable time
    a = time.time()
    A = time.gmtime(a)
    AList = list(A)

    AList[0] = year
    AList[1] = month
    AList[2] = day

    ATimeInSeconds = time.mktime(time.struct_time(AList))

    return ATimeInSeconds

def add(PROJECTLIST):    #this is usually refered to as 'data'
    '''
    input due date & project name
    output "project" -- a list with a name, seconds since epoc and streaks
    '''
    print('What is this projects name? ex: daily tooth brushing, reading, prayer')
    name = str(input())
    print('when will the project be completed(and there by deleted)')
    dueDate = timeTillDateInSeconds()
    project = []
    project.append(name)
    project.append(dueDate)
    project.append(0)
    PROJECTLIST.append(project)

    print('Confirm? (type "no" to cancel)')
    print(PROJECTLIST[-1])
    confirmation = str(input())
    if confirmation == 'no':
        PROJECTLIST.remove(PROJECTLIST[-1])
        return PROJECTLIST

    return PROJECTLIST


badBooleen = 1

print('input help for options')

#KAR = timeTillDateInSeconds()    #the hell is wrong with me
#print(KAR)
while badBooleen == True:
    inputCommand = str(input())
    if inputCommand == 'end':
        badBooleen = 0
    if inputCommand == 'help':
        print('This is the shelve file editor for projectListV2.py, which is nathans attempt to add streaks to small tasks or goals.')
        print('its mainly a side project.')
        print('Commands:')
        print('help -- this is help')
        print('end -- this takes you out of the loop back into the terminal')
        print('add -- this requires 4 prompted inputs,the project name, the day, the month and the year')
        print('del -- prints all project names, streaks, and days till due date(even if negative)')
        print('edit -- prints project and asks for you ')
        print('list -- displays all projects in a nice table(i hope its nice anyway)')
    if inputCommand == 'add':
        data = add(data)
    if inputCommand == 'del':
        for i in range(len(data)):
            print('[',i,']',data[i])
        print('which to delete?')
        hold = input()
        if type(hold) == int and type <= len(data):
            print('delete',data[hold],'?')
            if input() == 'yes':
                data.remove(woah[hold])
    if inputCommand == 'list':
        for i in range(len(data)):
            print(data[i])
    #if inputCommand ==


print('----------------------------------')
print(data)

#TODO list
#gain ability to make new project due dates by filling in time_struct and converting to seconds





projectListV2Data['projectData'] = data
projectListV2Data.close()
