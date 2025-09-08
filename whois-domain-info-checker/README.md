WHOIS DOMAIN INFO CHECKER

This project is part of my Cantilever internship.  
It allows users to fetch WHOIS information for one or more domains and automatically saves the results into a CSV file.

## INSTALLATION:
1. Clone the repository:
   ```bash
   git clone https://github.com/ChethanaUG/Cantilever.git
   cd cantilever/whois-domain-info-checker
   ```
   
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On macOS/Linux
   ```
   ```bash
   python3 -m venv venv
   venv\Scripts\activate      # On Windows
   ```

3. Install required package:
   ```bash
   pip install python-whois
   ```

## USAGE:
 Run the script:
 ```bash
 python3 whois_checker.py
 ```
 When prompted, enter domain names one by one.
 Type done (or press Enter without typing anything) to finish and save results.

Example session:
```
 Please enter domain names one at a time. Type 'done' to finish and save the results.
 Enter domain name (or 'done' to finish): amazon.com
 Enter domain name (or 'done' to finish): google.com
 Enter domain name (or 'done' to finish): done
 ✅ All domain info saved successfully to 'domain_info.csv'.
```

## OUTPUT:
 The results are saved in a file named domain_info.csv with fields:
 - Domain Registrar
 - Creation Date
 - Expiry Date
 - Last Updated
 - Registrant Country

Example row in the CSV:
 ```sql
 Domain,Registrar,Creation Date,Expiry Date,Last Updated,Registrant Country
 amazon.com,MarkMonitor Inc.,1994-11-01,2030-11-01,2024-11-01,US
 ```
