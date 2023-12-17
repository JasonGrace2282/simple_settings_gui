# Creater: JasonGrace2282


pkgver=0
pkgrel=1
pkgname="simple_settings_gui-git"

pkgdesc="A gui to hold other gui launchers"
arch=('any')
url = "https://github.com/JasonGrace2282/${pkgname%-git}"
license="GPL3"
provides=("${pkgname%-git}")
conflicts=("${pkgname%-git}")
makedepends=("git")
depends=("python" "python-tk" "customtkinter")

prepare()
{
  git clone https://gitlab.com/william.belanger/${pkgname%-git}.git --single-branch
}

package()
{
    cd "${pkgname%-git}"
    echo "{}" > ~/.config/settings_map.json
}
