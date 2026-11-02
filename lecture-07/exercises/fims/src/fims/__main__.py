
def main():
   helpers.hello(TITLE)

   files={}
    
   while True:
      for file in monit.getFiles(monitor):
         hash = hashlib.sha256()

         with open(file) as f:
            for chunk in iter(lambda: f.read(2048), ""):
               hash.update(chunk.encode("utf-8"))
               sha256 = hash.hexdigest()

               if file in files and sha256 != files[file]:
                  print(f'{file} has been changed! {time.strftime("%Y-%m-%d %H:%M:%S")}')
                  
               files[file]=sha256
               with shelve.open(DATABASE) as s:
                  s[file] = files[file]

            time.sleep(1)

if __name__ == "__main__":
   try:
      main()
   except KeyboardInterrupt:
      helpers.bye(TITLE)
