"""
remove_first_and_last(list_to_clean)

html = ['<h1>' , 'some content', ''</h1>]

returned remove_first_and_last(html)
=> ['some content] ----this should be returned

html2 = ['<h1>' , 'some content', ''</h1>]
"""

def remove_first_and_last(list_to_clean): # say function remove first and last and list to clean is passed in
    _, *content, _ = list_to_clean      # GLOB(ability to grab the elements, * returns the list in the middle) _ will ignore the element
    return content                          # don't need to return it with the * because we aren't globbing yet 


html = ['<h1>', 'My content', '</h1>']    # 

print(remove_first_and_last(html))        # removed the first and last elements

other_content_to_clean = ['', 'My content', 'Something else', '/']

print(remove_first_and_last(other_content_to_clean)) # this will glob the first and last elements and glob the 2 strings elements in the list