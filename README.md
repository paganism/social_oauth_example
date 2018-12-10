# This web app is example of oauth usage. Here is used login via VK

To see how it works you should go [here](http://yuriybelov.pythonanywhere.com/)

# How to run 
* Clone or download repo, install all requirements to virtualenv.
* Repo already has sqlite DB, so you don't need apply migrations. 
* Then you have to create application on [VK](https://vk.com/dev) for web platform and set your website address (http://example.com) and your domain(example.com). 
* If you don't have your own domain it is possible to run app on localhost. For it you should login to localhost as root, enter to virtualenv and run command as root:

```
# python3 manage.py runserver 127.0.0.1:80
```
Also you need to modify /etc/hosts file. You should add the following line:
```
127.0.0.1 your-domain-which-you-set-up-for-vk-app (example.com)
```
* After that you can open your favorite browser and go to your-domain-which-you-set-up-for-vk-app (example.com)
* If you have hosting provider, just deploy application according provider instructions.

# Project Goals
The code is written for educational purposes.