__author__ = "JJ.sven"

import xml.etree.ElementTree as ET

tree = ET.parse('xml_source')
root = tree.getroot()

# node = ET.Element

# tag 标签
# attrib 属性
# text 标签内容文本
print(root, root.tag)

# 全遍历（递归就行了）
for child in root:
    print(child.tag, child.attrib, child.text)
    for i in child:
        print(i.tag, i.attrib, i.text)

# # 遍历指定tag的节点
for node in root.iter('year'):
    print(node.tag, node.text, node.attrib)
    new_year = int(node.text)
    # 修改text
    node.text = str(new_year)
    # 修改atrib
    node.set('attri', 'content')
    node.set('atr2', 'hehe')
    # 修改tag
    node.tag = 'YEAR'

# 删除node
for node in root.iter('country'):
    info = node.find('info')
    if info:
        node.remove(info)

tree.write('xml_source')

# 创建xml文件
root = ET.Element('root')
a = ET.SubElement(root, 'sub1', {'attri':'content'})
a.text = 'sub1 content'

b = ET.SubElement(a, 'sub2', {'attri': 'content'})
b.text = 'sub2 content'

tr = ET.ElementTree(root)
tr.write('xml_build.xml', encoding='utf-8', xml_declaration=True, short_empty_elements=True)
ET.dump(root)