
import whois
import csv
from datetime import datetime

def fetch_domain_details(domain_name):
   
    try:
        domain_data = whois.whois(domain_name)
        return {
            "Domain": domain_name,
            "Registrar": domain_data.registrar if domain_data.registrar else "N/A",
            "Creation Date": format_date_field(domain_data.creation_date),
            "Expiry Date": format_date_field(domain_data.expiration_date),
            "Last Updated": format_date_field(domain_data.updated_date),
            "Registrant Country": domain_data.country if hasattr(domain_data, 'country') else "N/A",
        }
    except Exception as error:
        print(f"Could not retrieve data for {domain_name}: {error}")
        
        return {
            "Domain": domain_name,
            "Registrar": "N/A",
            "Creation Date": "N/A",
            "Expiry Date": "N/A",
            "Last Updated": "N/A",
            "Registrant Country": "N/A",
        }

def format_date_field(date_value):
    
    if not date_value:
        return "N/A"
    if isinstance(date_value, list):
        formatted_dates = [d.strftime("%Y-%m-%d") for d in date_value if isinstance(d, datetime)]
        return ", ".join(formatted_dates) if formatted_dates else "N/A"
    if isinstance(date_value, datetime):
        return date_value.strftime("%Y-%m-%d")
    return str(date_value)

def write_to_csv(records, output_filename="domain_info.csv"):
   
    fieldnames = ["Domain", "Registrar", "Creation Date", "Expiry Date", "Last Updated", "Registrant Country"]
    with open(output_filename, "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for record in records:
            writer.writerow(record)

if __name__ == "__main__":
    domain_list = []
    print("Please enter domain names one at a time. Type 'done' to finish and save the results.")

    while True:
        user_input = input("Enter domain name (or 'done' to finish): ").strip()
        if user_input.lower() == "done" or user_input == "":
            break
        details = fetch_domain_details(user_input)
        if details:
            domain_list.append(details)

    if domain_list:
        write_to_csv(domain_list)
        print("✅ All domain info saved successfully to 'domain_info.csv'.")
    else:
        print("No domain information was collected to save.")
