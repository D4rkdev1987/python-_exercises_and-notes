from fbchat import Client
from fbchat.models import Message, MessageReaction

username = "marineepo@gmail.com"
password = "Buckeyefan1987$"

client = Client(username, password)

users = client.fetchThreadList()
print(users)

detailed_users = [ list(client.fetchThreadInfo(user.uid).values())[0] for user in users]

sorted_detailed_users = sorted(detailed_users, key=lambda u: u.message_count, reverse=True)
best_friend = sorted_detailed_users[0]

print("Best Friend:", best_friend.name, "with a message count of", best_friend.message_count)

client.send(Message(
    text=f"Congratulations {best_friend.name}, you are my best friend with {best_friend.message_count} messages!"
    ),
    thread_id=best_friend.uid)

all_users = client.fetchAllUsers()

print("You talked with a total of", (all_users), "users!")

client.logout()




