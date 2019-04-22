# Welcome to Raul's very own Certificate Automator 3000!

## First things first... _installation_

### For Old-Timers
That is, for people who are acquainted with Python and/or already have it installed.
To run [certificate_generator.py](https://github.com/ralbso/python/blob/master/certificate_automator/certificate_generator.py)
you must install all packages listed within that script. That is, you should run
`pip install PyPDF2==1.26.0` and `pip install reportlab==3.5.19` in your Command Prompt,
if you don't have these packages. I recommend you create a new environment, as I do
in the installation scripts found in this repository.

### For Newbies
#### Windows
Please run [install.bat](https://github.com/ralbso/python/blob/master/certificate_automator/install.bat).
The script should take care of everything.  
To do this, double click the `.bat` file in your file browser. After installation, the CMD window will remain open, and the new conda environment `cert` will be active. The current directory displayed in your CMD window should now be the folder where you have the [certificate_generator.py](https://github.com/ralbso/python/blob/master/certificate_automator/certificate_generator.py) file.  
Now, simply type `python certificate_generator.py`, and the program will run.

#### MacOS, Linux
Please run [install.sh](https://github.com/ralbso/python/blob/master/certificate_automator/install.sh). This script will take care of everything.  
To do this, double click the `.sh` file in Finder. After installation, the Terminal will remain open, and the newly created conda environment `cert` will be active. The current directory displayed in your Terminal should now be the folder where you have the [certificate_generator.py](https://github.com/ralbso/python/blob/master/certificate_automator/certificate_generator.py) file. Now, simply type `python certificate_generator`, and the program will run.

## Editing email
This applet not only creates and saves certificates, it also emails the certificates to the corresponding recipient. I'm quite sure you don't want to send the default email. To edit the content of your message, please edit the [email_attendees.py](https://github.com/ralbso/python/blob/master/certificate_automator/email_attendees.py) script. The variables in the code are very self-explanatory, but just in case, here's a quick little guide:  
* `sender`: This is the name that will appear in the "From" field in the email you will send.
* `subject`: This one's obvious. Just change the subject to whatever you want.
* `receiver`: This one should not be messed with. It receives the list of emails you input on the applet.
* `body`: Now **this** is what you really want to change. This is the body of your email. It follows the conventional string notation: no markup of any kind (no **bold**, not _italics_), and write everything between quotation marks (`""`). To create a new paragraph, use `\n` (equivalent to hitting `Enter` once).
* `server.login`: This is used to log into the email. I wrote this for use within the organization **Neuro-RUM**, but if for any reason you want to change the email you send the message from, simply change the email in this field.  

Anything else should not be messed around with if you're not experienced with programming.

## Known Issues
There are no known issues at the moment.

## Licensing
Copyright (c) 2019 Raul Mojica Soto-Albors under the
[MIT License](https://tldrlegal.com/license/mit-license):  

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so.

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
