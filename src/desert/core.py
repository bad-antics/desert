"""Desert Metaphor Engine"""
import json,random

class DesertEngine:
    METAPHORS={
        "physical":{"description":"The American desert as sublime emptiness",
                    "quote":"The desert is a sublime form of disappearance.",
                    "interpretation":"Physical vastness mirrors conceptual void"},
        "digital":{"description":"Information desert - data without meaning",
                   "quote":"We are in a desert of information and meaning.",
                   "interpretation":"Proliferation of data creates meaning drought"},
        "cultural":{"description":"Cultural desert - simulation replaces depth",
                    "quote":"Culture is always that which is already dead.",
                    "interpretation":"Mass culture evacuates authentic experience"},
        "temporal":{"description":"Time desert - eternal present",
                    "quote":"The end of history is not a dramatic event.",
                    "interpretation":"Without future or past, we inhabit empty now"},
    }
    
    def explore(self,desert_type):
        return self.METAPHORS.get(desert_type,{})
    
    def void_index(self,cultural_factors):
        score=0
        if cultural_factors.get("mass_media"): score+=20
        if cultural_factors.get("consumerism"): score+=20
        if cultural_factors.get("social_media"): score+=20
        if cultural_factors.get("simulation"): score+=20
        if cultural_factors.get("spectacle"): score+=20
        return {"void_index":score,"state":"Desert" if score>60 else "Oasis" if score<30 else "Mirage"}
    
    def generate_meditation(self):
        meditations=[
            "In the desert of the real, every oasis is a mirage.",
            "The void is not empty — it is full of the absence of meaning.",
            "To cross the desert is to discover that the other side is also desert.",
            "Silence in the desert speaks louder than all the noise of civilization.",
        ]
        return random.choice(meditations)
