import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",
                      help="enter interface")
    parser.add_option("-m", "--mac", dest="new_mac", help="enter new mac")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error('[-] invalid  interface')

    if not options.new_mac:
        parser.error('[-] invalid mac')
    return options


def mac_changer(interface, newMac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", newMac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    if_config_result = subprocess.check_output(["ifconfig", interface])
    reg_exp_match = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",
                              f_config_result.decode('utf-8'))
    if reg_exp_match:
        return reg_exp_match.group(0)

    else:
        print("[-] we could not read the current mac address of " + interface)


options = get_arguments()

current_mac = get_current_mac(options.interface)
print("[+] current mac is " + str(current_mac))
mac_changer(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+]current mac is successfully changed to " + options.new_mac)
else:
    print("[+]current mac could not be changed")
