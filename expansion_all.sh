for file in `find ./src/*/*.py`; do
    echo $file
    newfile=`echo ${file/src/expansion}`
    pypy3 expansion.py $file $newfile
done
for file in `find ./src/*.test.py`; do
    echo $file
    newfile=`echo ${file/src/expansion}`
    pypy3 expansion.py $file $newfile
done

black expansion
ruff --fix expansion
