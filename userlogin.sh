username="arm"
if who | grep -q "$username"; then
    echo "user logged in "
else    
    echo "not logged in"
fi