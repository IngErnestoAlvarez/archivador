from pathlib import Path
def makeToString(var):
    if not isinstance(var, str):
        return var.get()
    else:
        return var

def makeToPath(var):
    if not isinstance(var, Path):
        p = Path(var)
    else:
        p = var
    return p
