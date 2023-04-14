import colorama
import argparse
from scapy.all import ARP, Ether, srp
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

def arp_request(target):
	try:
		packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=target)
		result = srp(packet, timeout=2, verbose=0)[0]
		print(f"{Fore.GREEN}IP ADDRESS" + " "*10 + f"MAC ADDRESS{Fore.RESET}")
		for sent, received in result:
			print("{:16}    {}".format(received.psrc , received.hwsrc))

	except Exception as e:
		print(f"{Fore.RED}[!] Error: {Fore.RESET}", e)

argument_parser = argparse.ArgumentParser(description='Local net scanner')
argument_parser.add_argument('-t', required=True, type=str, help='Target Ex: 192.168.2.1/24')
args = argument_parser.parse_args()

arp_request(args.t)
