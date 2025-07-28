from textnode import TextNode, TextType

def main():
    FirstObj = TextNode("test text!", TextType.LINK, "https://www.boot.dev")

    print(FirstObj)

main()