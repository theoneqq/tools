def get_ip(*args):
        if platform.system() == 'Windows':
                my_name = socket.getfqdn(socket.gethostbyname('localhost'))
                my_addr = socket.gethostbyname(my_name)
                ip = my_addr.split('\n')[0]
                return ip
            else:
         
                my_addr = os.popen(
                                    "ifconfig | grep -A 1 %s|tail -1| awk '{print $2}'" % args[0]).read()
                        ip = re.search(r'(?<![\.\d])(?:25[0-5]\.|2[0-4]\d\.|[01]?\d\d?\.)'
                                                                r'{3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)(?![\.\d])',my_addr).group()
                                return ip
                                 
                                 
                                if __name__ == '__main__':
                                    f = get_ip('eno16777736')
                                        print(f)
