import whois 
from datetime import datetime 
import re
import requests 
from bs4 import BeautifulSoup 

def analyze_url(url): 
    risk = 0 
    findings = [] 
    
    # IP Address Detection 
    ip_pattern = r"(\d{1,3}\.){3}\d{1,3}" 
    if re.search(ip_pattern, url): 
        findings.append("⚠️ IP Address Used Instead of Domain") 
        risk += 25 
        
    # URL Shortener Detection 
    shorteners = [ "bit.ly", "tinyurl.com", "t.co", "goo.gl" ] 
    for shortener in shorteners: 
        if shortener in url.lower(): 
            findings.append("⚠️ URL Shortener Used") 
            risk += 20 
            
    # HTTPS Check 
    if url.startswith("https"): 
        findings.append("✅ HTTPS detected") 
    else: 
        findings.append("⚠️ Not Secure") 
        risk += 30 
        
    # URL Length 
    if len(url) > 50: 
        findings.append("⚠️ Long URL") 
        risk += 20 
        
    # @ Symbol 
    if "@" in url: 
        findings.append("⚠️ @ found") 
        risk += 30 
        
    # Suspicious Keywords 
    suspicious_words = [ "login", "verify", "update", "secure", "bank" ] 
    for word in suspicious_words: 
        if word in url.lower(): 
            findings.append(f"⚠️ Suspicious keyword: {word}") 
            risk += 15 
            
    # Form Detection 
    try: 
        response = requests.get(url, timeout=5) 
        soup = BeautifulSoup( response.text, "html.parser" ) 
        forms = soup.find_all("form") 
        if forms: 
            findings.append("🔐 Login Form Found") 
        else: 
            findings.append("❌ No Form Found") 
    except: 
        findings.append("⚠️ Website Not Reachable") 
    

    # Domain Age Check 
    try: 
        domain_info = whois.whois(url) 
        creation_date = domain_info.creation_date 
        
        if isinstance(creation_date, list): 
            creation_date = creation_date[0] 
        if creation_date: 
            age_days = ( 
                        datetime.now() - 
                        creation_date.replace(tzinfo=None) 
            ).days 
            findings.append( 
                            f"Domain Age: {age_days} days"
            ) 
            if age_days < 365: 
                    findings.append( 
                                    "⚠️ Newly Registered Domain" 
                    ) 
                    risk += 25 
    except: 
        findings.append( "⚠️ Domain Age Not Available" )

    return risk, findings 

