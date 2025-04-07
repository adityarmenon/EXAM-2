file="/home/arm/Codes/exam/scripting exam/shell/file.txt"

hash(){
    sha256sum "$file"
}

if [ ! -f "$file" ];then
    echo " File doesnt exist"
    exit 1
fi

oghash=$(hash)
 echo "Original hash: $oghash"

read -p "Press Crtl D once you complete"

newhash=$(hash)
echo "New hash: $newhash"

if [ "$oghash" == "$newhash" ];then
    echo "File not changed"
else
    echo "File Modified"
fi