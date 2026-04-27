import json
import os

class ReflectionAgent:
    def __init__(self, tree_path):
        with open(tree_path, 'r') as f:
            self.nodes = {node['id']: node for node in json.load(f)}
        self.state = {
            "answers": {},
            "signals": {"axis1": {"internal": 0, "external": 0}, 
                        "axis2": {"contribution": 0, "entitlement": 0},
                        "axis3": {"self": 0, "altro": 0}}
        }

    def run(self):
        current_id = "START"
        while current_id:
            node = self.nodes.get(current_id)
            if not node: break

            # Process Signals
            if node['signal']:
                axis, value = node['signal'].split(':')
                self.state['signals'][axis][value] += 1

            # Handle Node Types
            if node['type'] in ['start', 'bridge', 'reflection']:
                print(f"\n[SYSTEM]: {node['text']}")
                input("--- Press Enter to continue ---")
                current_id = self.get_next_id(node)

            elif node['type'] == 'question':
                print(f"\n[QUESTION]: {node['text']}")
                options = node['options'].split('|')
                for i, opt in enumerate(options, 1):
                    print(f"{i}. {opt}")
                
                choice = int(input("\nSelect an option (number): ")) - 1
                selected_text = options[choice]
                self.state['answers'][node['id']] = selected_text
                current_id = self.get_next_id(node)

            elif node['type'] == 'decision':
                current_id = self.evaluate_decision(node)

            elif node['type'] == 'summary':
                summary_text = self.generate_summary(node['text'])
                print(f"\n*** FINAL REFLECTION ***\n{summary_text}")
                current_id = self.get_next_id(node)

            elif node['type'] == 'end':
                print(f"\n[FINISH]: {node['text']}")
                break

    def get_next_id(self, node):
        if node['target']: return node['target']
        # Default: find the node that lists this node as parent
        for next_node in self.nodes.values():
            if next_node['parentId'] == node['id']: return next_node['id']
        return None

    def evaluate_decision(self, node):
        rules = node['options'].split(';')
        last_answer = list(self.state['answers'].values())[-1]
        for rule in rules:
            condition, target = rule.split(':')
            possible_answers = condition.split('=')[1].split('|')
            if last_answer in possible_answers:
                return target
        return None

    def generate_summary(self, template):
        # Calculate dominant poles
        def get_dominant(axis):
            vals = self.state['signals'][axis]
            return max(vals, key=vals.get)

        summary = template.replace("{axis1.dominant}", get_dominant("axis1"))
        summary = summary.replace("{axis2.dominant}", get_dominant("axis2"))
        summary = summary.replace("{axis3.dominant}", get_dominant("axis3"))
        return summary

if __name__ == "__main__":
    # Path point to your JSON file
    tree_file = os.path.join("..", "tree", "reflection-tree.json")
    agent = ReflectionAgent(tree_file)
    agent.run()
