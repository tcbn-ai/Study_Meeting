#!/bin/bash
files='*.pdf'
for filepath in ${files}
do
	echo $filepath
	pdftocairo -svg "${filepath}" "${filepath}.svg"
done
