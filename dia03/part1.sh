if [[ ! -f $1 || $# -eq 0 ]]; then
	file='test.txt'
else
	file=$1
fi

cat $file | grep -oP '(?<=mul)\([0-9]+,[0-9]+\)' | tr -d '()' | awk -F ',' '{sum += $1 * $2 }END{print sum}'
