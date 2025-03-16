class SocialMediaIntegration:
    def __init__(self, user_id, social_media_type, access_token):
        self.user_id = user_id
        self.social_media_type = social_media_type
        self.access_token = access_token

    def share_progress(self, message):
        print(f"Sharing progress to {self.social_media_type}: {message}")