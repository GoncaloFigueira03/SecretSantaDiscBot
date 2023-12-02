import random
from interactions import slash_command, slash_option, SlashContext, Client, Intents, listen, OptionType, User

DISCORD_TOKEN = 'Your bot token goes here'
GUILD_ID =  43798573495734 # Your guild ID goes here (replace de random number) if you want to restrict the bot to a specific server. If you want to use it in all servers, just remove the scopes=[GUILD_ID] from the slash commands

bot = Client(intents=Intents.DEFAULT)
userList = []

# ----- Secret Santa Algorithm ----- #
def secret_santa(names):
    # Copy the list of names
    gifters = names.copy()
    receivers = names.copy()

    breakCheck = True

    while True:
        breakCheck = True
        # Shuffle the receivers list
        random.shuffle(receivers)

        # Ensure no one is assigned to themselves // if you want you can add more conditions inside de for loop
        for i in range(len(gifters)):
            if gifters[i] == receivers[i]:
                breakCheck = False
            
            # just remove de comment below and switch de names to people you want to avoid to be assigned to each other
            # if str(gifters[i]) == "person1" and str(receivers[i]) == "person2":
            #     breakCheck = False

            # if str(gifters[i]) == "person2" and str(receivers[i]) == "person1":
            #     breakCheck = False
        
        if breakCheck == True:
            break

    # Return receivers
    return receivers


# ----- Events ----- #
@listen()
async def on_startup():
    print("Bot is ready!")


# ----- Slash Commands ----- #
# --- Adds to the Enroll List --- #
@slash_command(name="enroll_in_secret_santa", description="Enrolls members in the secret santa event.", scopes=[GUILD_ID])
@slash_option(name="users", description="He should be here", opt_type=OptionType.USER)
async def enroll_users(ctx: SlashContext, users: User):
    userList.append(users)
    await ctx.send(f'{users.mention} was enrolled in Secret Santa')
    print(f'{users} was appended to list')

# --- Removes from the Enroll List --- #
@slash_command(name='remove_enrolled', description="Oops he shouldn't have been enrolled...", scopes=[GUILD_ID])
@slash_option(name="users", description="He shouldn't be here", opt_type=OptionType.USER)
async def remove_enrolled(ctx: SlashContext, users: User):
    userList.remove(users)
    await ctx.send(f'{users.mention} was removed from the enrolled list.')
    print(f'{users} removed from userList')

@slash_option(name="remove_all", description="Clears the enrolled list.")
async def empty_enrolled(ctx: SlashContext, users: User):
    userList.clear()
    await ctx.send("The enrolled list was cleared.") 
    print("Enrolled list is now empty")

# --- Processes the Secret Santa --- #
@slash_command(name="process_ss", description="DM all enrolled users with the corresponding person to gift.", scopes=[GUILD_ID])
async def ungabunga(ctx: SlashContext):
    personGifting = secret_santa(userList)
    i = 0
    for person in userList:
        await person.send(f"Your secret santa is {personGifting[i]}. Good luck on finding a good gift!")
        print(f'{person} was messaged with corresponding person to gift')
        i+=1

    await ctx.send(f'All users enrolled were messaged!')

# ----- Start Bot ----- #
bot.start(DISCORD_TOKEN)