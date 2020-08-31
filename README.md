# tess_c3

## Description 
This program uses the [Web TESS Viewing Tool](https://heasarc.gsfc.nasa.gov/cgi-bin/tess/webtess/wtv.py) to count how many sectors a star will be observed in in cycle 3. 

## Table of Contents
- Progress
- File Descriptions
- Obtaining Data

## Progress
This program runs successfully; it writes each star to a separate file and also writes the number of sectors each star will be observed in in cycle 3. 

## File Descriptions
- TIC_C3.txt: This text file contains a list of stars. It's the input file used by TESSC3.py to search for each star in the Web TESS Viewing Tool. 
- TESSC3.py: This program uses the Web TESS Viewing Tool to find the number of sectors each star will be observed in in cycle 3. It writes all of this information to TESSc3_updated.txt. 
- TESSc3_updated.txt: This is the separate text file that the TESSC3.py program writes to. 

## Obtaining Data
The data is obtained using the [Web TESS Viewing Tool](https://heasarc.gsfc.nasa.gov/cgi-bin/tess/webtess/wtv.py). 

