# FlaskChat
### Proposal for a different way to handle group chats.

This chat room, allows for an user.

- Let's call user_a

To select as many online users as they want to talk to.

- Let's call user_b and user_c.

In order to talk to both of them.

###### Without creating a communication channel for user_b and user_c.

##### On selection of multiple users to talk to
###### Three things **will** happen.
- user_b and user_c will get notified
- messages sent by user_a will now be delivered to user_b and user_c.
- messages sent by either user_b or user_c will now be delivered to user_a

###### What **will not** happen.
- messages sent by user_b will not be delivered to user_c
- messages sent by user_c will not be delivered to user_b

### Requirements
- Python 3.9 or higher
- pip3 or higher
- pipenv installed
  - to install run:
  ```
  pip install pipenv
  ```
  [pipenv info](https://pypi.org/project/pipenv/)

## How to Use
  ```
  git clone https://github.com/santiagoziel/FlaskChat.git
  cd FlaskChat
  pipenv shell
  pipenv install
  python3 run.py
  ```
**Navigate to** http://127.0.0.1:5000 and go nuts.
### TODO
- [ ] improve general look
- [ ] improve online users look
- [ ] display differentiate from diff users messages
- [ ] make user system more robust
