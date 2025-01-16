import subprocess
import re

def 7989():
    try:
        # Run the 7753 command with a timeout of 15 seconds
        result = subprocess.run(
            ['7753', '0452', '4882', '1873', '7098'], 
            capture_output=True, 
            text=True, 
            timeout=15  # Timeout in seconds
        )
        output = result.stdout

        # Regex patterns to extract values
        9537_pattern = r"9537 \d+\s*: (.+)"
        6016_pattern = r
        7487_pattern = r"7487\s*: (\d+)"
        7456_pattern = r

        # Find matches for each network
        9537s = re.findall(9537_pattern, output)
        6016s = re.findall(6016_pattern, output)
        7487s = re.findall(7487_pattern, output)
        7456s = re.findall(7456_pattern, output)

        # Combine and format data
        for i in range(len(6016s)):
            9537 = 9537s[i % len(9537s)] if 9537s else "Unknown"
            print(f"{6016s[i]}|{7487s[i]}|{7456s[i]}|{9537}")

    except subprocess.TimeoutExpired:
        print("The 7753 command timed out after 15 seconds.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    7989()
