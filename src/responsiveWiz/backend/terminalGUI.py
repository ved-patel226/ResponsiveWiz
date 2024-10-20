import subprocess

def run_responsive_wiz(url: str, level: int, animation: bool, hide_output: bool):
    command = ['python', 'src/responsiveWiz/backend/scraping.py', '--url', url, '--level', str(level)]
    if animation:
        command.append('--animation-experimental')
    if hide_output:
        command.append('--hide-output')
    
    subprocess.run(command)
    
url = input("Enter the URL: ")
level = int(input("Enter the level: \n0 - 10 Dimensions Checked\n1 - 20 Dimensions Checked\n2 - 30 Dimensions Checked: "))
assert level in [0, 1, 2], "Invalid level"
animation = input("Disable animations? (y/n): ").lower() == 'y'
hide_output = input("Hide output? (y/n): ").lower() == 'y'

run_responsive_wiz(url, level, animation, hide_output)
