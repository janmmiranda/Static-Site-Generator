class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
        
    def props_to_html(self):
        if self.props == None:
            return ""
        items = self.props.items()
        res = []
        for item in items:
            res.append(f"{item[0]}=\"{item[1]}\"")
        return " " + " ".join(res)


    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, children=None, props=None):
        super().__init__(tag, value, children, props)

    def to_html(self):
        if self.value is None:
            raise ValueError(f"No value set on LeafNode")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"