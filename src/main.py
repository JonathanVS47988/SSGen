from textnode import TextNode, TextType
from copy_static import copy_src_to_dest

def main():
    #FirstObj = TextNode("test text!", TextType.LINK, "https://www.boot.dev")
    #print(FirstObj)

    copy_src_to_dest("./static", "./public")

main()