import re

sen = 'void update_position(struct srv *s)'
fn_match = re.match(r"((int)|(float)|(void)|(double)|(char))\s+([\w]+)(\((.*?)\))",sen)

argument_list = fn_match.group(9)

fn_name = fn_match.group(7)

v = "init_tree = next_tree;"
fn_match = re.match(r"([\s]*([a-zA-Z_0-9]+)[\s]*\=[\s]*[a-zA-Z_0-9]+)",v)
print(fn_match.group(2))