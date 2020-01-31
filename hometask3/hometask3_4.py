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


def tag_to_name(tag):
    tag = tag[1:len(tag)-1]
    if tag[:1] == "/":
        tag = tag[1:]
    slash = tag.find("/")
    if slash != -1:
        tag = tag[:slash-1]
    space = tag.find(" ")
    if space != -1:
        tag = tag[:space-1]
    return tag


# test_string = ['<root>', '</root>', '<root />']
# for el in test_string:
#     print(tag_to_name(el))


def tag_parse(input_tag):
    if (input_tag[:1] == "<") & (input_tag.find("/") == -1):
        key = 'parent'
    if (input_tag[:1] == "<") & (input_tag[len(input_tag) - 2:] == "/>"):
        key = "wo_children"
    if (input_tag[:2] == "</"):
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
    first_tag = list(xml_tree.items())[0][0]
    # print(tag_to_name(first_tag))
    # print(to_tag_with_key(input_xml)[first_tag])

    if first_tag.find("/") == -1:
        children = []
        children_tree = xml_tree.copy()
        children_tree.__delitem__(first_tag)
        children_tree.__delitem__("</"+tag_to_name(first_tag)+">")
        children_tree = {k: v for k, v in filter(lambda item: item[1] == first_tag, children_tree.items())}
        children_tree = {k: v for k, v in filter(lambda value: value[0][:2] != "</", children_tree.items())}
        # print("filtered ", children_tree)

        for tag in children_tree:
            if tag.find("/") != -1:
                child = {'name': tag_to_name(tag), 'children': []}
                children.append(child)
            else:
                child_with_child_string = input_xml[input_xml.find(tag): input_xml.find("</"+tag_to_name(tag)+">")+len(tag)+1]
                # print("child_with_child_string", child_with_child_string)
                children.append(xml_parser(child_with_child_string))
    else:
        children = []

    parsed = {'name': tag_to_name(first_tag), 'children': children}
    return parsed


def xml_output(input_xml):
    xml_out = xml_parser(input_xml)
    return xml_out

a = '<root><element1 /><element2 /><element3><element4 /></element3></root>'
print(a)
print(xml_output(a))