import dotenv

dotenv.load_dotenv()

class FeatureB():
    def __init__(self):
        pass

    def get_status(self):
        try:
            return "feature B is working"
        except Exception as e:
            return {"error": str(e)}