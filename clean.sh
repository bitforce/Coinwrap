a='__pycache__'
b='.ropeproject'
c='.cache'
d='*.pyc'
if test "find . -name $a"; then
    find . -name $a -type d -exec echo "removing '{}'" \;
    rm -rf `find . -type d -name $a`
fi
if test "find . -name $b"; then
    find . -name $b -type d -exec echo "removing '{}'" \;
    rm -rf `find . -type d -name $b`
fi
if test "find . -name $c"; then
    find . -name $c -type d -exec echo "removing '{}'" \;
    rm -rf `find . -type d -name $c`
fi
if test "find . -name $d"; then
    find . -name $d -type f -exec echo "removing '{}'" \;
    rm -rf `find . -type f -name $d`
fi

