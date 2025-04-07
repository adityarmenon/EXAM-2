allowed=("user1" "arm" "user3")
cuser=$(whoami)

if [[ ! "${allowed[@]}" =~ "${cuser}" ]];then
    echo " Access denied"
fi
    echo "Access granted"



