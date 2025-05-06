![TermaChat](docs/title.png)

A terminal based peer-to-peer chat application, designed for local as well as global chat through either 1-1 or group chats.

## Features

- Admin control over server configurations
- Chat rooms for two or multiple users
- Nicknames for users
- Encrypted connection between client and server messages
- Client authentication using password
- Client authentication using MFA
- Chat history
- In-chat command execution (commands start with '/')

# How it works

- The admin starts up a server locally on their machine.
- Admin registers users and sends them password for their account
- The clients connect to the server using IP and PORT and their password
- Client chooses a chatroom to connect and start chatting  

![how_it_works](/docs/how_it_works.png)

> [!NOTE]
> The "How it works" flow is entirely hypothetical at this stage. It will be changed as time and it's development progresses.

> [!WARNING]
> There may be security risks involved in the early stages of development and may put you at risk, unless security fixes are introduced for a specific scenario.