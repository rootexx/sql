import requests

class AdminPanelFinder:
    def find_admin_panel(self, urls):
        common_admin_paths = [
            "/admin",
            "/admin/login",
            "/admin_panel",
            "/administrator",
            "/moderator",
            "/webadmin",
            "/wp-admin",
            "/user",
            "/controlpanel",
        ]

        found_admin_panel = None

        for url in urls:
            for path in common_admin_paths:
                admin_url = url + path
                response = requests.get(admin_url)
                if response.status_code == 200:
                    found_admin_panel = admin_url
                    break

            if found_admin_panel:
                break

        return found_admin_panel
