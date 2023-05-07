from checks import XSSChecker, SQLInjectionChecker, DirectoryTraversalChecker, CommandInjectionChecker
from admin_panel_finder import AdminPanelFinder
from user_interface import UserInterface

def main():
    user_interface = UserInterface()
    xss_checker = XSSChecker()
    sql_injection_checker = SQLInjectionChecker()
    directory_traversal_checker = DirectoryTraversalChecker()
    command_injection_checker = CommandInjectionChecker()
    admin_panel_finder = AdminPanelFinder()

    while True:
        option = user_interface.get_menu_option()

        if option == "0":
            print("Programdan çıkılıyor...")
            break
        elif option == "1":
            url = user_interface.get_url()
            vulnerabilities = xss_checker.check(url)
            user_interface.show_vulnerabilities(vulnerabilities)
        elif option == "2":
            url = user_interface.get_url()
            vulnerabilities = sql_injection_checker.check(url)
            user_interface.show_vulnerabilities(vulnerabilities)
        elif option == "3":
            url = user_interface.get_url()
            vulnerabilities = directory_traversal_checker.check(url)
            user_interface.show_vulnerabilities(vulnerabilities)
        elif option == "4":
            url = user_interface.get_url()
            vulnerabilities = command_injection_checker.check(url)
            user_interface.show_vulnerabilities(vulnerabilities)
        elif option == "5":
            urls = []
            num_urls = int(input("Kaç adet URL gireceksiniz: "))

            for i in range(num_urls):
                url = user_interface.get_url()
                urls.append(url)

            admin_panel = admin_panel_finder.find_admin_panel(urls)
            user_interface.show_admin_panel(admin_panel)
        else:
            print("Geçersiz bir seçenek girdiniz. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
from checks import XSSChecker, SQLInjectionChecker, DirectoryTraversalChecker, CommandInjectionChecker
from admin_panel_finder import AdminPanelFinder
from user_interface import UserInterface

def main():
    user_interface = UserInterface()
    xss_checker = XSSChecker()
    sql_injection_checker = SQLInjectionChecker()
    directory_traversal_checker = DirectoryTraversalChecker()
    command_injection_checker = CommandInjectionChecker()
    admin_panel_finder = AdminPanelFinder()

    while True:
        option = user_interface.get_menu_option()

        if option == "0":
            print("Programdan çıkılıyor...")
            break
        elif option == "1":
            url = user_interface.get_url()
            vulnerabilities = xss_checker.check(url)
            user_interface.show_vulnerabilities(vulnerabilities)
        elif option == "2":
            url = user_interface.get_url()
            vulnerabilities = sql_injection_checker.check(url)
            user_interface.show_vulnerabilities(vulnerabilities)
        elif option == "3":
            url = user_interface.get_url()
            vulnerabilities = directory_traversal_checker.check(url)
            user_interface.show_vulnerabilities(vulnerabilities)
        elif option == "4":
            url = user_interface.get_url()
            vulnerabilities = command_injection_checker.check(url)
            user_interface.show_vulnerabilities(vulnerabilities)
        elif option == "5":
            urls = []
            num_urls = int(input("Kaç adet URL gireceksiniz: "))

            for i in range(num_urls):
                url = user_interface.get_url()
                urls.append(url)

            admin_panel = admin_panel_finder.find_admin_panel(urls)
            user_interface.show_admin_panel(admin_panel)
        else:
            print("Geçersiz bir seçenek girdiniz. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
