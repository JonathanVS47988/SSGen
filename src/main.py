from textnode import TextNode, TextType
from copy_static import copy_src_to_dest
from generate_page import generate_page

def main():
    #FirstObj = TextNode("test text!", TextType.LINK, "https://www.boot.dev")
    #print(FirstObj)

    copy_src_to_dest("./static", "./public")
    generate_page("./content/index.md", "./template.html", "./public/index.html")

main()