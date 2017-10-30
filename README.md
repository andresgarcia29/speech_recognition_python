# Script in python to use Speech Recognition of Google Cloud
----
### 1- Install all modules of Google

- Install python modules

```
pip install --upgrade google-cloud
```

- Install Gcloud:

Mac Os and Linux

The installation needs to admministrator permissions you have give it with "sudo su" affter execute the first command.

```
1:
curl https://sdk.cloud.google.com | bash
2:
exec -l $SHELL
3:
gcloud init
```

When the script ask "Modify profile to update your $PATH and enable shell command 
completion?" you have to select "Y" because you're using "sudo" the configuration will be save in [/var/root/.bash_profile] so the next thing to do is writte in the console "cat /var/root/.bash_profile" we have to copy the text.

- The next line updates PATH for the Google Cloud SDK.
if [ -f '/Users/macbook/google-cloud-sdk/path.bash.inc' ]; then source '/Users/macbook/google-cloud-sdk/path.bash.inc'; fi

- The next line enables shell command completion for gcloud.
if [ -f '/Users/macbook/google-cloud-sdk/completion.bash.inc' ]; then source '/Users/macbook/google-cloud-sdk/completion.bash.inc'; fi

Next we have to paste in the console configuration in my case is in 
```
/Users/profile/.bash_profile
```
Then reload the configurarion with:
```
source ~/.bash_profile
```

> My recomendation is when you use "sudo su" when the script say "Do you configure your path" you should to write the path where the information about gcloud is saved! in my case /Users/my_profile_name

- For windows

https://cloud.google.com/sdk/downloads#windows

### 2- Install SoX

- Mac os:

```
brew install sox
```

- Linux:

```
sudo apt-get install libasound2-plugins libasound2-python libsox-fmt-all
sudo apt-get install sox
```

SoX - Sound eXchange
https://audio.online-convert.com/es/convertir-a-flac

> "Now that we have Sox installed, we can start setting up our Python script. Because Google’s Speech Recognition API only accepts single-channel audio, we’ll probably need to use Sox to convert our file."

Sox is a script to decode de audio files.

When you have a file, you have you put in the root path of the index.py.

Then configure the file convert.py with the name of the file and then execute the script.

### 3- Finish

Configure the name of the file in index.py and run the script. Wait, and enjoy it!