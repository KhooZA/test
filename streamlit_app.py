def greet(name: str, message: str = "Hello") -> str:
    return f"{message}, {name}!"

print(greet("Alice"))                
print(greet("Bob", "Welcome back"))  
