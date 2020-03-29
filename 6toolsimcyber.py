#cara membuat tools untuk pemula
clear
figlet "Tools"
echo "=========================================="
echo " Author  : Wahyuoktafian"
echo " YouTube : https://www.youtube.com/channel/UCVzhlGQYAGHWv2uMkGaDP8w"
echo " GitHub  : https://github.com/Wahyuoktafian/6Tools-Termux-ByIMCYBER"
echo "=========================================="
echo
echo "Pilih Menu Tools Nya Slur And Subcribe Channel gw yak ^_^"
echo "[1] Dark FB"
echo "[2] MBF"
echo "[3] DDOS"
echo "[4] Hack CCTV"
echo "[5] Prank spammer"
echo "[6] Tools Hack FB"
echo "[7] Install Bahan"
read -p "[?] Pilih : " pil;
# Batas gan
if [ $pil = 1 ]
then
git clone https://github.com/B4N954N2-ID/DarkPremium
cd DarkPremium
python2 darkpremium.py
fi
# batas gan
if [ $pil = 2 ]
then
git clone https://github.com/pirmansx/mbf
cd mbf
pythob2 MBF.py
fi
# batas gan
if [ $pil = 3 ]
then
git clone https://github.com/cyweb/hammer
cd hammer
python hammer.py
fi
# batas gan
if [ $pil = 4 ]
then
git clone https://github.com/kancotdiq/ipcs
cd ipcs
python2 scan.py
fi
# batas gan
if [ $pil = 5 ]
then
git clone https://github.com/B4N954N2-ID/prank
cd prank
python2 spam.py
fi
# batas gan
if [ $pil = 6 ]
then
git clone https://github.com/FR13ND8/BRUTEFORCEnew
cd BRUTEFORCEnew
sh new.sh
fi
# batas gan
if [ $pil = 7 ]
then
apt update && apt upgrade
pkg install nano
pkg install python
pkg install git
pkg install python2
pip install requests mechaniz
pip2 install requests mechanize
pkg install php
fi
