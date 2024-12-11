import socket, termcolor


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def scan_target_port(target, port):                 #scans a target on a given port
    try:
        sock.connect((target, port))
        print(termcolor.colored((f"Port {port} is open"), "green"))
        banner = sock.recv(1024).decode('utf-8')
        print(banner)
        sock.close()
    except:
        pass


def scan_target_ports(target, ports):                #scans a target with a range of ports
    print(termcolor.colored((f"[+] Starting Scan For This Target -> {target}"), "green"))
    for port in range(1, ports+1):
        scan_target_port(target, port)

def main():
    targets = ""
    try:
        while targets.strip() == "":
            targets = input(termcolor.colored(("[*] Enter Target To Scan Separated By comma(,) (e.g. 192.100.23.4, example.com) or Enter A Single Target To Scan (e.g. scan_me.com ): "), "light_green"))
            if targets == "":
                print("Target Field can not be empty")

        ports = int(input(termcolor.colored(("[*] Enter How Many Ports You Want To Scan(e.g. 100): "), "light_green")))

        if ',' in targets:
            targets = targets.split(",")
            print(targets)
            print(termcolor.colored(("[*] Scanning Multiple Targets"), 'blue'))
            for target in targets:                                                  #scans multiple targets
                scan_target_ports(target.strip(),ports)
        else:
            scan_target_port(targets, ports)

    except:
        print("An Error occurred")


if __name__ == "__main__":
    main()






