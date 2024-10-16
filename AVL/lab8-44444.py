class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"Node({self.data})"

    @staticmethod
    def height(node):
        if node is None:
            return -1
        return max(Node.height(node.left), Node.height(node.right)) + 1

    def balance(self):
        return Node.height(self.left) - Node.height(self.right)

    def leftRotate(self):
        y = self.right
        T = y.left
        y.left = self
        self.right = T
        return y

    def rightRotate(self):
        x = self.left
        T = x.right
        x.right = self
        self.left = T
        return x

    @staticmethod
    def insert(root, data):
        if root is None:
            return Node(data)
        branch = "left" if data < root.data else "right"
        root.__dict__[branch] = Node.insert(root.__dict__[branch], data)

        balance = root.balance()

        if balance > 1 and root.left.balance() >= 0:            
            return root.rightRotate()

        if balance > 1 and root.left.balance() < 0:       
            root.left = root.left.leftRotate()
            return root.rightRotate()

        if balance < -1 and root.right.balance() <= 0:
            return root.leftRotate()

        if balance < -1 and root.right.balance() > 0:
            root.right = root.right.rightRotate()
            return root.leftRotate()
        
        return root

    def _gen_display(self) -> 'tuple[list, int, int, int]':
        '''
        return
        - tree image: list[str]
        - left spacing: int
        - value width: int
        - right spacing: int
        '''
        if self is None:
            return [], 0, 0, 0
        lt, lf, lv, lb = Node._gen_display(self.left)
        rt, rf, rv, rb = Node._gen_display(self.right)
        data = str(self.data)
        if not lt and not rt:
            return [data], 0, len(data), 0
        add_left, add_right = int(bool(lt)), int(bool(rt))
        line = ((' '*(lf+lv) + '/' + ' '*(lb)) * add_left +
                ' ' * len(data) +
                (' '*rf + '\\' + ' '*(rv+rb)) * add_right)
        out = [' '*(lf+lv+add_left) + '_'*lb + data +
               '_'*rf + ' '*(rv+rb+add_right), line]
        if len(lt) > len(rt):
            rt.extend([' ' * (rf+rv+rb)] * (len(lt) - len(rt)))
        elif len(lt) < len(rt):
            lt.extend([' ' * (lf+lv+lb)] * (len(rt) - len(lt)))
        for l, r in zip(lt, rt):
            out.append(l + ' '*(len(data)+add_left+add_right) + r)
        return out, (lf+lv+lb+add_left), len(data), (rf+rv+rb+add_right)

    @staticmethod
    def collect_subtree_values(node, values):
        if node is None:
            return
        Node.collect_subtree_values(node.left, values)
        Node.collect_subtree_values(node.right, values)
        values.append(node.data)

    @staticmethod
    def rebar(root, val, direction):
        temp = root
        while temp is not None and temp.data != val:
            if val < temp.data:
                temp = temp.left
            elif val > temp.data:
                temp = temp.right

        if temp is None:
            print(f"No {val} in this tree")
            return 1

        values = []
        Node.collect_subtree_values(temp, values)
        
        if direction == "left":
            values.sort(reverse=True)  
        elif direction == "right":
            values.sort() 
        
        new_tree = Node(values[0])
        current_node = new_tree
        for v in values[1:]:
            if direction == "left":
                current_node.left = Node(v)
                current_node = current_node.left
            else:
                current_node.right = Node(v)
                current_node = current_node.right

        temp.data = new_tree.data
        temp.left = new_tree.left if direction == "left" else None
        temp.right = new_tree.right if direction == "right" else None

        return None


rotate, direction, inp = input('Enter input: ').split(',')
rotate = int(rotate)
root = None
for i in map(int, inp.split()):
    root = Node.insert(root, int(i))

tree_image = root._gen_display()
print("Before")
print(*tree_image[0], sep='\n')
print("-" * sum(tree_image[1:]))

if not Node.rebar(root, rotate, direction):
    print("After")
    tree_image = root._gen_display()
    print(*tree_image[0], sep='\n')
