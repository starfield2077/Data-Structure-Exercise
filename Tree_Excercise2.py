class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, num):
        idx = num

        if self.parent:
            prefix = '  ' * self.get_level() + "|__"
        else:
            prefix = ''

        print(prefix + self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

def build_location_tree():

    root = TreeNode("Global")

    india = TreeNode("India")
    usa = TreeNode("USA")

    gujarat = TreeNode('Gujarat')
    karnakata = TreeNode('Karnakata')

    india.add_child(gujarat)
    india.add_child(karnakata)

    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))
    karnakata.add_child(TreeNode("Bangluru"))
    karnakata.add_child(TreeNode("Mysore"))

    princeton = TreeNode("Princeton")
    trenton = TreeNode("Trenton")
    san_francisco = TreeNode("San Francisco")
    mountain_view = TreeNode("Mountain View")
    palo_alto = TreeNode("Palo Alto")

    new_jersey = TreeNode("New Jersey")
    california = TreeNode("California")

    new_jersey.add_child(princeton)
    new_jersey.add_child(trenton)

    california.add_child(san_francisco)
    california.add_child(mountain_view)
    california.add_child(palo_alto)

    usa.add_child(new_jersey)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    return root

if __name__ == '__main__':
    root = build_location_tree()
    root.print_tree()
