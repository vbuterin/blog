#!/usr/bin/python3
import os, sys

os.system('rsync -av site/. root@{}:/var/www/html'.format(sys.argv[1]))
