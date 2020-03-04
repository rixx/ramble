#!/bin/zsh
bundle exec jekyll build && rsync -avzu --info=progress2 -h _site/* tonks:/usr/share/webapps/ramble
