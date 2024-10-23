def simplifyPath(self, path: str) -> str:
    res = []
    lst = path.split('/')
    for itm in lst:
        if itm == '.':
            pass
        elif itm == '..':
            if res:
                res.pop()
        elif itm:
            res.append(itm)
    return '/'+'/'.join(res)