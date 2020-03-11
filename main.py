from toggl.TogglPy import Toggl
import configparser
import time

# Get config
config = configparser.ConfigParser()
config.sections()
config.read('config.ini')

# Get Toggl config
toggl = Toggl()

TogglConfig = config['Toggl']

if TogglConfig['auth_token']:
    print('Using Toggl token for authentication')
    toggl.setAPIKey(TogglConfig['user_token'])
elif TogglConfig['auth_email']:
    print('Using Toggl email and password for authentication')
    toggl.setAuthCredentials(TogglConfig['user_email'], TogglConfig['user_password'])
else:
    raise Exception('Please configure your Toggl authentication.')


# Every 5 min, check the timer
# If the timer is still the same value as last, don't change it
# If it is different, change the display to the opposite view
# and change the status value

working = False
# display not working

while True:

    currentEntry = toggl.request('https://www.toggl.com/api/v8/time_entries/current')

    if currentEntry["data"] == None and working == True:
        working = False
        print("Not Working")
    elif currentEntry["data"] != None and working == False:
        working = True
        print("Working")
    time.sleep(5)
    # time.sleep(5 * 60)
