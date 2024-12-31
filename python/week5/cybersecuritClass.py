class Cybersecurity:
    def __init__(self, security_level, is_firewall_active):
        self.security_level = security_level
        self.is_firewall_active = is_firewall_active
        
    def display_info(self):
        print(f"Security Level: {self.security_level}")
        print(f"Firewall Active: {self.is_firewall_active}")
        
    def run_security_check(self):
        print("Running general security check...")

class Antivirus(Cybersecurity):
    def __init__(self, security_level, is_firewall_active, virus_definition_version):
        super().__init__(security_level, is_firewall_active)  # Call the parent constructor
        self.virus_definition_version = virus_definition_version
        
    def run_security_check(self):
        print(f"Running antivirus security check with definition version {self.virus_definition_version}...")

    def display_antivirus_info(self):
        self.display_info()
        print(f"Virus Definition Version: {self.virus_definition_version}")

if __name__ == "__main__":
    general_security = Cybersecurity("High", True)
    general_security.display_info()
    general_security.run_security_check()

    print("\n--- Antivirus System ---")
    antivirus = Antivirus("Very High", True, "v2024.01")
    antivirus.display_antivirus_info()
    antivirus.run_security_check()
