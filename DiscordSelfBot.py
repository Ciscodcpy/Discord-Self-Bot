import asyncio
from datetime import datetime
import subprocess
import sys
import os
import discord
intents = discord.Intents.default()
intents.message_content = True
intents.members = True


client = discord.Client(intents=intents)

async def send_dm_to_specific_members(token, user_ids, message):
    async with client:
        await client.start(token, bot=False)
        await client.wait_until_ready()

        for user_id in user_ids:
            user = await client.fetch_user(user_id)
            try:
                await user.send(message)
                print(f'Message sent to {user.name}')
            except discord.Forbidden:
                print(f'Could not send message to {user.name} - might be due to privacy settings or blocked user.')
            except Exception as e:
                print(f'An error occurred while sending message to {user.name}: {e}')

        await client.close()

async def schedule_message(token, user_ids, message, schedule_time):
    async with client:
        await client.start(token, bot=False)
        await client.wait_until_ready()

        current_time = datetime.now()
        time_difference = schedule_time - current_time

        if time_difference.total_seconds() > 0:
            await asyncio.sleep(time_difference.total_seconds())

            for user_id in user_ids:
                user = await client.fetch_user(user_id)
                try:
                    await user.send(message)
                    print(f'Message sent to {user.name}')
                except discord.Forbidden:
                    print(f'Could not send message to {user.name} - might be due to privacy settings or blocked user.')
                except Exception as e:
                    print(f'An error occurred while sending message to {user.name}: {e}')

        await client.close()

async def read_and_respond_to_messages(token, channel_id, keyword, response):
    async with client:
        await client.start(token, bot=False)
        await client.wait_until_ready()

        channel = client.get_channel(channel_id)

        @client.event
        async def on_message(message):
            if message.content.lower().find(keyword.lower()) != -1:
                await message.channel.send(response)

        await client.close()

async def mass_invite_to_server(token, server_invite, user_ids):
    async with client:
        await client.start(token, bot=False)
        await client.wait_until_ready()

        for user_id in user_ids:
            user = await client.fetch_user(user_id)
            try:
                await user.send(server_invite)
                print(f'Invite sent to {user.name}')
            except discord.Forbidden:
                print(f'Could not send invite to {user.name} - might be due to privacy settings or blocked user.')
            except Exception as e:
                print(f'An error occurred while sending invite to {user.name}: {e}')

        await client.close()

async def send_dm_with_template(token, user_ids, template, replacements):
    async with client:
        await client.start(token, bot=False)
        await client.wait_until_ready()

        for user_id in user_ids:
            user = await client.fetch_user(user_id)
            message = template.format(**replacements)
            try:
                await user.send(message)
                print(f'Message sent to {user.name}')
            except discord.Forbidden:
                print(f'Could not send message to {user.name} - might be due to privacy settings or blocked user.')
            except Exception as e:
                print(f'An error occurred while sending message to {user.name}: {e}')

        await client.close()
from colorama import Fore, Style, init
init()


kuromi_ascii = r"""
------------------------------------------------------------------------------------------------------------------------
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠛⠛⠛⠒⠒⠶⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀                                                                      
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⠤⠴⠶⠒⠒⠲⠶⠦⢤⣼⡃⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⣴⠛⠻⡆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⠀⠀⢀⣠⠶⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢶⣄⠀⠀⠀⠀⠀⠀⠀⣠⠿⢦⡴⠇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⠟⠉⠈⠉⠻⣦⠟⠁⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣆⠀⠀⠀⢠⡾⠁⠀⠀⠀⠀⠀⠀
⠀⢀⣀⠀⢀⣠⠶⠋⠁⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⠤⠴⠋⠀⠀⠀⠀⠀⠀⠀  
⢰⡏⠈⢳⣟⠁⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⢸⡟⠉⣿⣿⣧⣨⠇⢀⣀⣀⡀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀                   You did it! You made it this far!
⠀⠛⠚⠋⠉⠳⢦⡀⠀⠀⠀⠀⠀⡾⠀⠀⠀⠀⠀⠀⠀⢀⠙⠿⢿⣿⣿⣯⠞⠋⠁⠈⠉⠳⢦⡄⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⢀                   
⠀⠀⠀⠀⠀⠀⠀⠙⢷⣄⠀⠀⢀⡇⠀⠀⠀⠀⠀⣤⠞⠉⠉⠙⠛⠛⠋⠀⠀⠀⠀⠀⠀⢠⡀⠙⣦⠀⣸⠃⠀⢰⠋⠉⠳⠋⠉⠙⡆⠀    
⠀⠀⠀⠀⢀⠤⠤⣄⡀⠈⠛⠚⠋⣷⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡶⢛⣿⣁⠀⢸⣦⡟⠀⠀⠸⣆⠀⠀⠀⠀⡼⠃⠀                                
⠀⠀⠀⠀⡏⠀⠀⠀⠵⠒⠲⢤⠀⠹⡆⠀⠀⢸⠇⢀⣤⡤⠤⣄⠀⠀⢠⠄⣄⠀⠀⢰⣿⠿⣿⣀⣸⡟⠀⠀⠀⠀⠈⠓⢤⡴⠊⠀⠀⠀                     Discord: Chickenmaaster
⠀⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀⢨⠇⠀⠙⢦⡀⢸⡄⠀⣻⣴⣶⡶⠀⠀⣬⠭⠅⡆⠀⠈⣴⠟⠉⠉⢻⣦⡶⢲⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀                      Github: Ciscodcpy
⠀⠀⠀⠀⠀⠳⡄⠀⣀⡤⠖⠉⠀⠀⠀⠀⠙⢦⣿⣤⣛⣿⠿⢧⣄⠀⠈⠒⣒⣡⡤⢾⡇⠀⢠⣴⣟⣯⡛⠛⠃⠀⠀⠀⢠⡏⠉⠳⠖⠲                     
⠀⠀⠀⣀⣀⡀⠹⠋⠁⠀⠀⠀⠀⠀⠀⠀⢀⣀⣈⣽⠿⣇⠀⠀⠹⡗⠚⣋⡭⠤⠤⣤⣷⡀⠀⢻⢿⣄⡿⠀⠀⠀⠀⠀⠀⠳⡀⠀⢀⡠         
⡴⠚⠻⠇⠀⣹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣅⣿⠋⢉⣛⣿⠀⠀⢹⠟⠉⠀⠀⠀⠀⠈⠳⣶⠟⠀⠀⠀⡰⠒⠓⢆⠀⠀⠀⠘⠒⠉This software/tool is designed strictly for educational purposes only.
⠹⢄⣀⠀⡰⠃⠀⠀⠀⠀⠀⠀⠀⢸⡗⠒⠲⣶⠀⠀⠺⣥⣽⣦⡴⠟⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⢰⡇⠀⠀⢨⡧⣄⡀⠀It serves as a learning aid to help users understand programming concepts
⠀⠀⠈⠉⠁⠀⠀⣀⣀⡞⠉⠙⡆⠀⣧⣴⣄⠹⣦⣀⣀⣸⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡾⠃⠀⠀⠀⠘⡇⠀⠀⠀⠀⠀⠙⡆automation, or system behaviors in a controlled and ethical environment.
⠀⠀⠀⠀⠀⢠⠏⠁⠈⠀⠀⠀⡀⠀⠈⠀⠙⠳⠦⣬⣭⣽⣿⣆⠀⠀⠀⠀⠀⣤⠀⠀⣹⡇⠀⠀⠀⠀⠀⣇⣀⣀⣀⣀⣀⡼⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢧⣄⣀⣀⠀⢠⠇⠀⠀⠀⠀⠀⠀⠀⠀⡟⠀⠁⠀⠀⠀⠀⣰⠏⠀⠀⠻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⠛⣉⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢦⣀⣀⣤⠞⠛⠶⠤⠴⠚⠁⠀⠀⠀⠀
                                                        _  __    _    _    ____     ______    __  __    _____  
                                                        | |/ /  | |  | |  |  _ \   |   _  |  |  \/  |  |_   _| 
                                                        | ' /   | |  | |  | |_) |  |  | | |  | \  / |    | |   
                                                        |  <    | |  | |  |  _ <   |  | | |  | |\/| |    | |   
                                                        | . \   | |__| |  | | \ \  |  |_| |  | |  | |   _| |_  
                                                        |_|\_\   \____/   |_|  \_\ |______|  |_|  |_|  |_____| 

------------------------------------------------------------------------------------------------------------------------
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
print(Fore.MAGENTA + kuromi_ascii + Style.RESET_ALL)





init(autoreset=True)

def main():
    while True:
        print(Fore.MAGENTA + "\nChoose an option:" + Style.RESET_ALL)
        print(Fore.MAGENTA + "---------------------------------------------" + Style.RESET_ALL)
        print(Fore.MAGENTA + "1. Send DM to specific members" + Style.RESET_ALL)
        print(Fore.MAGENTA + "2. Schedule a message" + Style.RESET_ALL)
        print(Fore.MAGENTA + "3. Read and respond to messages" + Style.RESET_ALL)
        print(Fore.MAGENTA + "4. Mass invite to server" + Style.RESET_ALL)
        print(Fore.MAGENTA + "5. Send DM with template" + Style.RESET_ALL)
        print(Fore.MAGENTA + "6. Exit" + Style.RESET_ALL)
        print(Fore.MAGENTA + "---------------------------------------------" + Style.RESET_ALL)


        choice = input(Fore.MAGENTA + "Enter your choice: " + Style.RESET_ALL)

        if choice == '1':
            token = input(Fore.MAGENTA + 'Enter your Discord account token: ' + Style.RESET_ALL)
            user_ids = input(Fore.MAGENTA + 'Enter a comma-separated list of user IDs: ' + Style.RESET_ALL).split(',')
            user_ids = [uid.strip() for uid in user_ids]
            message = input(Fore.MAGENTA + 'Enter the message you want to send: ' + Style.RESET_ALL)
            asyncio.run(send_dm_to_specific_members(token, user_ids, message))

        elif choice == '2':
            token = input(Fore.MAGENTA + 'Enter your Discord account token: ' + Style.RESET_ALL)
            user_ids = input(Fore.MAGENTA + 'Enter a comma-separated list of user IDs: ' + Style.RESET_ALL).split(',')
            user_ids = [uid.strip() for uid in user_ids]
            message = input(Fore.MAGENTA + 'Enter the message you want to send: ' + Style.RESET_ALL)
            schedule_time_str = input(Fore.MAGENTA + 'Enter the schedule time (YYYY-MM-DD HH:MM:SS): ' + Style.RESET_ALL)
            schedule_time = datetime.strptime(schedule_time_str, '%Y-%m-%d %H:%M:%S')
            asyncio.run(schedule_message(token, user_ids, message, schedule_time))

        elif choice == '3':
            token = input(Fore.MAGENTA + 'Enter your Discord account token: ' + Style.RESET_ALL)
            channel_id = int(input(Fore.MAGENTA + 'Enter the channel ID: ' + Style.RESET_ALL))
            keyword = input(Fore.MAGENTA + 'Enter the keyword to respond to: ' + Style.RESET_ALL)
            response = input(Fore.MAGENTA + 'Enter the response message: ' + Style.RESET_ALL)
            asyncio.run(read_and_respond_to_messages(token, channel_id, keyword, response))

        elif choice == '4':
            token = input(Fore.MAGENTA + 'Enter your Discord account token: ' + Style.RESET_ALL)
            server_invite = input(Fore.MAGENTA + 'Enter the server invite link: ' + Style.RESET_ALL)
            user_ids = input(Fore.MAGENTA + 'Enter a comma-separated list of user IDs: ' + Style.RESET_ALL).split(',')
            user_ids = [uid.strip() for uid in user_ids]
            asyncio.run(mass_invite_to_server(token, server_invite, user_ids))

        elif choice == '5':
            token = input(Fore.MAGENTA + 'Enter your Discord account token: ' + Style.RESET_ALL)
            user_ids = input(Fore.MAGENTA + 'Enter a comma-separated list of user IDs: ' + Style.RESET_ALL).split(',')
            user_ids = [uid.strip() for uid in user_ids]
            template = input(Fore.MAGENTA + 'Enter the message template: ' + Style.RESET_ALL)
            replacements_input = input(Fore.MAGENTA + 'Enter the replacements (key=value, separated by commas): ' + Style.RESET_ALL)
            replacements = dict(item.split('=') for item in replacements_input.split(','))
            asyncio.run(send_dm_with_template(token, user_ids, template, replacements))

        elif choice == '6':
            break

        else:
            print(Fore.MAGENTA + "Invalid choice. Please try again." + Style.RESET_ALL)


if __name__ == '__main__':
    if '--no-restart' not in sys.argv:
        script_path = os.path.abspath(sys.argv[0])
        command = f'start cmd /k python "{script_path}" --no-restart'
        subprocess.Popen(command, shell=True)
        sys.exit()  # Prevent loop
    else:
        main()