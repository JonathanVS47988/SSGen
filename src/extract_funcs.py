#extract_funcs.py

import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    QUOTE = "quote"
    CODE = "code"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def extract_markdown_images(text):

    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
 
def extract_markdown_links(text):
       
   return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def markdown_to_blocks(markdown):

    block_strings = []
    
    split_strings = markdown.split('\n\n')
    for raw_block in split_strings:
        raw_block = raw_block.strip()
        if raw_block != '':
            block_strings.append(raw_block)
    
    return block_strings

def block_to_block_type(md_text):
    lines = md_text.split('\n')
    current_num = 1
    
    if re.match(r"^`{3}.*\`{3}$", md_text, re.DOTALL):
        return BlockType.CODE
    
    if re.match(r"#{1,6} ", lines[0]):
        return BlockType.HEADING
    
    is_quote_block = True
    for line in lines:
        if not line.startswith('>'):
            is_quote_block = False
            break
    if is_quote_block:
        return BlockType.QUOTE
    
    is_unordered_list_block = True
    for line in lines:
        if not line.startswith('- '):
            is_unordered_list_block = False
            break
    if is_unordered_list_block:
        return BlockType.UNORDERED_LIST
       
    is_ordered_list_block = True
    for line in lines:
        cap_num = re.match(r"^(\d+)\. ", line)
        if cap_num is None or int(cap_num.group(1)) != current_num:
            is_ordered_list_block = False
            break
        current_num += 1

    if is_ordered_list_block:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH