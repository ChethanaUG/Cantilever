## Project Summary
This repository contains evidence of a phishing page simulation as part of the Cantilever internship, showcasing ethical security testing and awareness using Zphisher on localhost.

> ℹ️ Disclaimer  
This project uses the open-source tool [Zphisher](https://github.com/htr-tech/zphisher), which was cloned and executed locally as per company guidelines.  
I do not claim authorship of Zphisher. My contribution is running the tool, testing it with dummy data, and documenting the process with screenshots for educational purposes.

# Phishing Page Simulation — Evidence & Plan

**Purpose:** Evidence of running Zphisher for an educational exercise. Only dummy credentials were used.

> ⚠️ Ethical & Legal Notice  
> This repository and any included demos are strictly for learning and testing in a controlled environment. Only dummy/test credentials were used. Do **NOT** use these techniques on real users or systems.

---

## What is in this folder
- `evidence/` — screenshots showing the steps I ran (personal info blurred).  
- `phishing-demo/` — small educational demo (index.html + save.php) demonstrating local credential capture (dummy-only).

---

## Local URL used (safe to show)
Local test URL used: `http://127.0.0.1:8080` (loopback/localhost — not accessible from the internet).

---

## How I ran the tool (commands used locally)
```bash
git clone https://github.com/htr-tech/zphisher.git
cd zphisher
chmod +x zphisher.sh
bash zphisher.sh
```

## Evidence (screenshots)

All screenshots are in the `phishing-simulation/evidence/` folder.

1. `01_clone.png` — **Cloning the Repository**  
   Screenshot: `git clone https://github.com/htr-tech/zphisher.git` (Shows the project being cloned successfully).

2. `02_cd.png` — **Navigating to the Project Directory**  
   Screenshot: `cd zphisher` (Shows entering the Zphisher folder after cloning).

3. `03_chmod.png` — **Setting Script Permissions**  
   Screenshot: `chmod +x zphisher.sh` (Displays permission being set for Zphisher launch script).

4. `04_menu.png` — **Launching Zphisher and Selecting a Phishing Template**  
   Screenshot: Zphisher main menu with attack options (shows interactive menu for choosing which site to simulate).

5. `05_select_template.png` — **Selecting Phishing Template**  
   Screenshot: selection of a specific site (e.g., Instagram) and page type (Traditional, Auto Followers, etc.).

6. `06_port_service.png` — **Configuring Port Forwarding Service**  
   Screenshot: selection of port forwarding method (Localhost, Cloudflared, LocalXpose).

7. `07_custom_port.png` — **Custom Port Selection**  
   Screenshot: prompt for setting a custom port (e.g., `Do You Want A Custom Port [y/N]:`).

8. `08_hosting_start.png` — **Starting the Phishing Simulation**  
   Screenshot: confirmation of successful local hosting and readiness to capture login information (e.g., `Successfully Hosted at: http://127.0.0.1:8080` and `Waiting for Login Info`).

9. `09_open_browser.png` — **Opening the Phishing Page in Browser**  
   Screenshot: launching the phishing page in an incognito tab at `http://127.0.0.1:8080` (local test).

10. `10_phishing_page.png` — **Viewing the Phishing Login Page**  
    Screenshot: fake Instagram followers login page showing username and password fields.

11. `11_submit_creds.png` — **Submitting Fake Credentials**  
    Screenshot: simulated victim entering `testuser123` / `password123` and clicking submit (dummy creds).

12. `12_captured_terminal.png` — **Captured Credentials and Session Details in Terminal**  
    Screenshot: Zphisher terminal output showing victim IP, captured credentials (dummy), and file save locations.

**Privacy note:** All personal/host names in screenshots are blurred. Only dummy credentials were used. Do not commit `creds.txt`, `usernames.txt`, `ip.txt` or any real credentials.
Note: Personal info/hostnames in screenshots have been blurred for privacy.
