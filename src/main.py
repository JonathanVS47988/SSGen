from textnode import TextNode, TextType
from copy_static import copy_src_to_dest
from generate_page import generate_pages_recursive

import sys

def main():

    if sys.argv[1]:
        basepath = str(sys.argv[1]+"/")
    else:
        basepath = "/"

    copy_src_to_dest("./static", "./docs")
    generate_pages_recursive("./content", "./template.html", "./docs", basepath)

main()