class ScoreManager:
    def __init__(self, file_path = "HS.txt"):
        self.file_path = file_path
        self.score = 0
        self.high_score = self._load_high_score()

    def _load_high_score(self):
        try:
            with open(self.file_path, "r") as f:
                return int(f.read())
        except:
            return 0

    def add_points(self, points):
        self.score += points

    def get_score(self):
        return self.score

    def get_high_score(self):
        return self.high_score

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(self.file_path, "w") as f:
                f.write(str(self.high_score))
            return True  # New high score
        return False  # Not a new high score