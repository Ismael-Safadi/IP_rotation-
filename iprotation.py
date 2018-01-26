import subprocess
import time
import os
print("""
#########################################################
#  _______            __                                #
# /       \          /  |                               #
# $$$$$$$  | ______  $$ | __     __  ______    _______  #
# $$ |__$$ |/      \ $$ |/  \   /  |/      \  /       | #
# $$    $$/ $$$$$$  |$$ |$$  \ /$$//$$$$$$  |/$$$$$$$/  #
# $$$$$$$/  /    $$ |$$ | $$  /$$/ $$ |  $$ |$$      \  #
# $$ |     /$$$$$$$ |$$ |  $$ $$/  $$ |__$$ | $$$$$$  | #
# $$ |     $$    $$ |$$ |   $$$/   $$    $$/ /     $$/  #
# $$/       $$$$$$$/ $$/     $/    $$$$$$$/  $$$$$$$/   #
#                                  $$ |                 #
#                                  $$ |                 #
#                                  $$/                  #
#          	                                        #
#########################################################
*IP Rotation*
*Developed By:Ismael Al-safadi*

""")
interface="eth0"
port="25"
chanel="11"
#ip="192.168.0.1"
with open("iplist.txt", "rU") as x:

        for i in x:
            i=i.strip()
            command=("iptables -t nat -I POSTROUTING -m state --state NEW -p tcp --dport {} -o {} -m statistic --mode nth --every {}  --packet 0 -j SNAT --to-source {}".format(port ,interface,chanel,i))
            try:
                subprocess.Popen(command,shell=True)
                time.sleep(1)
                print "commant executed ^__^"
            except:
                print "Ops!! I can't execute this command "
                    
