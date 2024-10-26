# def execute_command(command: str):
#     if command == 'ls':
#         print('$ listing files')
#     elif command == 'cd':
#         print('$ changing directory')
#     else:
#         print('$ command not implemented')
#     print('...Rest of the code')


# def execute_command(command: str):
#     match command:
#         case 'ls':
#             print('listing files')
#         case 'cd':
#             print('$ changing directory')
#         case _: # Não obrigatorio
#             print('$ command not implemented')

# execute_command('pwd')

# def execute_command(command: str):
#     match command.split(', '):
#         case ['ls', *directories, '--force']:
#             for directory in directories:
#                 print('$$ listing directory FORCED', directory)

#         case['ls', *directories]:
#             for directory in directories:
#                 print('$ listing directory from', directory)

#         case ['cd', path]:
#             print('$ changing directory to', path)
#         case _:
#             print('command not exists')

# execute_command('ls, /davi, /projeto, --force')
# execute_command('ls, /davi, /projeto')
# execute_command('abc')


# def execute_command(command: str):
#     match command.split(', '):
#         case['ls' | 'list', *directories]:
#             for directory in directories:
#                 print('$ listing directory from', directory)
#         case ['cd', path]:
#             print('$ changing directory to', path)
#         case _:
#             print('command not implemented')
#     print('...rest of the code...')
        
# execute_command('ls, / davi, /sla, /isso')
# execute_command('list, / davi, /sla, /isso')


# def execute_command(command: str):
#     match command.split(', '):
#         case ['ls' | 'list', *directories] if len(directories) > 1:
#             for directory in directories:
#                 print('$ listing ALL directory from', directory)

#         case ['ls' | 'list', *directories] if len(directories) < 1:
#             print('$ listing ALL directory from', directories[0])

#         case ['cd', path]:
#             print('$ changing directory to', path)
#         case _:
#             print('command not implemented')
#     print('...rest of the code...')
        
# execute_command('ls, / davi, /sla, /isso')
# execute_command('list, / davi, /sla, /isso')


# def execute_command(command: str):
#     match command.split(', '):
#         case ['ls' | 'list' as the_command, *directories] as the_list if len(directories) > 1:
#             for directory in directories:
#                 print('$ listing ALL directory from', directory)
#             print(f'{the_command}, {the_list}')
#         case ['ls' | 'list', *directories] if len(directories) < 1:
#             print('$ listing ALL directory from', directories[0])

#         case ['cd', path]:
#             print('$ changing directory to', path)
#         case _:
#             print('command not implemented')
#     print('...rest of the code...')
        
# execute_command('ls, / davi, /sla, /isso')
# execute_command('list, / davi, /sla, /isso')

# def execute_command(command: str):
#     match command:
#         case {'command': 'ls', 'directories': [_, *_]}:
#             print('DEU MATCH')
#             for directory in command['directories']:
#                 print('$ listing directory from', directory)
#         case ['cd', path]:
#             print('$ changing directory to', path)
#         case _:
#             print('command not implemented')
#     print('...rest of the code...')

from dataclasses import dataclass

@dataclass
class Command:
    command: str
    directories: list[str]

def execute_command(command: Command):
    match command:
        case Command(command='ls', directories=[_, *_]):
            for directory in command.directories:
                print('$ listing ALL directory from', directory)
        
        case Command(command='cd', directories=[_, *_]):
            for directory in command.directories:
                print('$ changing to', directory)
        
        case _:
            print('command not implemented')
    print('rest of the code...')

command_1 = Command('ls', ['/users'])
command_2 = Command('cd', ['/users'])

execute_command(command_1)
execute_command(command_2)
