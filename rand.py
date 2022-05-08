import random


def Help():
    space = 10
    for command in Commands:
        print(f'{command}{(space-len(command))*" "}{Commands[command]["des"]}')

def Ex1():
    print('topic: 1 10')
    print(f'random: {random.randint(int(topic[0]),int(topic[1]))}')

def Ex2():
    print('topic: dog cat mouse')
    print('random: ' + random.choice(['dog','cat','mouse']))

Commands = {
    'help':{
        'des':'danh sách các lệnh',
        'main':Help
    },
    'exam1':{
        'des':'how to random a number?',
        'main':Ex1
    },
    'exam2':{
        'des':'how to random a list topic?',
        'main':Ex2
    }
}
print(type("a"))
topic = str(input("topic [help]: ")).split(" ")
if len(topic) > 2:
    print('random: ' + random.choice(topic))
elif len(topic) == 2 and type(topic[0]) != "<type 'str'>":
    print(f'random: {random.randint(int(topic[0]),int(topic[1]))}')
elif len(topic) == 1 and topic[0] in Commands:
    print('------------------------------------')
    Commands[topic[0]]['main']()