# Heredoc-multi line strings
# start by creating the variable content
# simliar to multi line comments use 3 double quotes (for herdocs) wrap it all in 3 single or double quotes
# now to remove the new lines from top and bottom use function strip()  always place parens at the end of functions

content = """
Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.

Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
""".strip()

print(content)