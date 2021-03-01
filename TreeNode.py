class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_children(self):
        print(self.data)
        if self.children:
            for child in self.children:
                prefix = '|__' + child.data
                print(prefix)
        else:
            print('|__ is a leave')

    def print_tree(self):
        spaces = ' ' * self.get_level()
        prefix = spaces + '|__' if self.parent else ''
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

if __name__ == '__main__':
    root = TreeNode('Electronics')

    leave_test = TreeNode('Samsung')

    laptop = TreeNode('Laptop')
    laptop.add_child(TreeNode('Mac'))
    laptop.add_child(TreeNode('Surface'))
    laptop.add_child(TreeNode('Thinkpad'))
    laptop.add_child(leave_test)

    cellphone = TreeNode('Cell Phone')
    cellphone.add_child(TreeNode('iPhone'))
    cellphone.add_child(TreeNode('Google Pixel'))
    cellphone.add_child(TreeNode('Xiaomi'))

    tv = TreeNode('TV')
    tv.add_child(leave_test)
    tv.add_child(TreeNode('LG'))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    laptop.print_children()
    leave_test.print_children()
