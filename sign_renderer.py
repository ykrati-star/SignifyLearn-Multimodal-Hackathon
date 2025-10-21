# sign_renderer.py

class SignRenderer:
    """
    Maps simplified text/summary to the appropriate ISL animation codes.
    """
    def __init__(self):
        # Conceptual ISL code mapping based on a dataset
        self.isl_map = {
            "key takeaway": "ISL-CODE-T",
            "solution": "ISL-CODE-S",
            "equation": "ISL-CODE-E",
            "crucial concept": "ISL-CODE-C",
        }
        print("Sign Renderer: ISL Code Map loaded.")

    def get_sign_animation(self, summary_text: str) -> str:
        """
        Returns the synchronized sign code based on the fused summary text.
        """
        
        # Simple lookup logic for the most relevant sign word
        for key, code in self.isl_map.items():
            if key in summary_text.lower():
                return code # Return the most relevant sign
                
        return "ISL-CODE-DEFAULT" # If no match, return a default sign