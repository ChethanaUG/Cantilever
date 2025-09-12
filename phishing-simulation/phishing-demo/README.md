## Phishing-demo 

**Author:** Chethana UG  
**Date:** 2025-09-12

### What I created
I wrote a small, local educational demo to show how a phishing form can send credentials to a server-side script and how those credentials can be stored locally (for demonstration only). The files were created by me and tested on my local machine.

Files:
- `phishing-simulation/phishing-demo/index.html` — simple HTML login form (dummy only).  
- `phishing-simulation/phishing-demo/save.php` — PHP script that saves submitted inputs to a local file (timestamped), eg. `creds_YYYYMMDD.txt`.

### How it works:
1. Place both files in the same folder: `phishing-simulation/phishing-demo/` on your machine. 

Open Terminal and run:
```
 cd ~/Desktop/phishing-demo   #if phishing-demo folder is on your Desktop.
```
3. Start PHP built-in server from that folder:
```
php -S 127.0.0.1:8080
```
3. Open browser and visit:
http://127.0.0.1:8080/index.html
4. Enter dummy credentials (example: `testuser123` / `password123`) and submit.  
5. Check the demo folder for the created file `creds_YYYYMMDD.txt` to see the saved dummy entry.

### Expected outputs
- Browser shows a confirmation message after submitting (e.g., `✅ Thanks! (demo only)`).  
- A local file `creds_YYYYMMDD.txt` appears in the demo folder containing timestamped dummy credential entries.

### Safety & ethics
- I wrote these demo files myself for learning and testing.  
- Only **dummy/test credentials** were used.  
- **Do not** run this demo against real users or expose it publicly.  
- `creds_*.txt` and any credential files are listed in `.gitignore` and must not be committed to the repository.

**Commit message suggestion when adding demo files:**  
`Add phishing-demo (created by Chethana UG) — index.html and save.php`
