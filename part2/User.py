class User:
    def __init__(self, username):
        self.username = username
        self.assigned_text_zones = set()

    def assign_text_zone(self, text_zone):
        if text_zone.user is None:
            text_zone.user = self
            self.assigned_text_zones.add(text_zone)
            return True
        else:
            return False

    def unassign_all_text_zones(self):
        for text_zone in self.assigned_text_zones:
            text_zone.user = None
        self.assigned_text_zones = set()


