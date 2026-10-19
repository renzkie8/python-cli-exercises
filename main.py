import typer

app = typer .Typer()

EMOTIONS = ["happy", "sad","angry","excited"]
#CHORES = ["cleaning", "cooking", "gaming", "reading"]

@app.command()
def hello(name: str,age:int,iq:int,display_age: bool= True,display_iq : bool=True):
  print(f"Hello{name}")
  print(f"Age{age}")
  print(f"Your IQ is {iq}")

#@app.command()
#def how_are_you(emotion: typer.Choice(EMOTIONS), chores:typer.Choice(CHORES)):
  #print(f"How are you{emotion}")
  #print(f"What are you doing{chores}")

  if __name__ == "__main__":
    app()
    