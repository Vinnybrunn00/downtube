W = '\033[0m'  # white 
G = '\033[32m'  # green
C = '\033[36m'  # cyan

def banner():
    text = f'''
{C}
    ██████╗  ██████╗ ██╗    ██╗███╗   ██╗    ████████╗██╗   ██╗██████╗ ███████╗
    ██╔══██╗██╔═══██╗██║    ██║████╗  ██║    ╚══██╔══╝██║   ██║██╔══██╗██╔════╝
    ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║       ██║   ██║   ██║██████╔╝█████╗  
    ██║  ██║██║   ██║██║███╗██║██║╚██╗██║       ██║   ██║   ██║██╔══██╗██╔══╝  
    ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║       ██║   ╚██████╔╝██████╔╝███████╗
    ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝       ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝
      
      {W}version 1.0.0              {G}› {W}By Vinícius Bruno: From Brazil                                                                               
'''
    print(text)