
def getFiles(monitor):
	filesList=[]

	for x in monitor:
		if os.path.isdir(x['path']):
			if x['recursive']:
				filesList.extend([os.path.join(root, f) for (root, dirs, files) in os.walk(x['path']) for f in files])
			else:
				filesList.extend([item for item in os.listdir(x['path']) if os.path.isfile(item)])
		elif os.path.isfile(x['path']):
			filesList.append(x['path'])
	return filesList
