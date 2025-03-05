import json

def create_img(img):
    if (img == ""): return ""
    return f"<img src=\"{img}\" alt=\"isolated\" width=\"40\"/>"


# open a json object
data = []
with open('data.json') as f:
	data = json.load(f)
 
# open a json object 2
patterns = []
with open('patterns.json') as f:
	patterns = json.load(f)
 
file = open('leetcode.md', 'w')
 
print("# LeetCode Badges", file=file)
print("## What is Leetcode?", file=file)
print("**Leetcode** is a great place to learn and practice coding. It has a vast collection of problems that are categorized based on their difficulty level. It also has a great community where you can discuss problems and solutions with other users.", file=file)

print("## Why Leetcode?", file=file)
print("**Leetcode** is a great platform full of interesting problems and resources. It is a great place to learn and practice coding. It has a vast collection of problems that are categorized based on their difficulty level. It also has a great community where you can discuss problems and solutions with other users.", file=file)
print("### Here are some articles that you might find useful:", file=file)
for title, link in patterns:
	print(f"- [{title}]({link})", file=file)

print("## My Profile", file=file)
print("I started working on my **Leetcode** profile as I begun studying. At first I just wanted to recieve a free T-shirt. But as I progressed I realized that it was a great way to track my progress and learn new things. You can find my profile [here](https://leetcode.com/u/Ometek/).", file=file)
print("### Badges", file=file)
print("Name | Date | img | Name | Date | img", file=file)
print("--- | --- | --- | --- | --- | ---", file=file)

data.append(dict({"Badge Name": "", "Date": "", "img": ""}))

for i in range(len(data) // 2):
	print(data[i * 2]["Badge Name"], "|", data[i * 2]["Date"], "|", create_img(data[2 * i]["img"]), "|", file=file, end="")
	print(data[i * 2 + 1]["Badge Name"], "|", data[i * 2 + 1]["Date"], "|", create_img(data[2 * i + 1]["img"]), file=file)
    
file.close()