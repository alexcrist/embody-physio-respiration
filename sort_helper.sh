#!/usr/bin/env bash

# Get arguments
PID=$1
DATE=$2
START_TIME=$(echo $3 | sed 's/^0*//')
END_TIME=$(echo $4 | sed 's/^0*//')
DATA_DIRECTORY=$5

# Make directory with patient ID
mkdir -p $PID

# Loop through each file in the current directory
for FILENAME in $DATA_DIRECTORY/*; do

  FILEDATE=${FILENAME:7:8}
  if [ "$FILEDATE" == "$DATE" ]; then
    break
  fi

  # Extract time from filename (characters 16 - 21)
  TIME=${FILENAME:16:6}
  TIME=$(echo $TIME | sed 's/^0*//')

  # If time is in our window
  if (( TIME >= START_TIME )) && (( TIME <= END_TIME ))
  then

    # copy file to directory
    cp $FILENAME $PID

  fi

done
