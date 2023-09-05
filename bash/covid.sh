#!/bin/bash
# This script downloads COVID-19 data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
DEATHS=$(echo $DATA | jq '.[0].death')
HOSPITALIZED=$(echo $DATA | jq '.[0].hospitalizedCurrently')
TODAY=$(date)

echo"on $TODAY, there were $POSITIVE positive cases, $NEGATIVE negative tests, $DEATHS deaths, and $HOSPITALIZED hospitalized."





