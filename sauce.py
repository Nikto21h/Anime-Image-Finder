from saucenao_api import SauceNao

url = input("Paste image url here: ")
sauce = SauceNao()
results = sauce.from_url(url)
yn = input(f"I've found {results.long_remaining} images, may i show some of them? (y/n)")
if yn == "y":
    try:
        for i in range (int(results.long_remaining)):
            print(f"Title: {results[i].title} | Similarity {results[i].similarity} | Url: {results[i].urls}")
        
    except:
        pass
else:
    pass