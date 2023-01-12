If you want the instructions on how to run the original program find them here: https://github.com/south1907/addmember-telegram

What my fork does is exactly the same as the original program with a few upgrades.
When we go to add users on our group list, we often get the error "User cannot be added due to privacy settings". 
Obviously no matter how many times we try to add such a user it will fail. I believe that a lot of
these failures will trigger the spam filter, and in the best case scenario, they waste time and resources.
So I have changed add_members.py to save the user_id of a user when we encounter that error in
bad_user.json. Then if you look at delete_json_objects_all4_withsysargs.py you will see that by running
that program, we go through the json object and delete any instances of these "bad users" we find. 
The program delete_json_objects_all4_withsysargs.py takes one argument, the name of the group. 
Currently you will have to manually edit in all your telegram phone numbers. Please don't use mine.
Thanks!