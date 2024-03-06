## hey one 

(use "git add <file>..." to include in what will be committed)      
PS D:\Projects\DS> git init
Reinitialized existing Git repository in D:/Projects/DS/.git/
PS D:\Projects\DS> git add README.md
PS D:\Projects\DS> git commit -m "first commit" 
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        venv/

nothing added to commit but untracked files present (use "git add" to track)
PS D:\Projects\DS> conda activate venv/                               
PS D:\Projects\DS> git commit -m "first commit"
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)      
        venv/

nothing added to commit but untracked files present (use "git add" to track)
PS D:\Projects\DS> git branch -M.main
fatal: '.main' is not a valid branch name
PS D:\Projects\DS> git branch -M main
PS D:\Projects\DS> git remote add origin https://github.com/VaishnaviKanade/DSProject.git
PS D:\Projects\DS> git remote -v
origin  https://github.com/VaishnaviKanade/DSProject.git (fetch)      
origin  https://github.com/VaishnaviKanade/DSProject.git (push)       
PS D:\Projects\DS> git push -u origin main
info: please complete authentication in your browser...
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 218 bytes | 218.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/VaishnaviKanade/DSProject.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
PS D:\Projects\DS> git pull
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 2.35 KiB | 300.00 KiB/s, done.
From https://github.com/VaishnaviKanade/DSProject
   89c22db..7aac16d  main       -> origin/main
Updating 89c22db..7aac16d
Fast-forward
 .gitignore | 160 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 160 insertions(+)
 create mode 100644 .gitignore
PS D:\Projects\DS>
