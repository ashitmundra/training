def empty_folder():
	import os
	path=ask_path()
	final_path=path+"/*"
	confirm=ask_name()
	if (confirm=="yes") or (confirm=="ya") or (confirm=="yup") or (confirm=="sure"):
		os.system("rm -r "+final_path)
print("hi")
print("team2")
