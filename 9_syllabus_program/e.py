# Write a code that takes email id as input. Extract top level domain name and print as output

def extract_tld(email):
    try:
        username, domain = email.split('@')
    except ValueError:
        return "Invalid email format"

    domain_parts = domain.split('.')
    if len(domain_parts) < 2:
        return "Invalid email format"

    tld = domain_parts[-1]
    return tld


email = input("Enter email: ")
tld = extract_tld(email)
print("Top-level domain:", tld)
    
