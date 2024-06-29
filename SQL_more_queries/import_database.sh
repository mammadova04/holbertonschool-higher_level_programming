#!/bin/bash

# Variables
USERNAME="root"
PASSWORD="root"
DATABASE="hbtn_0d_tvshows"
DUMP_URL="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql"
DUMP_FILE="hbtn_0d_tvshows.sql"

# Download the database dump
wget -O $DUMP_FILE $DUMP_URL

# Create the database
mysql -u $USERNAME -p$PASSWORD -e "CREATE DATABASE IF NOT EXISTS $DATABASE;"

# Import the database dump
mysql -u $USERNAME -p$PASSWORD $DATABASE < $DUMP_FILE

