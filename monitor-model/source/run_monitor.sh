#!/bin/ash

while :
do
  date
  echo "--- Running monitor..."
  python main.py
  RET=$?
  if [ ${RET} == 2 ];
  then
    echo "Exit status 2"
    exit 0
  fi

  if [ ${RET} -ne 0 ];
  then
    echo "Exit status not 0"
    echo "Sleep 120"
    sleep 120
    break
  fi

  date
  echo "Sleep 60"
  sleep 60
done