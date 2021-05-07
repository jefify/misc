#!/bin/bash

for h in *.html
do
  [[ $h = template* ]] && continue
  mkdir -p src-${h%%.html}
  cd src-${h%%.html}
  egrep "(src.*http|link.*href.*http)" ../$h | cut -d'"' -f2 | sort | uniq | while read u
  do
    [ -f ${u##*/} ] || wget $u
  done
  cd ..
  (( `find src-${h%%.html} -type f | wc -l` )) || rmdir src-${h%%.html}
done

