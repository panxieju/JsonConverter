from PyQt5.QtWidgets import QTreeWidgetItem, QHeaderView


def genDictItem(key, value, column):
    newColumn = 2  # dict新增两列
    root = QTreeWidgetItem()
    key = '(obj) '+key
    root.setText(column, key)
    keys = value.keys()
    newColumns = []
    for key in keys:
        child, count = genChildItem(key, value[key], column+1)
        newColumns.append(count)
        root.addChild(child)
    return root, newColumn + max(newColumns)


def genChildItem(key, value, colunm):
    newColumn = 1
    if isinstance(value, dict):
        root, dictColumn = genDictItem(key, value, colunm)
        newColumn += dictColumn
    elif isinstance(value, list):
        root, listColumn = genListItem(key, value, colunm)
        newColumn += listColumn
    elif isinstance(value,str):
        root = QTreeWidgetItem()
        root.setText(colunm, '(str) ' + key)
        newColumn += 1
    elif isinstance(value,bool):
        root = QTreeWidgetItem()
        root.setText(colunm, '(bool) ' + key)
        newColumn += 1
    elif isinstance(value,float):
        root = QTreeWidgetItem()
        root.setText(colunm, '(float) ' + key)
        newColumn += 1
    elif isinstance(value,int):
        root = QTreeWidgetItem()
        root.setText(colunm, '(int) ' + key)
        newColumn += 1
    return root, newColumn


def genTree(treeWidget, data):
    assert isinstance(data, dict)
    treeWidget.header().setSectionResizeMode(QHeaderView.ResizeToContents)
    root = QTreeWidgetItem(treeWidget)
    column = 0
    root.setText(column, "JSON")
    root.setExpanded(True)
    keys = list(data.keys())
    keys.sort()
    counts = []
    column += 1
    for key in keys:
        child, count = genChildItem(key, data[key], column)
        counts.append(count)
        root.addChild(child)
    maxCount = max(counts) + 1
    treeWidget.setColumnCount(maxCount)
    for i in range(1,maxCount):
        treeWidget.setColumnWidth(i, 200)

def genListItem(key, value, startColumn):
    newColumn = 2
    newColumns = []
    root = QTreeWidgetItem()
    root.setText(startColumn, '[] ' + key)
    index = 0

    if value:
        v = value[0]
        if isinstance(v, str):
            child = QTreeWidgetItem()
            child.setText(startColumn + 1, '(str)')
            root.addChild(child)
            newColumn += 1
        elif isinstance(v, bool):
            child = QTreeWidgetItem()
            child.setText(startColumn + 1, '(bool)')
            root.addChild(child)
            newColumn += 1
        elif isinstance(v, float):
            child = QTreeWidgetItem()
            child.setText(startColumn + 1, '(float)')
            root.addChild(child)
            newColumn += 1
        elif isinstance(v, int):
            child = QTreeWidgetItem()
            child.setText(startColumn + 1, '(int)')
            root.addChild(child)
            newColumn += 1
        elif isinstance(v, list):
            child, listColumn = genListItem('[]')
            newColumn += listColumn
            root.addChild(child)
        elif isinstance(v, dict):
            child, dictColumn = genDictItem('item', v, startColumn + 1)
            newColumn += dictColumn
            root.addChild(child)
    else:
        root.addChild(QTreeWidgetItem().setText(startColumn, '(null)'))
    return root, newColumn