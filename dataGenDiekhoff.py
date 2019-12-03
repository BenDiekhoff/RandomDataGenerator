import generate as gen
import re
import json

numstring = input("Enter the number of users you want to generate: ")
num = int(numstring)

ls = gen.username(num)

count = 1
with open('data.json', 'w+') as file:
    data = []

    for username in ls:
        firstEmail = username[0]
        secondEmail = re.findall ('[A-Z][^A-Z]*', username)
        dom = gen.emailDomain()
        email = str(firstEmail) + "." + str(secondEmail[0]) + str(dom)
        fName = gen.firstName()
        lName = gen.lastName()
        password = gen.password()
        date = gen.createTime()
        createTime = date.date()
        lastUpdate = gen.lastUpdate(date)
        

        data.append({
            'user_id': count,
            'email': email,
            'username': username,
            'first_name': fName,
            'last_name': lName,
            'password': password,
            'create_time': str(createTime),
            'last_update': str(lastUpdate)
             })
        
        count += 1
    json.dump(data,file,indent=4)
    


