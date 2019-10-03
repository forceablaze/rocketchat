
import getpass
from rocketchat.api import API

RC = API("http://10.156.2.89:8008/rocketchat/ipf3")

username = 'sibo.wang'
password = getpass.getpass("Please input password:")
data = RC.login(username, password)

channelInfo = RC.channels_info('random')
userInfo = RC.users_info()
userId = userInfo['user']['_id']
channelId = channelInfo['channel']['_id']

userList = RC.users_list()
totalCount = userList['total']

offset = 0
while offset < totalCount:
    userList = RC.users_list(offset=offset)
    offset += userList['count']
    print(userList['offset'])
    print(userList['count'])

    for user in userList['users']:
        print(user['_id'], user['username'])
        print(RC.channels_invite(channelId, user['_id'])['success'])
