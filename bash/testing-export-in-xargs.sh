export ABC=123
echo ${ABC}
seq 1 10 | xargs -n 1 sh -c 'bash -c "echo ${ABC}"'
