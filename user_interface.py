class UserInterface:
    def run(self, main_function):
        try:
            main_function()
        except Exception as e:
            print("Bir hata oluştu: " + str(e))

    def get_menu_option(self):
        print("\nMenü:")
        print("1. XSS açığı kontrolü")
        print("2. SQL enjeksiyonu kontrolü")
        print("3. Dizin yolunu geçme kontrolü")
        print("4. Komut enjeksiyonu kontrolü")
        print("5. Admin paneli bulma")
        print("0. Çıkış")

        option = input("Seçenek numarasını girin: ")
        return option

    def get_url(self):
        url = input("URL'yi girin: ")
        return url

    def show_vulnerabilities(self, vulnerabilities):
        if vulnerabilities:
            print("\nBulunan açıklar:")
            for vulnerability in vulnerabilities:
                print(vulnerability)
        else:
            print("\nHerhangi bir açık bulunamadı.")

    def show_admin_panel(self, admin_panel):
        if admin_panel:
            print("\nAdmin paneli bulundu: " + admin_panel)
        else:
            print("\nAdmin paneli bulunamadı.")
