class TreeNode:
    def __init__(self, name, designation):
        self.data = [name, designation]
        self.children = []
        self.parent = None
        self.mode = ''

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, mode):
        self.mode = mode
        if self.mode == "name":
            res = self.data[0]
        elif self.mode == "designation":
            res = self.data[1]
        elif self.mode == "both":
            res = self.data[0] + ' (' + self.data[1] + ')'
        else:
            return

        if self.parent:
            prefix = '  ' * self.get_level() + "|__"
        else:
            prefix = ''

        print(prefix + res)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree(mode)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level


def build_product_tree():

    root = TreeNode("Nilupul", "CEO")

    cto = TreeNode("Chinmay", "CTO")
    hr_head = TreeNode("Gels", "HR Head")

    infrastructure_head = TreeNode("Vishwa", "Infrastructure Head")
    application_head = TreeNode("Aamir", "Application Head")
    recruitment_manager = TreeNode("Peter", "Recruitment Manager")
    policy_manager = TreeNode("Waqas", "Policy Manager")

    cloud_manager = TreeNode("Dhaval", "Cloud Manager")
    app_manager = TreeNode("Abhijit", "App Manager")

    cto.add_child(infrastructure_head)
    cto.add_child(application_head)

    hr_head.add_child(recruitment_manager)
    hr_head.add_child(policy_manager)

    infrastructure_head.add_child(cloud_manager)
    infrastructure_head.add_child(app_manager)

    root.add_child(cto)
    root.add_child(hr_head)

    return root


if __name__ == '__main__':
    root_node = build_product_tree()
    root_node.print_tree("name")  # prints only name hierarchy
    root_node.print_tree("designation")  # prints only designation hierarchy
    root_node.print_tree("both")  # prints both (name and designation) hierarchy
