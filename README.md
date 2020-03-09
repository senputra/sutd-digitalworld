# SUTD Digital World 1D Project



## Telegram Bot Documentation

### Prerequisite:

1. https://python-telegram-bot.org/https://python-telegram-bot.org/  *learn how to manipulate telegram bot with python*
2. https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks *Learn how to use webhook on heroku*

### API

1. `/available` : Bot to return the available machines. *parameters is yet to be decided*
2. `/plan`: Bot to return the suggested timing to do laundry on that date. *the parameter is yet to be decided*
3. `/report`: Mock a process to report any broken machine to the housing departments
   1. for starters: can try sending an email

### End 2 End(e2e) Test cases

1. User wants to wash/dry clothes:
   1. Check phone app. (**Branch: Telegram user story**)
   2. Go laundry
   3. Put laundries in and pay **(Branch: if machine is full)**
   4. press a button to indicate which machine he uses **(Branch: Pressed wrongly)**
2. User checks availability from Telegram:
   1. open phone
   2. talk with bot. send command `/available`
   3. bot replies with data
3. User presses the wrong button:
   1. Cancel by holding the button of a red square (for 1s)

