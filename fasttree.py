import subprocess

class fasttree:
    def __init__(self, file, tool_speed, tool_model, tool_expand_chars):
        self.file = file
        self.tool_speed = tool_speed
        self.tool_model = tool_model
        self.tool_expand_chars = tool_expand_chars
    def __str__(self):
        