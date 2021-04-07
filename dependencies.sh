#!/bin/bash

set -eu -o pipefail
sudo -n true
test $? -eq 0 || exit 1 "Execute script with sudo"

# check for python
if [[ "$(python3 -V)" =~ "Python 3" ]] 
then
	echo "Python 3 is installed."
else
	echo "Installing Python 3..."
	apt-get install python3
fi

# check for pip
if [[ "$(pip3 -V)" =~ "pip" ]]
then
	echo "Pip is installed."
else
	echo "Installing Pip 3..."
	apt-get install python3-pip
fi

# check for ffmpeg
if [[ "$(ffmpeg -version)" =~ "ffmpeg version" ]]
then
	echo "FFMPEG is installed."
else
	echo "Installing FFMPEG..."
	apt-get install ffmpeg $1 -y
fi

# install pip dependencies
echo "Install pip dependencies? (yn)"
read op
if [ "$op" = "y" ] 
then
	echo "Installing pip dependencies..."
	pip3 install discord
	pip3 install youtube-dl
	pip3 install pydub
	pip3 install python-dotenv
	pip3 install -U discord.py\[voice\]
fi

echo "Complete."
