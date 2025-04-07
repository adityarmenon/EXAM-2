if [[ $(id -u) -eq 0 ]]; then
    echo " should not be running as root "
    exit 1
fi
echo "Running as non root"