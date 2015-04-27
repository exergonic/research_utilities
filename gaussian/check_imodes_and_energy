#!/bin/bash

# About ---------------------------------------------------------------
#
# Will check every Guassian output file in a directory (*.log)
# for an imaginary mode and place free energy results plus the 
# "imaginary mode status" ( 0 = no IM ; 1 = has IM ) in a results
# text file.
#
# Invocation ----------------------------------------------------------
#
# ./IMandG.sh
# 
# Takes no arguments.
#
# ---------------------------------------------------------------------

# sane bash behavior
set -e # exit on first error
set -u # error on unset
# Variables ----------------------------------------------------------

declare results_file=results.txt
# variable for whether or not molecule possesses imaginary mode
declare im_status
# variable for testing presence of imaginary mode.
declare has_im
# variable for free energy of molecule.
declare G

# ----------------------------------------------------------------------

# Main script ---------------------------------------------------------

for logfile in *.log 
do
	# set im_status to 0, meaning no imaginary mode.
	im_status=0
	# see if log file has imaginary mode by grepping for "imaginary".
	has_im="$( grep "imaginary" $logfile )"
	# if has_im contains text, then the file has an IM, so set im_status=1.
	[[ -n "$has_im" ]] && im_status=1
	# variable G will be the free energy.
	G="$( grep "Sum of electronic and thermal Free Energies" $logfile | awk -F"=" '{ print $2 }'  )"
	# output the filename, free energy, and im_status to the results file.
	printf "%s\t%s\t%s\n" "$logfile" "$G" "$im_status" >> $RESULTS_logfile
done

printf "%s\n" "All done!"

exit 0
