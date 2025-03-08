



def markdown_to_blocks(markdown):
    # Split the markdown string by double newlines
    raw_blocks = markdown.split("\n\n")
    
    # Process each block - strip whitespace and filter empty blocks
    blocks = []
    for block in raw_blocks:
        # Strip leading/trailing whitespace
        cleaned_block = block.strip()
        # Only add non-empty blocks
        if cleaned_block:
            blocks.append(cleaned_block)
    
    return blocks


