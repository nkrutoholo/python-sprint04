import sqlite3
import sys

def help():
    print('Available commands:',
          '- help',
          '- connect [database]',
          '- close [database]',
          '- execute [database] "[SQL statement]"',
          '- show',
          '- exit',
          sep='\n')

def connect(db_file, connections):
    try:
        conn = sqlite3.connect(db_file)
        if db_file in connections:
            print(f'Already connected to database "{db_file}".')
        else:
            print(f'Created connection to database "{db_file}".')
            connections.update({db_file: conn})
    except sqlite3.Error as e:
        print(e)
    

def close(db_file, connections):
    try:
        if db_file not in connections:
            print(f'Cannot close connection to "{db_file}". Not connected.')
        else:
            connections[db_file].close()
            print(f'Closed connection to database "{db_file}".')
            connections.pop(db_file)
    except sqlite3.Error as e:
        print(e)

def execute(db_file, query, connections):
    try:
        if db_file not in connections:
            print(f'Cannot execute SQL statement. Not connected to "{db_file}".')
        else:
            conn = connections[db_file]
            cur = conn.cursor()
            cur.execute(query)
            print('Executed SQL statement.')
    except sqlite3.Error as e:
        print(e)

def show(connections):
    try:
        if len(connections) == 0:
            print('No connections.')
        else:
         print([k for k, v in connections.items()])
    except:
        print('No connections.')

def exit(connections):
    for k, v in connections.items():
        v.close()
        print(f'Closed connection to database "{k}"')
    sys.exit(0)


def handler(commands):
    ex_str = ' '.join(i for i in commands[2:]).split('"')
    commands = commands[0:2]
    commands.append(ex_str[1])
    return commands

if __name__ == '__main__':
    connections = {}
    while True:
        commands = input('Enter command: ').split(' ')
        if len(commands) > 2:
            commands = handler(commands)
        if len(commands) == 1 and commands[0] == 'help':
            help()
        elif len(commands) == 2 and commands[0] == 'connect':
            connect(commands[1], connections)
        elif len(commands) == 2 and commands[0] == 'close':
            close(commands[1], connections)
        elif len(commands) == 3 and commands[0] == 'execute':
            execute(commands[1], commands[2], connections)
        elif len(commands) == 1 and commands[0] == 'show':
            show(connections)
        elif len(commands) == 1 and commands[0] == 'exit':
            exit(connections)
        else:
            print('Invalid command. Try "help" to see available commands.')
