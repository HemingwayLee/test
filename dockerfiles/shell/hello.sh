pkgName="$1"

if ! dpkg -l "$pkgName" &> /dev/null ; then
    echo "Please install $pkgName !"
fi
