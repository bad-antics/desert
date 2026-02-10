from desert.core import DesertEngine
d=DesertEngine()
for dt in ["physical","digital","cultural","temporal"]:
    info=d.explore(dt)
    print(f"{dt}: {info.get('quote','N/A')}")
print(f"\nVoid index: {d.void_index({'mass_media':True,'social_media':True,'simulation':True})}")
print(f"Meditation: {d.generate_meditation()}")
