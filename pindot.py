import click

@click.command()
@click.option("--name", prompt="Enter your name:",help="The Name of the user")
def hello(name):
  click.echo(f"Hello{name}!")


PRIORITIES={
  "Y":"Agree", #add_todo a choice to prio
  "N":"Not Agree",
  "U":"Undecided",
  "M":"Medium",
  "H":"High",
  "L":"Low",
  
  


}

@click.command()
@click.option("--priority",type=click.Choice(PRIORITIES.keys()),default ="Y")
#another argument to propose the to_do_choose file_prio which is the click, if exist is false then the path of file doesn't exist but if it is True then the path of file is existing.
@click.argument("todofile",type=click.Path(exists=False), required=0)
#another argument to propose the option created items in the PRIORITIES, that is connected to the definition of data(name ,description, etc)
@click.option("-n","--name", prompt="Enter the todo name", help="The name of the todo items")
@click.option("-d","--desc", prompt="Describe the todo", help="The description of the todo items")
def add_todo(name,description,priority,age,todofile):
  filename=todofile if todofile is not None else "mytodos.txt"
#append to where the todofile will be open 
  with open(filename, "a+")as f:
    f.write(f"{name}:{description}[Priority:{PRIORITIES[priority]}")
  if __name__ == "__main__":
    hello()
    input("Press Enter to exit...")