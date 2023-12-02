# Secret Santa Bot

This is a secret santa discord bot code. It uses the **discord-py-interactions** library. It consists of 3 basic commands being **enroll_in_secret_santa**, **remove_enrolled**, and **process_ss** and the algorithm that distributes the enrolled members to the corresponding gift receivers. The output goes to the members enrolled DMs.


## enroll_in_secret_santa

This command receives one input, **user**, and stores the information in an **enrolled user list**. You have to enroll everyone **one by one**.

## remove_enrolled

This command has two options, to **clear the enrolled user list** or to simply **remove a single user** from said list in case you make a mistake while enrolling everyone.

## process_ss

This command runs the secret santa algorithm and sends **DM**s to all enrolled members with the corresponding member to gift.
> It shuffles the list of the receiving users and then runs by a few conditions to make sure there are all checked otherwise it will shuffle the list again until all conditions are met.
