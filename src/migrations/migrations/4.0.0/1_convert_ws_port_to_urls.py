#!/usr/bin/env python3
import os
import ast

SNAP_DATA = os.environ.get("SNAP_DATA")
CONFIGURE_PATH = f"{SNAP_DATA}/configuration.py"

if not os.path.isfile(CONFIGURE_PATH):
    sys.exit(0)

with open(CONFIGURE_PATH, "r") as f:
    content = f.read()

# Parse AST to safely find configuration
class ConfigVisitor(ast.NodeVisitor):
    def __init__(self):
        self.ws_port = None
        self.ws_urls = False

    def visit_Assign(self, node):
        if isinstance(node.targets[0], ast.Name):
            if node.targets[0].id == "WS_PORT":
                self.ws_port = ast.literal_eval(node.value)
            elif node.targets[0].id == "WS_URLS":
                self.ws_urls = True

visitor = ConfigVisitor()
visitor.visit(ast.parse(content))

# Migrate if needed
if visitor.ws_port and not visitor.ws_urls:
    new_content = content.replace(
        "WS_PORT =",
        f"WS_URLS = [{visitor.ws_port}]  # Migrated from WS_PORT\n# WS_PORT ="
    )

    with open(CONFIGURE_PATH, "w") as f:
        f.write(new_content)
