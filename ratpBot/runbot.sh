#!/bin/sh
echo "Initializing..."
  while true
  do
    echo "Bot started.. $(date)"
    python bot.py
    echo "The bot is crashed :( !"
    echo "Rebooting in: "
    for i in 1
    do
      echo "$i..."
  done
  echo "###########################################"
  echo "#Bot is restarting now $(date)            #"
  echo "###########################################"
done
