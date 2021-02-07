class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        folders = path.split("/")[1:]
                    
        for folder in folders:
            if folder != "..":
                if folder != "." and folder != "":
                    stack.append(folder)
            else:
                if stack != []:
                    stack.pop()
                
        return "/" + "/".join(stack)