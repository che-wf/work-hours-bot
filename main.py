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
SettingsConfig = config['Settings']

if TogglConfig['auth_token']:
    print('Using Toggl token for authentication')
    toggl.setAPIKey(TogglConfig['user_token'])
elif TogglConfig['auth_email']:
    print('Using Toggl email and password for authentication')
    toggl.setAuthCredentials(TogglConfig['user_email'], TogglConfig['user_password'])
else:
    raise Exception('Please configure your Toggl authentication.')



# Timer
working = False

while True:

    currentEntry = toggl.request('https://www.toggl.com/api/v8/time_entries/current')

    if currentEntry["data"] == None and working == True:
        working = False
        print("Not Working")
    elif currentEntry["data"] != None and working == False:
        working = True
        print("Working")
    time.sleep(int(SettingsConfig['interval']))
