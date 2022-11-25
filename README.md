# This is readme file for my student project on python.

**Installation:**

* Of course I tested this guide only on Linux OS, because sane person can't use proprietary programming products. Also I assume, that you already have installed Python 3.10.

* You should run following command in your terminal for downloading project files:
    $ git clone https://github.com/Nick18899/PythonProject_mipt

* You should install nvm package manager by following guide written on this page $ https://github.com/nvm-sh/nvm/blob/master/README.md

* After installation write following commands in your terminal:
    $ nvm install 16

    $ nvm use 16

* After that, you have to install npm package manager. I have Arch-based Linux, so I do it via this command:
    $ yay -S npm
    or by
    $ pacman -S npm

* You have successfully installed package manager. Now you should install dependencies.
    * Run following command in $ /home/alexcorabl/PythonProject_mipt/src/front/src/
        $ npm install
    * Run following command in $ /home/alexcorabl/PythonProject_mipt/src/server/src/
        $ pip install

* Congratulations, now you can run project!



**Running:**

* Run following command in $ /home/alexcorabl/PythonProject_mipt/src/server/src/
    $ flask app.py
    * WARNING: it will run DEVELOPMENT, not production, version of server

* Run following command in $  /home/alexcorabl/PythonProject_mipt/src/front/src/
    $ npm run build

* These commands will run server and front on your localhost. Server will be deployed on 5050 port, front on 8080 port.
