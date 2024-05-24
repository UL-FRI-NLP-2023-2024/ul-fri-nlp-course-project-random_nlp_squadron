#!/bin/bash

input_file=data/$1
vertical_file=data/vf_$1
deduplicated_file=data/d_$1

# Convert to vertical file
sed -e 's/ /\n/g' -e 's/<content>/<content>\n/g' -e 's/<\/content>/\n<\/content>/g' $input_file > $vertical_file

echo Here
# Run the deduplicator
onion-1.4/src/onion -sm -n 5 -p content -d xml $vertical_file > $deduplicated_file
rm $vertical_file

# Convert back to the original form
sed -i -e ':a;N;$!ba;s/\n/ /g' -e 's/> </></g' -e 's/<content> /<content>/g' -e 's/ <\/content>/<\/content>/g' -e 's/<\/item>/<\/item>\n/g' -e 's/<items>/\n<items>\n/g' $deduplicated_file