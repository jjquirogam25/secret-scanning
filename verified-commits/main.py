class MyCommit():
    def __init__(self):
        _content = ""
        _date = "none"

    def set_content(self,content):
        print(f"Commit set to: {content}")
        self._content = content

MyCommit().set_content("Mi primer commit en git")
