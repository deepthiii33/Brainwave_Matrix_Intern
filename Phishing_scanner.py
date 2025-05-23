import re
import time
from urllib.parse import urlparse
from fuzzywuzzy import fuzz

# Some known brands to compare against
known_brands = ['google.com', 'paypal.com', 'amazon.com', 'microsoft.com', 'facebook.com','netflix.com',
                 'linkedin.com', 'instagram.com', 'youtube.com','apple.com', 'whatsapp.com', 
                 'tiktok.com', 'snapchat.com']

# Some common suspicious keywords in phishing links
suspicious_keywords = ['support', 'service', 'login', 'account', 'verify', 'update', 'secure', 'confirm', 
                       'free', 'password']

# Common shortened URL domains
shorteners = ['bit.ly', 'tinyurl.com', 'goo.gl', 't.co', 'rebrand.ly', 'b.link','short.io', 'cutt.ly', 'lnkd.in']

# Validate and clean input
def clean_url(raw_url):
    raw_url = raw_url.strip()

    if not raw_url:
        return None

    # Basic structure checking
    if not re.match(r"^https?://[^\s]+\.[^\s]+", raw_url):
        return None

    return raw_url

# Check if a URL is suspicious
def is_suspicious_url(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    path = parsed_url.path
    reasons = []

    # 1. Checking if IP address used as domain
    if re.match(r"^https?:\/\/(\d{1,3}\.){3}\d{1,3}", url):
        reasons.append("Uses IP address instead of domain")

    # 2. Checking for Known URL shortener
    base_domain = '.'.join(domain.split('.')[-2:])
    if base_domain in shorteners:
        reasons.append("Uses a known URL shortener")

    # 3. Too many digits in domain
    if sum(c.isdigit() for c in domain) > 5:
        reasons.append("Domain contains too many digits")

    # 4. Contains '@' symbol
    if '@' in url:
        reasons.append("Contains '@' symbol (can mask real domain)")

    # 5. Suspicious keywords in full URL
    if any(word in url.lower() for word in suspicious_keywords):
        reasons.append("Contains suspicious keyword(s)")

    # 6. URL does not use HTTPS
    if not url.lower().startswith("https://"):
        reasons.append("URL does not use HTTPS")

    # 7. Brand impersonation (fuzzy match)
    for brand in known_brands:
        score = fuzz.partial_ratio(domain.lower(), brand)
        domain_clean = domain.lower().replace("www.", "")
        if score > 80 and domain_clean != brand:
            reasons.append(f"Domain may imitate brand: '{brand}'")
            break

    return (len(reasons) > 0), (reasons if reasons else ["No red flags found"])

# CLI interaction
def main():
    print("🔍 Welcome to the Phishing Link Scanner!")
    print("Paste one or more URLs (separated by commas), and check them for suspicious signs.\n")
    urls = input("Enter URL(s): ").split(',')

    for raw_url in urls:
        cleaned_url = clean_url(raw_url)

        if not cleaned_url:
            print(f"\n⛔ Skipping invalid input: '{raw_url.strip()}'")
            continue

        print(f"\n🔗 Scanning: {cleaned_url}")
        time.sleep(1)

        is_suspicious, reasons = is_suspicious_url(cleaned_url)

        if is_suspicious:
            print("⚠️ This URL looks suspicious. Here's why:")
            for reason in reasons:
                print(f" - {reason}")
        else:
            print("✅ This URL looks safe. No red flags found.")

        time.sleep(1.2)

if __name__ == "__main__":
    main()
