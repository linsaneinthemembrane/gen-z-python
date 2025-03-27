"""
My grand vision for this is to redesign how we thing of Python, making it easier for the new generation to learn

Below is an example of the new code

icl This is a comment
istg math

pmo add_numbers(a, b):
    sybau a + b

srs x > 10:
    ijbol("x is greater than 10")

ts i in range(5):
    ijbol(i)

it's simply a translation of this:

# This is a comment
import math

def add_numbers(a, b):
    return a + b

if x > 10:
    print("x is greater than 10")

for i in range(5):
    print(i)
"""

# Define the replacements dictionary at the module level
replacements = {
    "pmo": "def",
    "ts": "for",
    "bffr": "assert",
    "flop": "raise Exception",
    "istg": "import",
    "ijbol": "print",
    "sybau": "return",
    "ngl": "True",
    "srs": "if",
    "sm": "while",
    "rn": "now",
    "icl": "#"
}

def gen_z_to_python(code):
    # Process the code line by line to preserve structure
    result_lines = []
    lines = code.split('\n')
    
    for line in lines:
        # Preserve leading whitespace
        leading_space = len(line) - len(line.lstrip())
        processed_line = line[:leading_space]
        
        # Process the non-whitespace part
        remaining = line[leading_space:]
        
        # Split by spaces but preserve strings and other elements
        import re
        tokens = re.findall(r'["\'].*?["\']|\S+', remaining)
        
        for token in tokens:
            # Don't replace tokens inside quotes
            if (token.startswith('"') and token.endswith('"')) or \
               (token.startswith("'") and token.endswith("'")):
                processed_line += token + " "
            elif token in replacements:
                processed_line += replacements[token] + " "
            else:
                processed_line += token + " "
        
        result_lines.append(processed_line.rstrip())
    
    return "\n".join(result_lines)

def run_gen_z_python(code):
    python_code = gen_z_to_python(code)
    
    # Create a namespace with Python builtins
    namespace = {'__builtins__': __builtins__}
    
    # Map all function-like Gen Z terms to their Python equivalents
    function_mappings = {
        "ijbol": print,  # Map ijbol to print
        "flop": lambda msg: raise_exception(msg),  # Map flop to raise
        # Add any other function-like mappings here
    }
    
    # Helper function for flop (raise)
    def raise_exception(msg):
        raise Exception(msg)
    
    # Add the function mappings to the namespace
    for gen_z_term, python_func in function_mappings.items():
        namespace[gen_z_term] = python_func
    
    # Add True/False constants if needed
    namespace["ngl"] = True
    
    # Execute the transpiled code with our custom namespace
    exec(python_code, namespace)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python gen_z_python.py <filename.gzpy>")
        sys.exit(1)
    
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            gen_z_code = file.read()
        
        python_code = gen_z_to_python(gen_z_code)
        print("Transpiled Python code:")
        print(python_code)
        print("\nRunning the code:")
        run_gen_z_python(gen_z_code)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except Exception as e:
        print(f"Error: {e}")
