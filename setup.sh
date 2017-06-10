#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install i2c-tools
sudo apt-get install python-smbus
sudo adduser pi i2c
sudo apt-get install python-dev python-setuptools
sudo easy_install Pillow

sudo raspi-config nonint do_expand_rootfs
sudo raspi-config nonint do_i2c 1

