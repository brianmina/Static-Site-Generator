


def split_into_blocks(markdown):
    # Step 1: Split the input markdown string at double newlines
    blocks = markdown.split("\n\n")
    
    # Step 2: Strip whitespace from each block
    cleaned_blocks = [block.strip() for block in blocks]
    
    return cleaned_blocks


# Sample markdown string
markdown_text = """
This is a paragraph.

# My Heading

- List item 1
- List item 2

Another paragraph here.
"""

# Use your function
blocks = split_into_blocks(markdown_text)

# Print the result
print(blocks)
