#!/bin/sh
set -e

# ---- Edit these for each project ----
NAME="budget-tracker"          # lowercase, no spaces: becomes the command you type
MAIN="main.py"            # file that starts the program
DESCRIPTION="A python, terminal run, budget, income and expenses tracker"
MAINTAINER="Odin Kirkham okir9913@gmail.com"
# -------------------------------------

VERSION="${1:-1.4}"
PKG="${NAME}_${VERSION}_all"

rm -rf "$PKG"
mkdir -p "$PKG/DEBIAN" "$PKG/usr/bin" "$PKG/usr/share/$NAME"

tar --exclude=./.git --exclude=./.github --exclude=./build-deb.sh \
    --exclude=./.gitignore --exclude="./${NAME}_*" --exclude='__pycache__' \
    -cf - . | tar -xf - -C "$PKG/usr/share/$NAME"

cat > "$PKG/usr/bin/$NAME" <<EOF
#!/bin/sh
exec python3 /usr/share/$NAME/$MAIN "\$@"
EOF
chmod 755 "$PKG/usr/bin/$NAME"

cat > "$PKG/DEBIAN/control" <<EOF
Package: $NAME
Version: $VERSION
Architecture: all
Maintainer: $MAINTAINER
Depends