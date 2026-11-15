import os
import fb_page

try:
    fb_page.main()
except AttributeError:
    print("[!] Error: 'fb_page' module has no 'main' function. Please check your .so file compilation.")
