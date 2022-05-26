#Modules

import socket,os,sys,argparse,requests


from sys import platform


#Color

G = '\033[92m'  # green
Y = '\033[93m'  # yellow
B = '\033[94m'  # blue
R = '\033[91m'  # red
W = '\033[0m'   # white



#start check if platfom is linux and other

if platform == "linux" or platform == "linux2" or platform == "win32" or platform == "darwin":

    def banner():
        #type of font is: big
        print("""%s

                     _____  _   _  _____     _ _                                      
                    |  __ \| \ | |/ ____|   | (_)                                     
                    | |  | |  \| | (___   __| |_ ___  ___ _____   _____ _ __ ___ _ __ 
                    | |  | | . ` |\___ \ / _` | / __|/ __/ _ \ \ / / _ \ '__/ _ \ '__|
                    | |__| | |\  |____) | (_| | \__ \ (_| (_) \ V /  __/ | |  __/ |   
                    |_____/|_| \_|_____/ \__,_|_|___/\___\___/ \_/ \___|_|  \___|_|   
                                                                    
                                                                    %s%s
                                        #######################
                                        #                     #
                                        # Coded By Kero Magdy #
                                        #                     #
                                        #######################
                                        
        """     % (R, W, Y))

    banner()

    def parser_error(errmsg):
        print("Usage: python " + sys.argv[0] + " (^_^) use -h for help")
        print(R + "Error: " + errmsg + W)
        sys.exit()
        

    def parse_args():
        # parse the arguments
        parser = argparse.ArgumentParser(epilog='%s\tExample: \r\npython3 ' %(Y) + sys.argv[0] + " -d example.com -s example%s" % (W) ,  description='DNS discoverer')
        parser.error = parser_error
        parser._optionals.title = 'OPTIONS'
        parser.add_argument('-d', '--domain', metavar='', help='Enter domain', required=True)
        parser.add_argument('-s', '--server', metavar='', help='Enter the server of domain by using (dig tool) Example: dig example.com -t ns  ', required=True)

        return parser.parse_args()



    try:
        print('%s\n\nversion:1.1.2\n\n%s' % (Y,W))
        
        def scan():
            results =  parse_args()
            domain  = results.domain
            server  = results.server

            #add "https://" for domain

            add = "https://" + domain

            if requests.post(add).status_code == 200:
                print("Valid Domain\n")
                print(add)
            else:
                print("Invalid Domain\n")
                print(add)
                exit()
                
            #public DNS

            def public_dns():
                first_scan = '%s\nFirst Scan!\n%s' % (R,W)
                print(first_scan)
                os.system('dnsenum ' + domain)

            public_dns()

            print('\n\n')
            second_scan = '%s\nSecond Scan!\n%s' % (R,W)
            print(second_scan)
            print('\n\n')
            #special DNS

            def special_dns():
                os.system('dig @' + server + ' axfr ' + domain)

            special_dns()

            print('\n\n')
            third_scan = '%s\nThird Scan!\n%s' % (R,W)
            print(third_scan)
            print('\n\n')

            ports = range(1,65536)

            for p in ports:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.settimeout(1)
                r = s.connect_ex((domain,p)) 

                if r == 0:
                    #more special DNS
                    for repeat in [p]:
                        service = socket.getservbyport(repeat)
                        print('--[ * {} * is open --> {} ]'.format(repeat,service))
                        os.system('dig @' + server + ' -p ' + str(repeat) + ' axfr ' + domain)
                else:
                    #print('this port' , p , 'is not open')
                    pass
                s.close()
        print('%s\nDon\'t forget to use version of python3\n%s' % (Y,W))

        scan()

    except:
        print('%s\nError,Please repeat the process to scan all ports again%s' % (R,W))

    else:
        print('\n%sScan Done!%s' % (Y,W))

#else:print('\n%sSorry, platform is not linux (▰˘︹˘▰)' % (R))
else:print("You must install dig and dnsenum both tools")
