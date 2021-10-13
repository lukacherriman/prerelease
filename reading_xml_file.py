import xml.etree.ElementTree as et

"""with open('C:/PythonFiles/books.xml', 'r') as reader:
    data = reader.readlines()
    new_data = ""
    for line in data:
        new_data += line"""


"""root = et.fromstring(tree)
print(root)
xml_string = et.tostring(root).decode('utf8')"""

"""print(child_list)

for current_book in root.findall(child_list[0]):
    print(current_book.tag, current_book.attrib)
    for elements in current_book.findall(''):
        print(elements.tag, elements.attrib)
        """

tree = et.parse('C:/PythonFiles/books.xml')
root = tree.getroot()


# used recursion to get all the nodes into a list
def get_children(node):
    "print(node.tag, node.attrib, node.text)"
    child_list = [node.tag, node.attrib, node.text]
    for child in node:
        if child not in child_list:
            child_list.append(get_children(child))
    return child_list


def parseXML(data):
    root = et.fromstring(data)
    news_items = []
    for item in root.findall('book'):
        for child in item:
            print(child.tag, child.text)


# played around with how to display the xml file after getting it into a list
def print_xml(list):
    print(tree_list[0])
    for i in range(3, len(tree_list)):
        for j in range(len(tree_list[i])):
            if type(tree_list[i][j]) is list:
                print(f"    {tree_list[i][j]}")
            else:
                print(f"\n  {tree_list[i][j]}")


new_book = et.SubElement(root, 'book', {'category': 'history'})
title = et.SubElement(new_book, 'title')
author = et.SubElement(new_book, 'author')
price = et.SubElement(new_book, 'price')
year = et.SubElement(new_book, 'year')
title.text = 'history of the world'
author.text = 'Luka Cherriman '
price.text = '10.00'
year.text = '2021'

parseXML(tree)
tree_list = get_children(root)
print_xml(tree_list)



"wasn't sure which data I would populate the dictionary with so I decided to print the tree from a list instead"



