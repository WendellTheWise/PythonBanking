#!/bin/sh
set -e

NAME="budget-tracker"
MAIN="main.py"
DESCRIPTION="A python, terminal run, budget, income and expenses tracker"
MAINTAINER="Odin Kirkham <okir9913@gmail.com>"

VERSION="${1:-1.0.0}"
PKG="${NAME}_${VERSION}_all"

rm -rf "$PKG"
mkdir -p "$PKG/DEBIAN" "$PKG/usr/bin" "$PKG/usr/share/$NAME"

tar --exclude=./.git --exclude=./.github --exclude=./build-deb.sh \
    --exclude=./.gitignore --exclude="./${NAME}_*" --exclude='__pycache__' \
    -cf - . | tar -xf - -C "$PKG/usr/share/$NAME"

echo '#!/bin/sh' > "$PKG/usr/bin/$NAME"
echo "exec python3 /usr/share/$NAME/$MAIN \"\$@\"" >> "$PKG/usr/bin/$NAME"
chmod 755 "$PKG/usr/bin/$NAME"

echo "Package: $NAME" > "$PKG/DEBIAN/control"
echo "Version: $VERSION" >> "$PKG/DEBIAN/control"
echo "Architecture: all" >> "$PKG/DEBIAN/control"
echo "Maintainer: $MAINTAINER" >> "$PKG/DEBIAN/control"
echo "Depends: python3" >> "$PKG/DEBIAN/control"
echo "Description: $DESCRIPTION" >> "$PKG/DEBIAN/control"

dpkg-deb --build --root-owner-group "$PKG"
echo "Built $PKG.deb"
