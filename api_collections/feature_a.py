import dotenv

dotenv.load_dotenv()

class FeatureA():
    def __init__(self):
        pass

    def get_status(self):
        try:
            return "feature A is working"
        except Exception as e:
            return {"error": str(e)}