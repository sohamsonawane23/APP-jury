import tkinter as tk
from tkinter import ttk, messagebox
import random


class Node:
    """A node in the Binary Search Tree."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.x = 0
        self.y = 0


class BinarySearchTree:
    """A class to handle the BST logic."""

    def __init__(self):
        self.root = None
        self.nodes_to_draw = []

    def insert(self, value):
        """Inserts a new value into the BST."""
        if not isinstance(value, int):
            return False, "Please enter a valid number."
        if self.search(value):
            return False, f"Value {value} already exists."

        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True, f"Value {value} inserted successfully."

        current_node = self.root
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    break
                current_node = current_node.left
            else:  # value > current_node.value
                if current_node.right is None:
                    current_node.right = new_node
                    break
                current_node = current_node.right
        return True, f"Value {value} inserted successfully."

    def search(self, value):
        """Searches for a value and returns the node if found, otherwise None."""
        if not isinstance(value, int):
            return None
        current_node = self.root
        while current_node is not None:
            if value == current_node.value:
                return current_node
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None

    def delete(self, value):
        """Deletes a node from the BST."""
        if not isinstance(value, int):
            return False, "Please enter a valid number."

        self.root, deleted = self._delete_recursive(self.root, value)
        if deleted:
            return True, f"Value {value} deleted successfully."
        else:
            return False, f"Value {value} not found. Cannot delete."

    def _delete_recursive(self, node, value):
        """Recursive helper function for deletion."""
        if node is None:
            return None, False

        if value < node.value:
            node.left, deleted = self._delete_recursive(node.left, value)
            return node, deleted
        elif value > node.value:
            node.right, deleted = self._delete_recursive(node.right, value)
            return node, deleted
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right, True
            elif node.right is None:
                return node.left, True

            # Node with two children: find the inorder successor (min value in the right subtree)
            successor = self._find_min_node(node.right)
            node.value = successor.value
            # Delete the inorder successor
            node.right, _ = self._delete_recursive(node.right, successor.value)
            return node, True

    def _find_min_node(self, node):
        """Helper to find the node with the minimum value in a subtree."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    # --- Traversal Methods ---
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

    # --- Visualization Logic ---
    def _layout(self, node, x, y, level):
        """Recursively sets the x,y coordinates for each node."""
        if not node:
            return

        offset_x = 100 * (0.5 ** (level - 1))

        node.x = x
        node.y = y
        self.nodes_to_draw.append(node)

        self._layout(node.left, x - offset_x, y + 60, level + 1)
        self._layout(node.right, x + offset_x, y + 60, level + 1)

    def update_positions(self):
        """Calculates the positions for all nodes for drawing."""
        self.nodes_to_draw = []
        if self.root:
            self._layout(self.root, 400, 50, 1)


class BSTVisualizerApp:
    """The main Tkinter application."""

    def __init__(self, root):
        self.root = root
        self.root.title("Python BST Visualizer")
        self.bst = BinarySearchTree()
        self.canvas = tk.Canvas(root, width=800, height=500, bg="#2D3748")
        self.canvas.pack(pady=10)
        self.setup_ui()
        self.animation_step = 0
        self.animation_path = []
        self.message_label = None
        self.traversal_label = None

    def setup_ui(self):
        """Sets up the control buttons and input fields."""
        control_frame = ttk.Frame(self.root)
        control_frame.pack(pady=10)

        # Insert controls
        ttk.Label(control_frame, text="Value:").pack(side=tk.LEFT, padx=5)
        self.insert_entry = ttk.Entry(control_frame, width=10)
        self.insert_entry.pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Insert", command=self.handle_insert).pack(side=tk.LEFT)

        # Search controls
        self.search_entry = ttk.Entry(control_frame, width=10)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Search", command=self.handle_search).pack(side=tk.LEFT)

        # Delete controls
        self.delete_entry = ttk.Entry(control_frame, width=10)
        self.delete_entry.pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Delete", command=self.handle_delete).pack(side=tk.LEFT)

        # Traversal and Random Tree
        traversal_frame = ttk.Frame(self.root)
        traversal_frame.pack(pady=5)
        ttk.Button(traversal_frame, text="Inorder", command=self.handle_inorder).pack(side=tk.LEFT, padx=5)
        ttk.Button(traversal_frame, text="Preorder", command=self.handle_preorder).pack(side=tk.LEFT, padx=5)
        ttk.Button(traversal_frame, text="Postorder", command=self.handle_postorder).pack(side=tk.LEFT, padx=5)
        ttk.Button(traversal_frame, text="Random Tree", command=self.handle_random).pack(side=tk.LEFT, padx=10)

        # Status messages
        self.message_label = ttk.Label(self.root, text="Ready for your commands!", font=('Helvetica', 10),
                                       foreground="#6EE7B7")
        self.message_label.pack(pady=5)

        traversal_title = ttk.Label(self.root, text="Traversal Result:", font=('Helvetica', 10, 'bold'),
                                    foreground="#E2E8F0")
        traversal_title.pack()
        self.traversal_label = ttk.Label(self.root, text="None", font=('Helvetica', 10), foreground="#E2E8F0")
        self.traversal_label.pack(pady=(0, 10))

        # Initial drawing
        self.draw_tree()

    def handle_insert(self):
        try:
            value = int(self.insert_entry.get())
            success, message = self.bst.insert(value)
            self.show_message(message, success)
            self.draw_tree()
        except ValueError:
            self.show_message("Please enter a valid number.", False)

    def handle_search(self):
        try:
            value = int(self.search_entry.get())
            self.animation_path = []
            self.find_path_to_node(self.bst.root, value)
            if self.animation_path:
                self.animate_path(self.animation_path, 0, f"Searching for {value}...")
            else:
                self.show_message(f"Value {value} not found.", False)
        except ValueError:
            self.show_message("Please enter a valid number.", False)

    def handle_delete(self):
        try:
            value = int(self.delete_entry.get())
            success, message = self.bst.delete(value)
            self.show_message(message, success)
            self.draw_tree()
        except ValueError:
            self.show_message("Please enter a valid number.", False)

    def handle_inorder(self):
        self.animate_traversal(self.bst.inorder_traversal(), "Inorder Traversal:")

    def handle_preorder(self):
        self.animate_traversal(self.bst.preorder_traversal(), "Preorder Traversal:")

    def handle_postorder(self):
        self.animate_traversal(self.bst.postorder_traversal(), "Postorder Traversal:")

    def handle_random(self):
        self.bst.root = None
        values = random.sample(range(1, 100), k=random.randint(5, 12))
        for value in values:
            self.bst.insert(value)
        self.show_message(f"Generated a new tree with {len(values)} random nodes.", True)
        self.draw_tree()
        self.traversal_label.config(text="None")

    def show_message(self, text, is_success):
        color = "#6EE7B7" if is_success else "#FCA5A5"
        self.message_label.config(text=text, foreground=color)

    def draw_tree(self):
        self.canvas.delete("all")
        self.bst.update_positions()

        # Draw lines first
        self._draw_lines(self.bst.root)

        # Draw nodes on top
        for node in self.bst.nodes_to_draw:
            self._draw_node(node)

    def _draw_lines(self, node):
        if not node:
            return
        if node.left:
            self.canvas.create_line(node.x, node.y, node.left.x, node.left.y, fill="#A0AEC0", width=2)
            self._draw_lines(node.left)
        if node.right:
            self.canvas.create_line(node.x, node.y, node.right.x, node.right.y, fill="#A0AEC0", width=2)
            self._draw_lines(node.right)

    def _draw_node(self, node, highlight=False, fill_color="#4299E1"):
        size = 30
        x, y = node.x, node.y
        if highlight:
            self.canvas.create_oval(x - size, y - size, x + size, y + size, fill=fill_color, outline="white", width=3)
        self.canvas.create_oval(x - size, y - size, x + size, y + size, fill=fill_color, outline="#E2E8F0", width=2)
        self.canvas.create_text(x, y, text=str(node.value), fill="white", font=('Helvetica', 12, 'bold'))

    def find_path_to_node(self, node, value):
        if node is None:
            return
        self.animation_path.append(node)
        if value < node.value:
            self.find_path_to_node(node.left, value)
        elif value > node.value:
            self.find_path_to_node(node.right, value)

    def animate_path(self, path, step, message):
        if step < len(path):
            self.show_message(message, True)
            self.draw_tree()
            current_node = path[step]
            self._draw_node(current_node, highlight=True, fill_color="#38A169" if step == len(path) - 1 else "#F6AD55")
            self.root.after(800, self.animate_path, path, step + 1, message)
        else:
            found = path[-1].value == int(self.search_entry.get())
            self.show_message(f"Value {path[-1].value} was {'found' if found else 'not found'}.", found)

    def animate_traversal(self, result_list, message):
        self.traversal_label.config(text="")
        self.show_message(message, True)
        self.draw_tree()

        def step_traversal(index):
            if index < len(result_list):
                current_value = result_list[index]
                self.traversal_label.config(text=f"{self.traversal_label.cget('text')} {current_value}")

                # Find and highlight the node
                for node in self.bst.nodes_to_draw:
                    if node.value == current_value:
                        self._draw_node(node, highlight=True, fill_color="#F6AD55")
                        break

                self.root.after(500, self.draw_tree)
                self.root.after(1000, step_traversal, index + 1)
            else:
                self.show_message("Traversal complete.", True)

        step_traversal(0)


def main():
    root = tk.Tk()
    app = BSTVisualizerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()