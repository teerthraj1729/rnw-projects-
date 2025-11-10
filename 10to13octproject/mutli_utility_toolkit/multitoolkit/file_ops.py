from pathlib import Path

BASE_DIR = Path.cwd()

def create_file(filename: str):
    p = BASE_DIR / filename
    p.touch(exist_ok=True)
    return str(p)

def write_file(filename: str, data: str):
    p = BASE_DIR / filename
    with p.open("w",encoding="utf-8")as f:
        f.write(data)
    return True

def read_file(filename: str)->str:
    file_path = Path(filename)   
    if not file_path.exists():    
        raise FileNotFoundError(f"File '{filename}' does not exist!")
    with open(file_path, "r") as f:
        return f.read()
   
def append_file(filename: str, data: str):
    p = BASE_DIR / filename
    with p.open("a",encoding="utf-8")as f:
        f.write(data)
    return True 
    
