# 4. На вход функции передается строка с xml документом (тэги без аттрибутов, корневой элемент только один).
#    Нужно выполнить следующее преобразование и вывести максимальную вложенность.
#    Пример:
#         a = '<root><element1 /><element2 /><element3><element4 /></element3></root>'
#         foo(a) ->
#         {
#             'name': 'root',
#             'children': [
#                 {'name': 'element1', 'children': []},
#                 {'name': 'element2', 'children': []},
#                 {
#                     'name': 'element3',
#                     'children': [
#                         {'name': 'element4', 'children': []}
#                     ]
#                 }
#             ]
#         }, 2
#       в данном случае у element4 тэга вложенность/глубина 2


def tag_parse(input):
    if (input[:1] == "<") & (input.find("/") == -1):
        key = 'parent'
    if (input[:1] == "<") & (input[len(input)-2:] == "/>"):
        key = "wo_children"
    if (input[:2] == "</"):
        key = 'parent_end'
    return key


def to_tag_with_key(input_xml):
    tags = {}
    while (len(input_xml) > 0):
        left_brace = input_xml.find("<")
        right_brace = input_xml.find(">")
        tag = input_xml[left_brace:right_brace + 1]
        rest = input_xml[right_brace + 1:]
        tags.update({tag: tag_parse(tag)})
        input_xml = rest
    return tags


def xml_to_tree(input_xml):
    xml_tree = to_tag_with_key(input_xml)

    tree = {}
    parent = ""
    parents = []

    for tag in xml_tree:
        # print(xml_tree[el])

        if xml_tree[tag] == 'parent':
            tree.update({tag: parent})
            parent = tag
            parents.append(tag)
        else:
            if xml_tree[tag] == 'wo_children':
                tree.update({tag: parent})
            else:
                if len(parents) > 1:
                    parent = parents[len(parents) - 2]
                    parents = parents[:len(parents)-1]
                else:
                    parent = ""
                tree.update({tag: parent})
    return tree


def xml_parser(input_xml):
    xml_tree = xml_to_tree(input_xml)

    return xml_tree


a = '<root><element1 /><element2 /><element3><element4 /></element3><element5 /></root>'
# b = '<element1 /><element2 /><element3><element4 /></element3>'
# c = '<element3><element4 /></element3>'
print(a)
print(xml_parser(a))



# def childrenParse(input_xml):
#     left_brace = input_xml.find("<")
#     right_brace = input_xml.find(">")
#     if (len(input_xml) > 0) & (left_brace != -1) & (right_brace != -1):
#         tag = input_xml[left_brace + 1:right_brace]
#         rest = input_xml[right_brace + 1:]
#         children = []
#         parent = ""
#
#         if (tag.find("/>") != -1):
#             children.append({'name':tag, 'children': []})
#
#
#         else:
#             if(tag.find("/") == -1):
#                 rest = rest[:rest.find("</" + tag)]
#                 # parsed = root_parse(rest)
#         parsed = {'name': tag, "children": children}
#
#     return (rest, parsed, parent)
#
# a = '<root><element1 /><element2 /><element3><element4 /></element3></root>'
# b = '<element1 /><element2 /><element3><element4 /></element3>'
# c = '<element3><element4 /></element3>'
# print(a)
# print(childrenParse(a))
# print(b)
# print(childrenParse(b))


#
#
#
#
#
#
#
# def xmlParser(input_xml):
#     left_brace = input_xml.find("<")
#     right_brace = input_xml.find(">")
#     if (len(input_xml) > 0) & (left_brace != -1) & (right_brace != -1):
#         tag = input_xml[left_brace+1:right_brace]
#         rest = input_xml[right_brace+1:]
#         children = []
#         parsed = {}
#         parent = ""
#
#         if (tag.find("/") == -1):
#             inside_tag = rest[:rest.find("</" + tag)]
#             print("inside tag", inside_tag)
#
#             brothers_check_list = inside_tag.split("<")[1:]
#             print("brothers list", brothers_check_list)
#
#             # for (len(inside_tag)>0):
#             #     children.append(xmlParser(inside_tag))
#
#             parsed = {'name': tag, 'children': children}  # xmlParser(inside_tag)
#
#             # brothers = []
#             # brothers_check_list = inside_tag.split("<")[1:]
#             # print("brothers list", brothers_check_list)
#             # for el in brothers_check_list:
#             #     brothers.append(el)
#             #     if (el.find("/") == -1):
#             #         break
#             # for el in brothers[:len(brothers) - 1]:
#             #     tag = el[:el.find(" /")]
#             #     parsed.append({'name': tag, 'children': []})
#
#             # next_el_parse = brothers[len(brothers) - 1]
#             # next_el = next_el_parse[:next_el_parse.find(">")]
#             # parsed.append({'name': next_el, 'children': xmlParser(inside_tag)})
#         else:
#             parsed = {'name': tag, 'children': []}
#
#     return parsed
#
#
# a = '<root><element1 /><element2 /><element3><element4 /></element3></root>'
# b = '<element1 /><element2 /><element3><element4 /></element3>'
# c = '<element3><element4 /></element3>'
# print(a)
# print(xmlParser(a))
# print(b)
# print(xmlParser(b))